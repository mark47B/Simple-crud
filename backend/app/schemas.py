import datetime as _dt

import pydantic as _pydantic


class _CarBase(_pydantic.BaseModel):
    license_plate: str

    class Config:
        orm_mode = True


class CarUpdate(_CarBase):
    owner: _pydantic.PositiveInt = None
    model: str = None
    vehicle_mileage: _pydantic.PositiveInt = None


class CarList(_CarBase):
    owner: _pydantic.PositiveInt
    model: str
    vehicle_mileage: _pydantic.PositiveInt


class CarCreate(_CarBase):
    owner: _pydantic.PositiveInt
    model: str
    vehicle_mileage: _pydantic.PositiveInt


class CarDelete(_CarBase):
    pass
