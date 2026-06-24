from app.models.unit import Unit

def create_unit(db, unit_data):
    unit =Unit(
        **unit_data.model_dump()
    )
    db.add(unit)
    db.commit()
    db.refresh(unit)

    return unit

def get_units(db):
    return db.query(Unit).all()