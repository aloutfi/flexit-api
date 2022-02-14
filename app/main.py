from fastapi import FastAPI
from flexit import queries
app = FastAPI()


@app.get("/")
async def root():
    queries.shows_of_actor('Kyle MacLachlan')
    return {"message": queries.shows_of_actor('Kevin Bacon')}


@app.get("/health_check")
async def health_check():
    return {"message": "Looks like the app is healthy"}