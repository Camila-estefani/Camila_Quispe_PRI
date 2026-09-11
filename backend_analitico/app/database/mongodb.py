import os

from pymongo import MongoClient


class MemoryCollection:
    def __init__(self, items=None):
        self._items = list(items or [])

    def find(self):
        return list(self._items)


class MemoryDatabase:
    def __init__(self):
        self._collections = {"sales": MemoryCollection()}

    def __getitem__(self, key):
        if key not in self._collections:
            self._collections[key] = MemoryCollection()
        return self._collections[key]


def get_database():
    mongo_uri = os.getenv("MONGO_URI")
    db_name = os.getenv("MONGO_DB_NAME", "asiamarket")

    if mongo_uri:
        try:
            client = MongoClient(mongo_uri, serverSelectionTimeoutMS=2000)
            return client[db_name]
        except Exception:
            pass

    return MemoryDatabase()
