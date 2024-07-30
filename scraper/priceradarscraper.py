from selenium.webdriver.common.by import By
from scrapy.selector import Selector
from time import sleep
import pandas as pd
from datetime import datetime
from utils.webdriver.init import init
import os

# Salvar os valores dos produtos
def save_product_values(response):
    sleep(5)
    now = datetime.now()
    formatted_now = now.strftime('%d/%m/%Y %H:%M:%S')

    products = []
    contagem = 0
    for product in response.xpath('//main[@class="sc-ccc9eb50-13 cWkplc"]/article'):
        contagem += 1
        print(f'contagem: {contagem}')
        price_string = product.xpath(".//span[@class='sc-b1f5eb03-2 iaiQNF priceCard']/text()").get()
        cleaned_string = price_string.replace("R$", "").replace('&nbsp;', ' ').strip()
        
        link_complement = product.xpath(".//a[@class='sc-9d1f1537-10 kueyFw productLink']/@href").get()
        link = f'https://www.kabum.com.br{link_complement}'
        item = {
            'Product Name': product.xpath(".//span[@class='sc-d79c9c3f-0 nlmfp sc-9d1f1537-16 fQnige nameCard']/text()").get(),
            'Value': cleaned_string,
            'link': link,
            'date': formatted_now,
        }
        print(item)
        products.append(item)
    return products

# Verifica se existe e clicar no botão "next"
def click_next_button(driver):
    try:
        next_button = driver.find_element(By.XPATH, '//a[@class="nextLink" and @aria-disabled="false"]')
        if next_button:
            driver.execute_script("arguments[0].click();", next_button)
            sleep(5)
            return True
    except:
        return False

# Classe principal do scraper
class ScrapyIphone:
    def __init__(self):
        self.driver, self.wait = init()
        self.driver.maximize_window()
    
    def start(self):
        url = 'https://www.kabum.com.br/busca/pelicula-para-iphone-15?page_number=1&page_size=20&facet_filters=&sort=most_searched&variant=catalog'
        self.driver.get(url)
        sleep(5)  
        all_products = []
        while True:
            response_webdriver = Selector(text=self.driver.page_source)
            products = save_product_values(response_webdriver)
            all_products.extend(products)
            
            if click_next_button(self.driver) == False:
                self.driver.close()
                return all_products

    def read_existing_data(self, file_name='products.xlsx'):
        if os.path.exists(file_name):
            return pd.read_excel(file_name)
        else:
            return pd.DataFrame(columns=['Product Name', 'Value', 'link', 'date'])

    def save_to_excel(self, products, file_name='products.xlsx'):
        existing_data = self.read_existing_data(file_name)
        new_data = pd.DataFrame(products)

        # Verifica se o produto já não existe na tabela
        combined_data = pd.concat([existing_data, new_data], ignore_index=True)
        combined_data.drop_duplicates(subset=['link', 'Value'], keep='first', inplace=True)
        
        combined_data.to_excel(file_name, index=False)
        print(f"Produtos salvos no arquivo {file_name}")

# Executa a função
if __name__ == "__main__":
    scraper = ScrapyIphone()
    while True:
        product_data = scraper.start()
        scraper.save_to_excel(product_data)
        sleep(1800)
