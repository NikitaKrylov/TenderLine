from fastapi import FastAPI, APIRouter
from fastapi.staticfiles import StaticFiles
from backend.api.auth.routes import router as auth_router
from backend.api.chat.routes import router as chat_router
from backend.api.documents.router import router as doc_router
from .api.database import init_models
from .web_endpoints import router as web_router


def create_app() -> FastAPI:
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(init_models())
    # asyncio.run(init_models())
    # Base.metadata.drop_all(engine)
    # Base.metadata.create_all(engine)

    _app = FastAPI()
    _app.mount('/static', StaticFiles(directory='frontend/static'), name='static')

    _app.include_router(web_router)
    _app.include_router(chat_router)
    _app.include_router(auth_router)
    _app.include_router(doc_router)

    return _app


app = create_app()


@app.on_event("startup")
async def on_startup():
    # await init_models()
    pass