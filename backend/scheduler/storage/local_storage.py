from abc import abstractmethod


class StorageInterface:
    @abstractmethod
    def put(self, key, data) -> None: pass

    @abstractmethod
    def get(self, key) -> dict: pass


class LocalStorage(StorageInterface):
    _instance = None
    _storage = {}

    def __new__(cls, *args, **kwargs):
        if not isinstance(cls._instance, cls):
            cls._instance = object.__new__(cls)
        return cls._instance

    def put(self, key, data) -> None:
        self._storage[key] = data

    def get(self, key) -> dict:
        return self._storage[key]

    def get_all(self):
        print(self._storage)
