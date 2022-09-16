import datetime as _dt

import pydantic as _pydantic 

class _CarBase(_pydantic.BaseModel): 
    owner: int
    model: str
    vehicle_mileage: int
    license_plate: str

    class Config:
        orm_mode = True 

class CarList(_CarBase):
	pass

class CarCreate(_CarBase):
	pass