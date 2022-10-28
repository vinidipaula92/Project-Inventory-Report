from datetime import datetime


class SimpleReport:
    @classmethod
    def generate(cls, inventory):
        oldest_date = cls.get_oldest_date(inventory)
        nearest_expiration_date = cls.get_nearest_expiration_date(inventory)
        company_more_products = cls.get_company_more_products(inventory)
        return (
            f"Data de fabricação mais antiga: {oldest_date}\n"
            f"Data de validade mais próxima: {nearest_expiration_date}\n"
            f"Empresa com mais produtos: {company_more_products}"
        )

    @classmethod
    def get_oldest_date(cls, inventory):
        oldest_date = datetime.now().strftime("%Y-%m-%d")
        for product in inventory:
            if product["data_de_fabricacao"] < oldest_date:
                oldest_date = product["data_de_fabricacao"]
        return oldest_date

    @classmethod
    def get_nearest_expiration_date(cls, inventory):
        nearest_expiration_date = datetime.now().strftime("%Y-%m-%d")
        return min(
            [
                product["data_de_validade"]
                for product in inventory
                if product["data_de_validade"] > nearest_expiration_date
            ]
        )

    @classmethod
    def get_company_more_products(cls, inventory):
        companies = {}
        for product in inventory:
            if product["nome_da_empresa"] in companies:
                companies[product["nome_da_empresa"]] += 1
            else:
                companies[product["nome_da_empresa"]] = 1
        return max(companies, key=companies.get)
