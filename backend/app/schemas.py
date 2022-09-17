import datetime as _dt

import pydantic as _pydantic 

class _CarBase(_pydantic.BaseModel): 
    license_plate: str

    class Config:
        orm_mode = True 

class CarUpdate(_CarBase):
    owner: int = None
    model: str = None
    vehicle_mileage: int = None

class CarList(_CarBase):
    owner: int
    model: str
    vehicle_mileage: int

class CarCreate(_CarBase):
    owner: int
    model: str
    vehicle_mileage: int

class CarDelete(_CarBase):
	pass