import csv
from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, file_path: str):
        if not file_path.endswith(".csv"):
            raise ValueError("Arquivo inválido")
        with open(file_path, "r") as file:
            return [row for row in csv.DictReader(file)]
