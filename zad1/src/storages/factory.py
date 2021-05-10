from storages.json import JsonStorage
from storages.text import TextStorage
from storages.csv import CsvStorage


class StorageFactory(object):

    @staticmethod
    def factory(extension):
        mapping = {
            'json': JsonStorage,
            'txt': TextStorage,
            'csv': CsvStorage,
        }
        return mapping.get(extension, TextStorage)
