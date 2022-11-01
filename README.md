# Seja bem vindo ao projeto Inventory Reports

<details>
  <summary><strong>👨‍💻 O que foi desenvolvido</strong></summary><br />

  Neste projeto pude fazer algo parecido, mas utilizando a Programação Orientada a Objetos! Implementando **gerador de relatórios** que recebe como entrada arquivos com dados de um estoque e gera, como saída, um relatório acerca destes dados.

  Esses dados de estoque poderão ser obtidos de diversas fontes:

  - Através da importação de um arquivo `CSV`;

  - Através da importação de um arquivo `JSON`;

  - Através da importação de um arquivo `XML`.

  Além disso, o relatório final possuirá duas versões: **simples** e **completa**.

  <strong>🚵 Habilidades trabalhadas:</strong>
 

  <ul>
    <li>Aplicar conceitos de Orientação a Objetos em Python;</li>
    <li>Aplicar padrões de projeto;</li>
    <li>Leitura e escrita de arquivos (XML, CSV, JSON).</li>
  </ul>
</details>


<details>
  <summary><strong>🎛 Linter</strong></summary><br />

  Para garantir a qualidade do código, foi utilizadp neste projeto o linter `Flake8`.
  Assim o código estará alinhado com as boas práticas de desenvolvimento, sendo mais legível
  e de fácil manutenção! 
</details>

<details>
  <summary><strong>🏕️ Ambiente Virtual</strong></summary><br />
  O Python oferece um recurso chamado de ambiente virtual, onde permite sua máquina rodar sem conflitos, diferentes tipos de projetos com diferentes versões de bibliotecas.

  1. **criar o ambiente virtual**

  ```bash
  $ python3 -m venv .venv
  ```

  2. **ativar o ambiente virtual**

  ```bash
  $ source .venv/bin/activate
  ```

  3. **instalar as dependências no ambiente virtual**

  ```bash
  $ python3 -m pip install -r dev-requirements.txt
  ```

  Com o seu ambiente virtual ativo, as dependências serão instaladas neste ambiente.
  Quando precisar desativar o ambiente virtual, execute o comando "deactivate". Lembre-se de ativar novamente quando voltar a trabalhar no projeto.

  O arquivo `dev-requirements.txt` contém todas as dependências que serão utilizadas no projeto, ele está agindo como se fosse um `package.json` de um projeto `Node.js`.
</details>

<details>
  <summary><strong>🛠 Testes</strong></summary><br />

  Para executar os testes certifique-se de que você está com o ambiente virtual ativado

  <strong>Executar os testes</strong>

  ```bash
  $ python3 -m pytest
  ```

  O arquivo `pyproject.toml` já configura corretamente o pytest. Entretanto, caso você tenha problemas com isso e queira explicitamente uma saída completa, o comando é:

  ```bash
  python3 -m pytest -s -vv
  ```

  Caso precise executar apenas um arquivo de testes basta executar o comando:

  ```bash
  python3 -m pytest tests/nomedoarquivo.py
  ```

  Caso precise executar apenas uma função de testes basta executar o comando:

  ```bash
  python3 -m pytest -k nome_da_func_de_tests
  ```

  Se desejar que os testes parem de ser executados quando acontecer o primeiro erro, use o parâmetro `-x`

  ```bash
  python3 -m pytest -x tests/test_simple_report.py
  ```

  Caso queria executar um teste especifico de um arquivo basta executar o comando:

  ```bash
  python3 -m pytest -x tests/nomedoarquivo.py::test_nome_do_teste
  ```

  Se quiser saber mais sobre a instalação de dependências com `pip`, veja esse [artigo](https://medium.com/python-pandemonium/better-python-dependency-and-package-management-b5d8ea29dff1).

</details>

<details>
  <summary><strong>🐳Docker</strong></summary>
  Caso queria executar os seus testes de projeto via `Docker-compose`, substituindo o ambiente virtual, execute o comando:

  ```bash
  docker-compose run --rm inventory pytest
  ```
</details>

<details>
  <summary><strong>🗃️ Arquivos com os dados de entrada</strong></summary><br />
  Três formatos de importação estão disponíveis no diretório <code>data</code> dentro do diretório <code>inventory_report</code>. Confira o exemplo de formato eles:
  
  <strong>Arquivos CSV</strong>
  Os arquivos **CSV** são separados por vírgula, como no exemplo abaixo:

```CSV
id,nome_do_produto,nome_da_empresa,data_de_fabricacao,data_de_validade,numero_de_serie,instrucoes_de_armazenamento
1,cadeira,Target Corporation,2021-02-18,2025-09-17,CR25,empilhadas
2,mesa,"Galena Madeira, Inc.",2022-12-06,2026-12-25,FR29,desmontadas
3,abajur,Keen Iluminação,2019-12-22,2025-11-07,CZ09,em caixas
```

<strong>Arquivos JSON</strong>
Os arquivos JSON seguem o seguinte modelo:

```json
[
  {
    "id":1,
    "nome_do_produto":"Borracha",
    "nome_da_empresa":"Papelaria Solar",
    "data_de_fabricacao":"2021-07-04",
    "data_de_validade":"2029-02-09",
    "numero_de_serie":"FR48",
    "instrucoes_de_armazenamento":"Ao abrigo de luz solar"
  }
]
```

<strong>Arquivos XML</strong>
Os arquivos **XML** seguem o seguinte modelo:

```xml
<?xml version='1.0' encoding='UTF-8'?>
<dataset>
  <record>
    <id>1</id>
    <nome_do_produto>Microfone</nome_do_produto>
    <nome_da_empresa>Tecno Uau LTDA</nome_da_empresa>
    <data_de_fabricacao>2021-10-27</data_de_fabricacao>
    <data_de_validade>2032-08-31</data_de_validade>
    <numero_de_serie>MT08</numero_de_serie>
    <instrucoes_de_armazenamento>Longe de fonte de calor</instrucoes_de_armazenamento>
  </record>
</dataset>
```
</details>

<h1 style="center">Obrigado pela visita ao meu repositório</h1>

## 🔗 Links

[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://vinidipaula.vercel.app/)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/vinicius-depaula/)

