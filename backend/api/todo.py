from fastapi import APIRouter, HTTPException
from database import (
    fetch_one_todo,
    fetch_all_todos,
    create_todo,
    update_todo,
    remove_todo,
)
import pymongo

router = APIRouter()

from model import TodoItem
from typing import List


@router.get("/", response_model=List[TodoItem])
async def get_todo():
    """This app shows all todo inserted to this app

    Returns:
        int: Some number. 1
    """
    return await fetch_all_todos()


@router.get("/{title}", response_model=TodoItem)
async def get_todo_by_title(title: str):
    """Shows a single todo

    Args:
        title (int): Todo title

    Returns:
        int: TodoData
    """
    response = await fetch_one_todo(title)
    if response:
        return response
    raise HTTPException(404, f"Todo Item not found with title '{title}'")


@router.post("/", response_model=TodoItem, operation_id="some_specific_id_you_define")
async def post_todo(item: TodoItem):
    """Creates a new Todo Item

    Args:
        todo ([type]): Todo item

    Returns:
        int: TodoData
    """
    item = TodoItem(title=item.title, description=item.description)
    try:
        response = await create_todo(item)
    except pymongo.errors.DuplicateKeyError:  # type: ignore
        raise HTTPException(404, f"Todo Item found with title '{item.title}'")

    if response:
        return response
    raise HTTPException(400, f"Bad request")


@router.put("/")
async def put_todo(title: str, desc: str):
    """Updates a new Todo Item

    Args:
        int: Todo title
        todo ([type]): Todo item

    Returns:
        int: TodoData
    """
    response = await update_todo(title, desc)
    if response:
        return response
    raise HTTPException(400, "Bad request")


@router.delete("/{title}")
async def delete_todo(title: str):
    """Creates a new Todo Item

    Args:
        title (int): Todo title

    Returns:
        int: TodoData
    """
    response = await remove_todo(title)
    if response:
        return {"success": True}
    raise HTTPException(400, "Bad request")
