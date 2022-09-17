from typing import List
import fastapi as _fastapi
import fastapi.security as _security
from fastapi.middleware.cors import CORSMiddleware
from fastapi_pagination import LimitOffsetPage, Page, add_pagination
from fastapi_pagination.ext.sqlalchemy import paginate

import sqlalchemy.orm as _orm

import app.services as _services
import app.schemas as _schemas

router = _fastapi.APIRouter()

@router.put("/car")
def update_car(car: _schemas.CarUpdate, db: _orm.Session = _fastapi.Depends(_services.get_db)):
	ok = _services.check_car_by_license_plate(car.license_plate, db)
	if ok == False:
		raise _fastapi.HTTPException(status_code=404, detail="The car was not found")
	return _services.update_car(car, db)


@router.post("/car")
def create_car(car: _schemas.CarCreate, db: _orm.Session = _fastapi.Depends(_services.get_db)):
    ok = _services.check_car_by_license_plate(car.license_plate, db)
    if ok == True:
    	return _services.update_car(car, db)
    return _services.create_car(car, db)


@router.get("/car/{car_id}")
def get_car_by_id(car_id: str, db: _orm.Session = _fastapi.Depends(_services.get_db)):
	return _services.get_car_by_license_plate(car_id, db)


@router.get("/car", response_model=Page[_schemas.CarList])
@router.get("/car/limit-offset", response_model=LimitOffsetPage[_schemas.CarList])
def car_list(db: _orm.Session = _fastapi.Depends(_services.get_db)):
	return paginate(_services.car_list(db))


@router.delete("/car/{car_id}")
def delete_car(car_id: str, db: _orm.Session = _fastapi.Depends(_services.get_db)):
	ok = _services.get_car_by_license_plate(car_id, db)
	if ok == False:
		raise _fastapi.HTTPException(status_code=404, detail="The car was not found")
	return _services.delete_car(car_id, db)


@router.get("/")
def root():
    return {"message" : 'PRIVET S BECKEND-a'}


add_pagination(router)