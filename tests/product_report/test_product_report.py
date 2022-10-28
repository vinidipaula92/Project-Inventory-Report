from inventory_report.inventory.product import Product


def test_relatorio_produto():
    product = Product(
        1,
        "Café",
        "Nescafé",
        "2020-01-01",
        "2021-01-01",
        "123456789",
        "em local seco e fresco",
    )
    assert product.__repr__() == (
        "O produto Café fabricado em 2020-01-01 por Nescafé com validade"
        " até 2021-01-01 precisa ser armazenado em local seco e fresco."
    )
