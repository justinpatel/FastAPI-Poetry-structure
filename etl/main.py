from fastapi import FastAPI
from api.app.routers import default
from api.core.config import Settings

import uvicorn


def include_router(app):
    app.include_router(default.router)

def start_application():
    app = FastAPI(version=Settings.APP_VERSION)
    include_router(app)
    return app

if __name__ ==  "__main__":
    app = start_application()
    uvicorn.run(app, host = Settings.APP_HOST, port = int(Settings.APP_PORT))