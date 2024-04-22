from src.Services.ApiService import ApiService
from src.Services.StorageService import FileStorageService


class App:
    def __init__(self):
        self._storage_service = FileStorageService()
        self._api_service = ApiService(storage=self._storage_service)

    def api_service(self) -> ApiService:
        return self._api_service
