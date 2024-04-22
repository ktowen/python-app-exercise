from typing import TypedDict


class Todo(TypedDict):
    userId: int
    id: int
    title: str
    completed: bool
