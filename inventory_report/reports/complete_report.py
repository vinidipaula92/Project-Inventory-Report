from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, inventory):
        simple_report = super().generate(inventory)
        companies = super().get_count_products_company(inventory)

        name_company = ""

        for name, quantity in companies.items():
            name_company += f"- {name}: {quantity}\n"

        return (
            f"{simple_report}\n"
            f"Produtos estocados por empresa:\n"
            f"{name_company}"
        )
