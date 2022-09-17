from fastapi import APIRouter

from app.handlers import router

routes = APIRouter()

routes.include_router(router, prefix="/api")
