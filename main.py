from fastapi import FastAPI, HTTPException
from sqlmodel import Session, select
from database import create_db_and_tables, engine
from models import Item
from datetime import datetime
from typing import List, Optional

app = FastAPI(
    title="Inventory Management API",
    description="A simple CRUD API built with FastAPI + SQLModel",
    version="1.0.0"
)


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


@app.get("/")
def root():
    return {
        "message": "Welcome to Inventory Management API",
        "version": "1.0.0",
        "docs": "/docs",
        "endpoints": {
            "GET /items": "List all items",
            "POST /items": "Create a new item",
            "GET /items/{item_id}": "Get a specific item",
            "PUT /items/{item_id}": "Update an item",
            "DELETE /items/{item_id}": "Delete an item"
        }
    }



@app.post("/items", response_model=Item)
def create_item(item: Item):
    with Session(engine) as session:
        session.add(item)
        session.commit()
        session.refresh(item)
        return item



@app.get("/items", response_model=List[Item])
def list_items(limit: int = 50, offset: int = 0, q: Optional[str] = None):
    with Session(engine) as session:
        statement = select(Item)

        if q:
            statement = statement.where(Item.name.contains(q))

        statement = statement.offset(offset).limit(limit)
        items = session.exec(statement).all()
        return items



@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    with Session(engine) as session:
        item = session.get(Item, item_id)
        if not item:
            raise HTTPException(404, "Item not found")
        return item



@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, updated: Item):
    with Session(engine) as session:
        item = session.get(Item, item_id)
        if not item:
            raise HTTPException(404, "Item not found")

        item.name = updated.name
        item.sku = updated.sku
        item.qty = updated.qty
        item.price = updated.price
        item.updated_at = datetime.utcnow()

        session.add(item)
        session.commit()
        session.refresh(item)
        return item



@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    with Session(engine) as session:
        item = session.get(Item, item_id)
        if not item:
            raise HTTPException(404, "Item not found")

        session.delete(item)
        session.commit()
        return {"ok": True, "message": "Item deleted"}
