from sqlalchemy.orm import Session
from models import Rectangle
from database import SessionLocal, create_database

sample_data = [
    {"x1": 0, "y1": 0, "x2": 2, "y2": 2},
    {"x1": 1, "y1": 1, "x2": 3, "y2": 3},
    {"x1": 2, "y1": 2, "x2": 4, "y2": 4},
]


def populate_db():
    db = SessionLocal()
    try:
        for data in sample_data:
            db.add(Rectangle(**data))
        db.commit()
    except Exception as e:
        print(f"Error populating database: {e}")
        db.rollback()
    finally:
        db.close()


if __name__ == "__main__":
    create_database()
    populate_db()
