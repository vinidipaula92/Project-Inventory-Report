from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv
import json
import xmltodict


class Inventory:
    @classmethod
    def import_inventory(cls, file_path: str):
        with open(file_path, "r") as file:
            if file_path.endswith(".csv"):
                return [row for row in csv.DictReader(file)]
            if file_path.endswith(".json"):
                return json.load(file)
            if file_path.endswith(".xml"):
                return xmltodict.parse(file.read())["dataset"]["record"]
            else:
                raise ValueError("Arquivo inválido")

    @classmethod
    def import_data(cls, file_path: str, report_type: str):
        products = cls.import_inventory(file_path)
        if report_type == "simples":
            return SimpleReport.generate(products)
        elif report_type == "completo":
            return CompleteReport.generate(products)
        else:
            raise ValueError("Tipo de relatório inválido")
