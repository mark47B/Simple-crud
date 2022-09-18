import fastapi as _fastapi
import fastapi.security as _security
from starlette.requests import Request
from starlette.responses import Response
from fastapi.middleware.cors import CORSMiddleware

import sqlalchemy.orm as _orm

import app.services as _services
import app.schemas as _schemas
from routes import routes
from app.database import SessionLocal


app = _fastapi.FastAPI(
    title="Simple crud task by corporeality",
    version="1.0.0"
)


@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = Response("Internal server error", status_code=500)
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response

app.include_router(routes)
