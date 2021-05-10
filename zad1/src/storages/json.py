import json

from storages.base import BaseStorage


class JsonStorage(BaseStorage):
    EXTENSION = 'json'

    @staticmethod
    def perform_save(file=None, data=None):
        json.dump(data, file)
