from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(
    title="Item Management API",
    description="A simple API for managing items",
    version="1.0.0"
)

# Pydantic models for request/response validation
class ItemBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: float

class Item(ItemBase):
    id: int

    class Config:
        from_attributes = True

# In-memory database (replace with real database)
items_db: dict[int, dict] = {}
next_id = 1

# GET all items
@app.get("/items", response_model=List[Item])
async def get_items(skip: int = 0, limit: int = 10):
    """Retrieve all items with pagination."""
    items_list = list(items_db.values())
    return items_list[skip:skip + limit]

# GET specific item
@app.get("/items/{item_id}", response_model=Item)
async def get_item(item_id: int):
    """Retrieve a specific item by ID."""
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    return items_db[item_id]

# POST create new item
@app.post("/items", response_model=Item, status_code=201)
async def create_item(item: ItemBase):
    """Create a new item."""
    global next_id
    new_item = {**item.dict(), "id": next_id}
    items_db[next_id] = new_item
    next_id += 1
    return new_item

# PUT update item
@app.put("/items/{item_id}", response_model=Item)
async def update_item(item_id: int, item: ItemBase):
    """Update an existing item."""
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    updated_item = {**item.dict(), "id": item_id}
    items_db[item_id] = updated_item
    return updated_item

# DELETE item
@app.delete("/items/{item_id}", status_code=204)
async def delete_item(item_id: int):
    """Delete an item."""
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    del items_db[item_id]
    return None

# Root endpoint
@app.get("/")
async def root():
    """Welcome message."""
    return {"message": "Welcome to Item Management API"}
