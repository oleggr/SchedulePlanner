from fastapi import FastAPI

from scheduler.routes import router


def get_application() -> FastAPI:
    application = FastAPI()
    application.include_router(router, prefix="/api")

    return application


app = get_application()
