from app.models.ledger_group import LedgerGroup

def create_group(db, group_data):
    group = LedgerGroup(
        **group_data.model_dump()
    )

    db.add(group)
    db.commit()
    db.refresh(group)
    return group

def get_groups(db):
    return db.query(LedgerGroup).all()