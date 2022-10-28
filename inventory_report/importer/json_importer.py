import json
from inventory_report.importer.importer import Importer


class JsonImporter(Importer):
    @classmethod
    def import_data(cls, file_path: str):
        if not file_path.endswith(".json"):
            raise ValueError("Arquivo inválido")
        with open(file_path, "r") as file:
            return json.load(file)
