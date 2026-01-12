from typing import List
from fastapi import FastAPI
from pydantic import BaseModel
import json

app = FastAPI()

class Person(BaseModel):
    id: int
    name: str
    age: int

DB: List[Person] = [
    Person(id=1, name="yasmin", age=27),
    Person(id=2, name="aline", age=24)
]

@app.get("/api01")
def read_api01():
    return DB

@app.get("/api02")
def read_api02():
    with open("people.json", "r") as file:
        return json.load(file)
