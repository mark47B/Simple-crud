import datetime as _dt

import pydantic as _pydantic 

class _CarBase(_pydantic.BaseModel): # Что добавлять в абстрактынй класс?
    owner: int
    
    model: str
    vehicle_mileage: int

class Car(_CarBase):
    id: int


# Нахуй это надо?
class CarCreate(_pydantic.BaseModel):
    license_plate: str

    class Config:
        orm_mode = True 