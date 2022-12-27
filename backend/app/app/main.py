from fastapi import FastAPI, APIRouter

root_router = APIRouter()
app = FastAPI(title="Wanker API", openapi_url=f"/openapi.json")

@root_router.get("/", status_code=200)
def root() -> dict:
    """
    Root GET
    """

    return {"status": "ok"}

app.include_router(root_router)
