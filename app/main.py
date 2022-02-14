from fastapi import FastAPI
from flexit import queries

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World!"}


@app.get("/shows_of_actor/{actor}")
async def shows_of_actor(actor):
    return {"message": queries.shows_of_actor(actor)}


@app.get("/health_check")
async def health_check():
    return {"message": "Looks like the app is healthy"}
