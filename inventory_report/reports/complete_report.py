from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, inventory):
        simple_report = super().generate(inventory)
        companies = super().get_company_more_products(inventory)

        return (
            f"{simple_report}\n"
            f"Produtos estocados por empresa:\n"
            f"{companies}"
        )
