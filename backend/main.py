from random import randint
import time

import fastapi as _fastapi
from starlette.requests import Request
from starlette.responses import Response
from loguru import logger

from routes import routes
from app.database import SessionLocal
import logs

app = _fastapi.FastAPI(
    title="Simple crud task by coproreality",
    version="1.0.0"
)

logs.init_logging("./config/log_config.json", False)
middleware_logger = logger.bind(type="middleware")


@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    log = middleware_logger.bind(request_id=randint(1_000_000_000, 9_999_999_999))

    request.logger = log

    log.info(f"Request from {request.url}. Path: {request.url.path}, Method: {request.method}")

    response = Response("Internal server error", status_code=500)
    start_time = time.time()
    try:
        start_time = time.time()
        request.state.db = SessionLocal()
        response = await call_next(request)
    except Exception as e:
        log.info(
            f"Path params: {request.path_params if request.path_params else dict()}|"
            f"Query params: {request.query_params if request.query_params else dict()}| "
            f"Headers:{request.headers.items()}")
        log.exception(str(e))
    finally:
        request.state.db.close()

    log.info(f"Request from {request.url} was processed in {time.time() - start_time} secs.")
    return response


app.include_router(routes)
