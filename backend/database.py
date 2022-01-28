from model import TodoItem
from typing import List

import motor.motor_asyncio

client = motor.motor_asyncio.AsyncIOMotorClient("mongodb://localhost:27017")

database = client.TodoList

collection = database.todo_item


async def fetch_one_todo(title) -> TodoItem:
    document = await collection.find_one({"title": title})
    return TodoItem(**document)


async def fetch_all_todos() -> List[TodoItem]:
    todos = []
    cursor = collection.find({})
    async for document in cursor:
        todos.append(TodoItem(**document))
    return todos


async def create_todo(todo: TodoItem) -> TodoItem:
    await collection.insert_one(todo.dict())
    return todo


async def update_todo(title, desc):
    await collection.update_one({"title": title}, {"$set": {"description": desc}})
    document = await collection.find_one({"title": title})
    return TodoItem(**document)


async def remove_todo(title: str) -> int:
    retVal = await collection.delete_one({"title": title})
    return retVal.deleted_count
