from fastapi import FastAPI

from app.api.api_v1 import api_router

app = FastAPI(title="Flexit-API", docs_url="/", redoc_url=None, version="1.0.0")
app.include_router(api_router)


@app.get("/health_check", tags=["utilities"])
async def health_check():
    return {"message": "Looks like the app is healthy"}
