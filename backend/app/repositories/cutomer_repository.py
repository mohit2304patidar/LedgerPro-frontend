from app.models.customer import Customer
from app.models.ledger import Ledger

def create_customer(db, customer_data):

    ledger = Ledger(name = customer_data.name)

    db.add(ledger)
    db.flush()

    # create customer
    customer = Customer(
        customer_code = customer_data.customer_code,
        name = customer_data.name,
        mobile = customer_data.mobile,
        email = customer_data.email,
        gst_number = customer_data.gst_number,
        pan_number = customer_data.pan_number,
        address = customer_data.address,
        city = customer_data.city,
        state = customer_data.state,
        credit_limit = customer_data.credit_limit,
        ledger_id = ledger.id,
        is_active = True
    )

    db.add(customer)
    db.commit()
    db.refresh(customer)
    
    return customer

def get_customers(db):
    return db.query(Customer).all()