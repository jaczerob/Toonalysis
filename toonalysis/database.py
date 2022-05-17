from pymongo.mongo_client import MongoClient
from pymongo.errors import DuplicateKeyError

from toonalysis import static
from toonalysis.types import Toon


class Toons:
    def __init__(self) -> None:
        self._client = MongoClient(port=27017)
        
        _db = self._client.get_database(static.MONGO_DATABASE)
        self._toons = _db.get_collection(static.MONGO_COLLECTION)

    def add_or_update(self, toon: Toon) -> None:
        document = toon.to_document()

        try:
            self._toons.insert_one(document)
        except DuplicateKeyError:
            self._toons.replace_one({"_id": toon.id}, document)

    def __enter__(self):
        return self

    def __exit__(self, *_):
        self._client.close()
