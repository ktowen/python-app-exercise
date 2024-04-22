import requests

from src.Models.Todo import Todo
from src.Services.StorageService import StorageService


class ApiService:
    def __init__(self, storage: StorageService):
        self._storage = storage

    def run(self) -> None:
        todo_list = self.fetch()
        self.store(todo_list)

    def fetch(self) -> list[Todo]:
        response = requests.get("https://jsonplaceholder.typicode.com/todos/")
        response.raise_for_status()
        return [Todo(**todo) for todo in response.json()]

    def store(self, data: list[Todo]) -> None:
        self._storage.save(data)
