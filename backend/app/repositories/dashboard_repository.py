from sqlalchemy import func, extract
from app.models.sale import Sale
from app.models.purchase import Purchase
from app.models.customer import Customer
from app.models.supplier import Supplier
from app.models.product import Product
from app.models.stock_movement import StockMovement
from app.models.sale_item import SaleItem
from app.repositories.stock_repository import get_current_stock


def get_dashboard_data(db):
    total_sales = (
        db.query(
            func.coalesce(
                func.sum(Sale.total_amount),
                0
            )
        )
        .scalar()
    )

    total_purchases = (
        db.query(
            func.coalesce(
                func.sum(Purchase.total_amount),
                0
            )
        )
        .scalar()
    )

    total_customers = (
        db.query(Customer).count()
    )

    total_suppliers = (
        db.query(Supplier).count()
    )

    total_products = (
        db.query(Product).count()
    )

    stock_value = (
        db.query(
            func.coalesce(
                func.sum(
                    StockMovement.quantity * StockMovement.rate
                ),
                0
            )
        )
        .scalar()
    )

    return {
        "total_sales": float(total_sales),
        "total_purchases": float(total_purchases),
        "total_customers": float(total_customers),
        "total_suppliers": float(total_suppliers),
        "total_products": float(total_products),
        "stock_value": float(stock_value)
    }

def get_top_selling_products(db, limit=10):

    products = (
        db.query(
            Product.id,
            Product.name,
            func.sum(SaleItem.quantity).label("total_qty")
        )
        .join(
            SaleItem,
            Product.id == SaleItem.product_id
        )
        .group_by(
            Product.id,
            Product.name
        )
        .order_by(
            func.sum(SaleItem.quantity).desc()
        )
        .limit(limit)
        .all()
    )

    return [
        {
            "product_id":  p.id,
            "product_name": p.name,
            "total_qty": float(p.total_qty)
        }
        for p in products
    ]

def get_low_stock_products(db, threshold=5):

    products = db.query(Product).all()

    result = []

    for product in products:
        current_stock = get_current_stock(
            db,
            product.id
        )

        if current_stock <= threshold:

            result.append(
                {
                    "product_id": product.id,
                    "product_name": product.name,
                    "current_stock": float(current_stock)
                }
            )

    result.sort(
        key = lambda x: x["current_stock"]
    )

    return result 

def get_monthly_sales(db):
    
    sales = (
        db.query(
            extract("month", Sale.sale_date).label("month"),
            func.sum(Sale.total_amount).label("sales")
        )
        .group_by(
            extract("month", Sale.sale_date)
        )
        .order_by(
            extract("month", Sale.sale_date)
        )
        .all()
    )

    months = {
        1: "Jan",
        2: "Feb",
        3: "Mar",
        4: "Apr",
        5: "May",
        6: "Jun",
        7: "Jul",
        8: "Aug",
        9: "Sep",
        10: "Oct",
        11: "Nov",
        12: "Dec" 
    }

    result = []

    for row in sales:
        result.append(
            {
                "month": months[int(row.month)],
                "sales": float(row.sales)
            }
        )
    return result

def get_monthly_purchase(db):

    purchases = (
        db.query(
            extract("month", Purchase.purchase_date)
            .label("month")
        )
        .group_by(
            extract("month", Purchase.purchase_date)
        )
        .order_by(
            extract("month", Purchase.purchase_date)
        )
        .all()
    )

    months = {
        1: "Jan",
        2: "Feb",
        3: "Mar",
        4: "Apr",
        5: "May",
        6: "Jun",
        7: "Jul",
        8: "Aug",
        9: "Sep",
        10: "Oct",
        11: "Nov",
        12: "Dec"
    }

    result = []

    for row in purchases:

        result.append(
            {
                "month": months[int(row.months)],
                "purchase": float(row.purchase)
            }
        )

    return result