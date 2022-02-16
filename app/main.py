from fastapi import FastAPI
from api.api_v1.api import api_router


app = FastAPI(docs_url="/", redoc_url=None)
app.include_router(api_router)


@app.get("/health_check")
async def health_check():
    return {"message": "Looks like the app is healthy"}
