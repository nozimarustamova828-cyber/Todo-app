from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import json
import os

app = FastAPI()
DATA_FILE = "todos.json"

class TodoItem(BaseModel):
    title: str
    completed: bool = False

class TodoUpdate(BaseModel):
    completed: bool

def read_todos():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def write_todos(todos):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(todos, f, indent=4, ensure_ascii=False)

@app.get("/", response_class=HTMLResponse)
async def read_index():
    with open("index.html", "r", encoding="utf-8") as f:
        return f.read()

@app.get("/api/todos")
async def get_todos():
    return read_todos()

@app.post("/api/todos")
async def create_todo(todo: TodoItem):
    if not todo.title.strip():
        raise HTTPException(status_code=400, detail="Vazifa nomi bo'sh bo'lmasligi kerak")
    todos = read_todos()
    # ID bug fix: max ID + 1 instead of len + 1
    new_id = max((t["id"] for t in todos), default=0) + 1
    new_todo = {
        "id": new_id,
        "title": todo.title.strip(),
        "completed": todo.completed
    }
    todos.append(new_todo)
    write_todos(todos)
    return new_todo

@app.patch("/api/todos/{todo_id}")
async def update_todo(todo_id: int, update: TodoUpdate):
    todos = read_todos()
    for todo in todos:
        if todo["id"] == todo_id:
            todo["completed"] = update.completed
            write_todos(todos)
            return todo
    raise HTTPException(status_code=404, detail="Vazifa topilmadi")

@app.delete("/api/todos/{todo_id}")
async def delete_todo(todo_id: int):
    todos = read_todos()
    original_len = len(todos)
    todos = [t for t in todos if t["id"] != todo_id]
    if len(todos) == original_len:
        raise HTTPException(status_code=404, detail="Vazifa topilmadi")
    write_todos(todos)
    return {"message": "O'chirildi"}
