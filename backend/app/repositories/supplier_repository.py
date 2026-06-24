from app.models.supplier import Supplier
from app.models.ledger import Ledger

def create_supplier(db, supplier_data):
    ledger = Ledger(name = supplier_data.name)
    db.add(ledger)
    db.flush()
    supplier = Supplier(
        supplier_code = supplier_data.supplier_code,
        name = supplier_data.name,
        mobile = supplier_data.mobile,
        email = supplier_data.email,
        gst_number = supplier_data.gst_number,
        pan_number = supplier_data.pan_number,
        address = supplier_data.address,
        city = supplier_data.city,
        state = supplier_data.state,
        ledger_id = ledger.id,
        is_active = True
    )

    db.add(supplier)
    db.commit()
    db.refresh(supplier)

    return supplier

def get_suppliers(db):
    return db.query(Supplier).all()