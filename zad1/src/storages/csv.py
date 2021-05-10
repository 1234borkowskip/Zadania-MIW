import csv

from storages.base import BaseStorage


class CsvStorage(BaseStorage):
    EXTENSION = 'csv'

    @staticmethod
    def perform_save(file=None, data=None):
        writer = csv.writer(file)
        for row in data:
            writer.writerow(row)
