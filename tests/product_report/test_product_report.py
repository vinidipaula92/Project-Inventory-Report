from inventory_report.inventory.product import Product


def test_relatorio_produto():
    product = Product(
        1,
        "CADEIRA",
        "Forces of Nature",
        "2022-04-04",
        "2023-02-09",
        "FR48",
        "conservar em local fresco",
    )
    assert product.__repr__() == (
        "O produto CADEIRA fabricado em 2022-04-04 por Forces of Nature"
        " com validade até 2023-02-09 precisa ser armazenado"
        " conservar em local fresco."
    )
