import datetime as _dt

import sqlalchemy as _sql
import sqlalchemy.ext.declarative as _declarative
import sqlalchemy.orm as _orm

import app.database as _database


class Car(_database.Base):
    __tablename__ = "cars"
    license_plate = _sql.Column(_sql.String(50), primary_key=True)
    model = _sql.Column(_sql.String(250), default=None)
    owner = _sql.Column(_sql.BIGINT, default=None)
    vehicle_mileage = _sql.Column(_sql.Integer, default=None)
