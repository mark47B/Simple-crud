import datetime as _dt

import sqlalchemy as _sql
import sqlalchemy.ext.declarative as _declarative
import sqlalchemy.orm as _orm

import app.database as _database

class Car(_database.Base):
    __tablename__="cars"
    # Прописывать ли car_название поля или так оставить? codestyle
    license_plate = _sql.Column(_sql.String(50),  primary_key=True) #  Уникальный идентификатор - номер автомобиля
    model = _sql.Column(_sql.String(250), default=None) # Модель автомобиля
    owner = _sql.Column(_sql.Integer, default=None) #  Владелец автомобиля (серия-номер паспорта)
    vehicle_mileage =_sql.Column(_sql.Integer, default=None) # В клиометрах
