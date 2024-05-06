from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel
import os

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}


@app.post("/items/")
def create_item(item: Item):
    item_id = "item_" + str(hash(item.name))  # 簡易的なID生成
    item_path = f"./item/{item_id}.txt"
    with open(item_path, "w") as file:
        file.write(f"Name: {item.name}\nPrice: {item.price}\nOffer: {item.is_offer}")
    return {"message": "Item saved", "item_id": item_id}