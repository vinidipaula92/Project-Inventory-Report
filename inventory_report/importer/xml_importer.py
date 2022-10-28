import xmltodict
from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, file_path: str):
        if not file_path.endswith(".xml"):
            raise ValueError("Arquivo inválido")
        with open(file_path, "r") as file:
            return xmltodict.parse(file.read())["dataset"]["record"]
