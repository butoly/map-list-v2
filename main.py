from fastapi import FastAPI
import database

app = FastAPI()
db = database.Database()


@app.get("/getUsers")
async def getUsers():
    response = db.getUsers()
    return {'responce': response}


@app.get("/getPlaces")
async def getPlaces():
    response = db.getPlaces()
    return {'responce': response}