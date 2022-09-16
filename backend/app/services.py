import sqlalchemy.orm as _orm
import app.database as _database, app.models as _models, app.schemas as _schemas
from app.models import Car

def create_database():
    return _database.Base.metadata.create_all(bind=_database.engine)


def get_db():
    db = _database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_car_by_license_plate(license_plate: str, db: _orm.Session):
    return db.query(_models.Car.license_plate == license_plate).first()

# Дописать схему создания машины + дописать сюда заполнение полей 
def create_car(car: _schemas.CarCreate, db: _orm.Session):
    car_obj = _models.Car(**car.dict())
    db.add(car_obj)
    db.commit()
    db.refresh(car_obj)
    return car_obj

def car_list(db: _orm.Session):
    return db.query(Car).all()