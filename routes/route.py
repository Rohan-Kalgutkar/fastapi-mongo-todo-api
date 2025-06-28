from fastapi import APIRouter, HTTPException, Query
from models.todos import Todo
from config.database import collection_name
from schema.schemas import list_serial, individual_serial
from bson import ObjectId
from bson.errors import InvalidId

router = APIRouter()

# ✅ GET all todos
@router.get("/", tags=["Todos"])
async def get_todos(page: int = Query(1, ge=1), limit: int = Query(10, ge=1)):
    skip = (page - 1) * limit

    todos_cursor = collection_name.find().skip(skip).limit(limit)
    todos = list_serial(todos_cursor)

    total_todos = collection_name.count_documents({})
    total_pages = (total_todos + limit - 1) // limit

    return {
        "page": page,
        "limit": limit,
        "total_todos": total_todos,
        "total_pages": total_pages,
        "todos": todos
    }


# ✅ POST new todo with duplicate check
@router.post("/", tags=["Todos"])
async def create_todo(todo: Todo):
    existing = collection_name.find_one({
        "name": todo.name,
        "description": todo.description
    })

    if existing:
        raise HTTPException(
            status_code=400,
            detail="Todo with the same name and description already exists"
        )

    result = collection_name.insert_one(todo.model_dump())
    created = collection_name.find_one({"_id": result.inserted_id})
    return {
        "message": "Todo created",
        "todo": individual_serial(created)
    }


# ✅ PUT update todo by ID
@router.put("/{todo_id}", tags=["Todos"])
async def update_todo(todo_id: str, todo: Todo):
    try:
        obj_id = ObjectId(todo_id)
    except InvalidId:
        raise HTTPException(status_code=400, detail="Invalid ID format")

    updated = collection_name.find_one_and_update(
        {"_id": obj_id},
        {"$set": todo.model_dump()},
        return_document=True
    )

    if not updated:
        raise HTTPException(status_code=404, detail="Todo not found")

    return {
        "message": "Todo updated",
        "todo": individual_serial(updated)
    }


# ✅ DELETE todo by ID
@router.delete("/{todo_id}", tags=["Todos"])
async def delete_todo(todo_id: str):
    try:
        obj_id = ObjectId(todo_id)
    except InvalidId:
        raise HTTPException(status_code=400, detail="Invalid ID format")

    deleted = collection_name.find_one_and_delete({"_id": obj_id})

    if not deleted:
        raise HTTPException(status_code=404, detail="Todo not found")

    return {
        "message": "Todo deleted",
        "todo": individual_serial(deleted)
    }
