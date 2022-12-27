from fastapi import FastAPI, APIRouter

from app.api.api_v1.api import api_router
from app.core.config import settings

root_router = APIRouter()
app = FastAPI(title="Wanker API", openapi_url=f"/openapi.json")


@root_router.get("/", status_code=200)
def root() -> dict:
    """
    Root GET
    """

    return {"status": "ok"}


app.include_router(api_router, prefix=settings.API_V1_STR)
app.include_router(root_router)
