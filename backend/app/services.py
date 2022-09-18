import sqlalchemy.orm as _orm
import app.database as _database
import app.models as _models
import app.schemas as _schemas


def create_database():
    return _database.Base.metadata.create_all(bind=_database.engine)


def get_db():
    db = _database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_car_by_license_plate(license_plate: str, db: _orm.Session):
    return db.query(_models.Car).\
           filter(_models.Car.license_plate == license_plate).first()


def check_car_by_license_plate(license_plate: str, db: _orm.Session):
    return db.query(_models.Car).\
           filter(_models.Car.license_plate == license_plate).count() > 0


def update_car(car: _models.Car, db: _orm.Session):
    old_car = db.query(_models.Car).\
              filter(_models.Car.license_plate == car.license_plate).first()
    if car.owner is not None:
        old_car.owner = car.owner
    if car.model is not None:
        old_car.model = car.model
    if car.vehicle_mileage is not None:
        old_car.vehicle_mileage = car.vehicle_mileage
    db.commit()
    return db.query(_models.Car).\
           filter(_models.Car.license_plate == car.license_plate).first()


def create_car(car: _schemas.CarCreate, db: _orm.Session):
    car_obj = _models.Car(**car.dict())
    db.add(car_obj)
    db.commit()
    db.refresh(car_obj)
    return car_obj


def delete_car(car_id: _schemas.CarDelete, db: _orm.Session):
    q = db.query(_models.Car).\
        filter(_models.Car.license_plate == car_id).\
        delete(synchronize_session='fetch')
    db.commit()
    return q


def car_list(db: _orm.Session):
    return db.query(_models.Car)
