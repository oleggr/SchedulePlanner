from scheduler.storage.local_storage import LocalStorage


class StorageFactory:
    @staticmethod
    def get_storage():
        return LocalStorage()
