from fastapi import FastAPI

from app.config import Settings
from app.routes import create, delete, get
from app.routes import list as list_routes

settings = Settings()

app = FastAPI(title=settings.app_name)

app.include_router(create.router)
app.include_router(delete.router)
app.include_router(get.router)
app.include_router(list_routes.router)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
