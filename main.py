from fastapi import FastAPI
import database

app = FastAPI()
db = database.Database()
db.addData()
db.getData()


@app.get("/getUsers")
async def read_item():
    return {"name": "name",
            "id_person": "id_person",
            "picture": "picture",
            }