import fastapi as _fastapi
import fastapi.security as _security
from fastapi.middleware.cors import CORSMiddleware

import sqlalchemy.orm as _orm

import app.services as _services
import app.schemas as _schemas

app = _fastapi.FastAPI()
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=['*'],
#     allow_credentials=True,
#     allow_methods=['*'],
#     allow_headers=['*'],
# )

@app.post("/api/do_car")
async def create_car(car: _schemas.CarCreate, db: _orm.Session = _fastapi.Depends(_services.get_db)):
    db_car = _services.get_car_by_license_plate(car.license_plate, db)
    if db_car:
        raise _fastapi.HTTPException(status_code=400, detail="The license plate already exists")
    return await _services.create_car(car, db)

# # Не дописано
# @app.delete("/api/car/{car_id}", status_code=204)
# async def delete_car(car_id: int):
#     pass


# @app.put("/api/car/{car_id}", status_code=204)
# async def update_car(car_id: int):
#     pass

@app.get("/api")
async def root():
    return {"message" : 'PRIVET S BECKEND-a'}