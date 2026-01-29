"""Create a Fabric IQ Ontology for business data understanding.

An Ontology is the foundation of Fabric IQ - it defines:
- Business Entities: Products, Customers, Orders, etc.
- Relationships: Customer HAS Orders, Order CONTAINS Products
- Rules: Business logic like "Premium Customer = >$10K annual spend"
- Actions: What operations can be performed on each entity

The ontology helps the AI agent understand your business context,
enabling accurate natural language to SQL translation.
"""

import os
import json
from pathlib import Path
from dotenv import load_dotenv
from dataclasses import dataclass, asdict
from typing import Optional

# Load environment from azd
azure_dir = Path(__file__).parent.parent / ".azure"
env_name = os.environ.get("AZURE_ENV_NAME", "")
if not env_name and (azure_dir / "config.json").exists():
    with open(azure_dir / "config.json") as f:
        config = json.load(f)
        env_name = config.get("defaultEnvironment", "")

env_path = azure_dir / env_name / ".env"
if env_path.exists():
    load_dotenv(env_path)


# =============================================================================
# ONTOLOGY DATA CLASSES
# =============================================================================

@dataclass
class EntityAttribute:
    """An attribute/column in a business entity."""
    name: str
    data_type: str
    description: str
    is_key: bool = False
    is_measure: bool = False
    format_string: Optional[str] = None


@dataclass 
class EntityRelationship:
    """A relationship between two entities."""
    name: str
    from_entity: str
    to_entity: str
    cardinality: str  # "one-to-many", "many-to-one", "many-to-many"
    description: str


@dataclass
class BusinessRule:
    """A business rule/calculation for derived metrics."""
    name: str
    entity: str
    expression: str
    description: str


@dataclass
class EntityAction:
    """An action that can be performed on an entity."""
    name: str
    entity: str
    description: str
    parameters: list[str]


@dataclass
class BusinessEntity:
    """A business entity (table) in the ontology."""
    name: str
    description: str
    source_table: str
    attributes: list[EntityAttribute]
    
    
@dataclass
class Ontology:
    """Complete Fabric IQ Ontology definition."""
    name: str
    description: str
    entities: list[BusinessEntity]
    relationships: list[EntityRelationship]
    rules: list[BusinessRule]
    actions: list[EntityAction]


# =============================================================================
# CONTOSO RETAIL ONTOLOGY DEFINITION
# =============================================================================

def create_contoso_ontology() -> Ontology:
    """Create the Contoso Retail ontology for the lab."""
    
    # --- Entity: Products ---
    products = BusinessEntity(
        name="Product",
        description="Items available for sale in the Contoso catalog",
        source_table="dbo.Products",
        attributes=[
            EntityAttribute("ProductID", "int", "Unique product identifier", is_key=True),
            EntityAttribute("ProductName", "string", "Display name of the product"),
            EntityAttribute("Category", "string", "Product category (Electronics, Clothing, etc.)"),
            EntityAttribute("SubCategory", "string", "Product sub-category"),
            EntityAttribute("UnitPrice", "decimal", "Current selling price", is_measure=True, format_string="$#,##0.00"),
            EntityAttribute("UnitCost", "decimal", "Cost to acquire/produce", is_measure=True, format_string="$#,##0.00"),
            EntityAttribute("StockLevel", "int", "Current inventory quantity", is_measure=True),
            EntityAttribute("ReorderPoint", "int", "Minimum stock before reorder"),
            EntityAttribute("IsActive", "boolean", "Whether product is currently sold"),
        ]
    )
    
    # --- Entity: Customers ---
    customers = BusinessEntity(
        name="Customer",
        description="Customers who have made purchases",
        source_table="dbo.Customers",
        attributes=[
            EntityAttribute("CustomerID", "int", "Unique customer identifier", is_key=True),
            EntityAttribute("CustomerName", "string", "Full name of the customer"),
            EntityAttribute("Email", "string", "Contact email address"),
            EntityAttribute("Segment", "string", "Customer segment (Consumer, Corporate, Small Business)"),
            EntityAttribute("Region", "string", "Geographic region"),
            EntityAttribute("JoinDate", "date", "Date customer first registered"),
            EntityAttribute("LifetimeValue", "decimal", "Total historical spend", is_measure=True, format_string="$#,##0.00"),
        ]
    )
    
    # --- Entity: Orders ---
    orders = BusinessEntity(
        name="Order",
        description="Customer purchase transactions",
        source_table="dbo.Orders",
        attributes=[
            EntityAttribute("OrderID", "int", "Unique order identifier", is_key=True),
            EntityAttribute("CustomerID", "int", "Reference to customer"),
            EntityAttribute("OrderDate", "date", "Date order was placed"),
            EntityAttribute("ShipDate", "date", "Date order was shipped"),
            EntityAttribute("Status", "string", "Order status (Pending, Shipped, Delivered, Returned)"),
            EntityAttribute("TotalAmount", "decimal", "Total order value", is_measure=True, format_string="$#,##0.00"),
            EntityAttribute("ShippingMethod", "string", "Delivery method selected"),
        ]
    )
    
    # --- Entity: OrderDetails ---
    order_details = BusinessEntity(
        name="OrderLine",
        description="Individual line items within an order",
        source_table="dbo.OrderDetails",
        attributes=[
            EntityAttribute("OrderDetailID", "int", "Unique line item identifier", is_key=True),
            EntityAttribute("OrderID", "int", "Reference to parent order"),
            EntityAttribute("ProductID", "int", "Reference to product"),
            EntityAttribute("Quantity", "int", "Number of units ordered", is_measure=True),
            EntityAttribute("UnitPrice", "decimal", "Price per unit at time of sale", is_measure=True, format_string="$#,##0.00"),
            EntityAttribute("Discount", "decimal", "Discount percentage applied", is_measure=True, format_string="0.0%"),
            EntityAttribute("LineTotal", "decimal", "Quantity * UnitPrice * (1 - Discount)", is_measure=True, format_string="$#,##0.00"),
        ]
    )
    
    # --- Relationships ---
    relationships = [
        EntityRelationship(
            name="CustomerOrders",
            from_entity="Customer",
            to_entity="Order",
            cardinality="one-to-many",
            description="A customer can have many orders"
        ),
        EntityRelationship(
            name="OrderLines",
            from_entity="Order",
            to_entity="OrderLine",
            cardinality="one-to-many",
            description="An order contains multiple line items"
        ),
        EntityRelationship(
            name="ProductOrderLines",
            from_entity="Product",
            to_entity="OrderLine",
            cardinality="one-to-many",
            description="A product can appear in many order lines"
        ),
    ]
    
    # --- Business Rules ---
    rules = [
        BusinessRule(
            name="PremiumCustomer",
            entity="Customer",
            expression="LifetimeValue >= 10000",
            description="Customers with lifetime value >= $10,000 are Premium tier"
        ),
        BusinessRule(
            name="GrossMargin",
            entity="Product",
            expression="(UnitPrice - UnitCost) / UnitPrice",
            description="Profit margin percentage for a product"
        ),
        BusinessRule(
            name="LowStock",
            entity="Product",
            expression="StockLevel <= ReorderPoint",
            description="Product needs to be reordered"
        ),
        BusinessRule(
            name="OrderFulfillmentDays",
            entity="Order",
            expression="DATEDIFF(day, OrderDate, ShipDate)",
            description="Days between order placement and shipment"
        ),
        BusinessRule(
            name="QuarterlySales",
            entity="Order",
            expression="SUM(TotalAmount) WHERE DATEPART(quarter, OrderDate) = @quarter",
            description="Total sales for a given quarter"
        ),
    ]
    
    # --- Actions ---
    actions = [
        EntityAction(
            name="GetTopProducts",
            entity="Product",
            description="Retrieve best-selling products by revenue or quantity",
            parameters=["metric (revenue|quantity)", "limit", "time_period"]
        ),
        EntityAction(
            name="GetCustomerOrders",
            entity="Customer",
            description="Retrieve order history for a specific customer",
            parameters=["customer_id", "date_range"]
        ),
        EntityAction(
            name="GetSalesSummary",
            entity="Order",
            description="Aggregate sales metrics by time period",
            parameters=["group_by (day|week|month|quarter)", "date_range"]
        ),
        EntityAction(
            name="GetInventoryStatus",
            entity="Product",
            description="Check stock levels and identify reorder needs",
            parameters=["category", "include_inactive"]
        ),
    ]
    
    return Ontology(
        name="ContosoRetail",
        description="Semantic model for Contoso Retail business data - enables natural language queries over sales, inventory, and customer data",
        entities=[products, customers, orders, order_details],
        relationships=relationships,
        rules=rules,
        actions=actions,
    )


# =============================================================================
# ONTOLOGY OUTPUT
# =============================================================================

def ontology_to_dict(ontology: Ontology) -> dict:
    """Convert ontology to dictionary for JSON serialization."""
    return {
        "name": ontology.name,
        "description": ontology.description,
        "entities": [
            {
                "name": e.name,
                "description": e.description,
                "sourceTable": e.source_table,
                "attributes": [asdict(a) for a in e.attributes]
            }
            for e in ontology.entities
        ],
        "relationships": [asdict(r) for r in ontology.relationships],
        "businessRules": [asdict(r) for r in ontology.rules],
        "actions": [asdict(a) for a in ontology.actions],
    }


def print_ontology_summary(ontology: Ontology):
    """Print a human-readable summary of the ontology."""
    print(f"\n{'='*60}")
    print(f"ONTOLOGY: {ontology.name}")
    print(f"{'='*60}")
    print(f"\n{ontology.description}\n")
    
    print(f"\n📦 ENTITIES ({len(ontology.entities)})")
    print("-" * 40)
    for entity in ontology.entities:
        key_attrs = [a.name for a in entity.attributes if a.is_key]
        measure_attrs = [a.name for a in entity.attributes if a.is_measure]
        print(f"\n  {entity.name}")
        print(f"    └─ {entity.description}")
        print(f"    └─ Source: {entity.source_table}")
        print(f"    └─ Keys: {', '.join(key_attrs)}")
        print(f"    └─ Measures: {', '.join(measure_attrs)}")
    
    print(f"\n\n🔗 RELATIONSHIPS ({len(ontology.relationships)})")
    print("-" * 40)
    for rel in ontology.relationships:
        arrow = "──>" if "one-to" in rel.cardinality else "──<"
        print(f"  {rel.from_entity} {arrow} {rel.to_entity} ({rel.cardinality})")
        print(f"    └─ {rel.description}")
    
    print(f"\n\n📐 BUSINESS RULES ({len(ontology.rules)})")
    print("-" * 40)
    for rule in ontology.rules:
        print(f"  {rule.name} [{rule.entity}]")
        print(f"    └─ {rule.description}")
        print(f"    └─ Expression: {rule.expression}")
    
    print(f"\n\n⚡ ACTIONS ({len(ontology.actions)})")
    print("-" * 40)
    for action in ontology.actions:
        print(f"  {action.name}({', '.join(action.parameters)})")
        print(f"    └─ {action.description}")


def save_ontology(ontology: Ontology, output_path: Path):
    """Save ontology to JSON file."""
    ontology_dict = ontology_to_dict(ontology)
    
    with open(output_path, "w") as f:
        json.dump(ontology_dict, f, indent=2)
    
    print(f"\n✅ Ontology saved to: {output_path}")


def main():
    print("Creating Fabric IQ Ontology...")
    print("=" * 60)
    print("""
An Ontology is the semantic foundation of Fabric IQ:

  • ENTITIES define your business objects (Products, Customers, Orders)
  • RELATIONSHIPS connect entities (Customer → Orders → Products)  
  • RULES encode business logic (Premium Customer = $10K+ spend)
  • ACTIONS define what questions can be answered

This enables the AI agent to understand business context and
translate natural language questions into accurate SQL queries.
    """)
    
    # Create the ontology
    ontology = create_contoso_ontology()
    
    # Print summary
    print_ontology_summary(ontology)
    
    # Save to file
    output_dir = Path(__file__).parent.parent / "data"
    output_dir.mkdir(exist_ok=True)
    output_path = output_dir / "contoso_ontology.json"
    save_ontology(ontology, output_path)
    
    print(f"\n{'='*60}")
    print("NEXT STEPS")
    print("=" * 60)
    print("""
1. Review the ontology in data/contoso_ontology.json
2. In a real scenario, you would:
   - Import this into Microsoft Fabric
   - Connect it to your Lakehouse/Warehouse tables
   - Configure it in Fabric IQ settings

3. Run '04_create_fabric_agent.py' to create an agent
   that uses this ontology for NL→SQL translation
    """)


if __name__ == "__main__":
    main()
