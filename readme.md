# ScrapyIphone - Scraping de Produtos do Kabum

Este projeto realiza o scraping de informações de produtos do site Kabum utilizando `Selenium` e `Scrapy`. O script coleta dados dos produtos, incluindo nome, preço e link, e salva esses dados em um arquivo Excel. Ele também navega automaticamente pelas páginas de resultados até que não haja mais páginas para processar. O programa executa em um loop infinito, rodando a cada 30 minutos, apenas adicionando ao arquivo Excel caso exista algo diferente

## Requisitos

- Python 3.7 ou superior
- Google Chrome
- ChromeDriver compatível com a versão do seu Chrome

### Bibliotecas Python

- `selenium`
- `scrapy`
- `pandas`
- `openpyxl`

Você pode instalar todas as dependências utilizando o seguinte comando:

```bash
pip install selenium scrapy pandas openpyxl
```

## Como rodar o projeto
Basta iniciar o arquivo principal, sendo assim:
```bash
py scraper/weatherscraper.py