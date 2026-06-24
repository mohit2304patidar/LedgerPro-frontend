from app.models.category import Category

def create_category(db, category_data):
    category = Category(
        **category_data.model_dump()
    )
    db.add(category)
    db.commit()
    db.refresh(category)

    return category

def get_categories(db):
    return db.query(Category).all()