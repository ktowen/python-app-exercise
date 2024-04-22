import csv
from datetime import datetime
from pathlib import Path

from src.Models.Todo import Todo


class StorageService:
    def save(self, data: list[Todo]) -> None:
        raise NotImplementedError()


class FileStorageService(StorageService):
    def save(self, data: list[Todo]) -> None:
        for todo in data:
            self.save_file(todo)

    def save_file(self, todo: Todo) -> None:
        file_path = Path("storage") / self.get_file_name(todo)

        with open(file_path, "w") as csvfile:
            fieldnames = todo.keys()
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerow(todo)

    def get_file_name(self, todo: Todo) -> str:
        now = datetime.now()
        return f"{now.strftime("%y_%m_%d")}_{todo['id']}.csv"
