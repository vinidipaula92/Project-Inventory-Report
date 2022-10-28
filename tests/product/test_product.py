from inventory_report.inventory.product import Product


def test_cria_produto():
    produto = Product(
        1,
        "Coca-Cola",
        "Coca-Cola Company",
        "2021-01-01",
        "2021-12-31",
        "123456789",
        "em local fresco e seco",
    )
    assert produto.nome_da_empresa == "Coca-Cola Company"
    assert produto.nome_do_produto == "Coca-Cola"
    assert produto.data_de_fabricacao == "2021-01-01"
    assert produto.data_de_validade == "2021-12-31"
    assert produto.numero_de_serie == "123456789"
    assert produto.instrucoes_de_armazenamento == "em local fresco e seco"
