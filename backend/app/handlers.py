from typing import List
import fastapi as _fastapi
import fastapi.security as _security
from fastapi.middleware.cors import CORSMiddleware

import sqlalchemy.orm as _orm

import app.services as _services
import app.schemas as _schemas

router = _fastapi.APIRouter()


@router.post("/api/do_car")
def create_car(car: _schemas.CarCreate, db: _orm.Session = _fastapi.Depends(_services.get_db)):
    db_car = _services.get_car_by_license_plate(car.license_plate, db)
    #if db_car != None:
    #    raise _fastapi.HTTPException(status_code=400, detail="The license plate already exists")
    return _services.create_car(car, db)

@router.get("/api/list_car", response_model=List[_schemas.CarList])
def car_list(db: _orm.Session = _fastapi.Depends(_services.get_db)):
	return _services.car_list(db)

# Не дописано
#@app.delete("/api/car/{car_id}", status_code=204)
#async def delete_car(car_id: int):
# 	pass


#@app.put("/api/car/{car_id}", status_code=204)
#async def update_car(car_id: int):
#    pass

@router.get("/api")
def root():
    return {"message" : 'PRIVET S BECKEND-a'}