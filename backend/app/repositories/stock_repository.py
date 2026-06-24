from sqlalchemy import func
from app.models.stock_movement import StockMovement
from app.models.product import Product

def create_stock_movement(db, stock_data):
    movement = StockMovement(
        **stock_data.model_dump()
    )

    db.add(movement)
    db.commit()
    db.refresh(movement)

    return movement

def get_current_stock(db, product_id):
    stock = db.query(
        func.sum(StockMovement.quantity)
    ).filter(
        StockMovement.product_id == product_id
    ).scalar()

    return float(stock or 0)

def get_stock_summary(db):
    products = db.query(Product).all()
    result = []

    for product in products:
        purchase_qty = (
            db.query(
                func.coalesce(
                    func.sum(StockMovement.quantity),
                    0
                )
            )
            .filter(
                StockMovement.product_id == product.id,
                StockMovement.movement_type == "PURCHASE"
            )
            .scalar()
        )

        sale_qty = (
            db.query(
                func.coalesce(
                    func.sum(StockMovement.quantity),
                    0
                )
            )
            .filter(
                StockMovement.product_id == product.id,
                StockMovement.movement_type == "SALE"
            )
            .scalar()
        )

        current_stock = (
            product.opening_stock
            + purchase_qty
            - sale_qty
        )

        result.append({
            "product_id": product.id,
            "product_name": product.name,
            "opening_stock": product.opening_stock,
            "purchase_qty": purchase_qty,
            "sale_qty": sale_qty,
            "current_stock": current_stock
        })

    return result

def get_stock_ledger(db, product_id: int):
    
    entries = (
        db.query(StockMovement)
        .filter(
            StockMovement.product_id == product_id
        )
        .order_by(
            StockMovement.created_at
        )
        .all()
    )

    result = []

    for entry in entries:

        qty_in = 0
        qty_out = 0

        if entry.movement_type == "PURCHASE":
            qty_in = float(entry.quantity)

        elif entry.movement_type == "SALE":
            qty_out = float(entry.quantity)

        result.append({
            "date": entry.created_at,
            "movement_type": entry.movement_type,
            "quantity_in": qty_in,
            "quantity_out": qty_out,
            "rate": float(entry.rate)
        })

    return result