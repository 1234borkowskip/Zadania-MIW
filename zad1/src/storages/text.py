from storages.base import BaseStorage


class TextStorage(BaseStorage):
    EXTENSION = 'txt'

    @staticmethod
    def perform_save(file=None, data=None):
        for row in data:
            file.writelines(str(row) + '\n')