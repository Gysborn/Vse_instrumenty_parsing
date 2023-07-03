from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from pydantic import BaseModel
from bs4 import BeautifulSoup
import pickle

import os


class Product(BaseModel):
    title: str
    image: str
    article: str
    price: str
    description: str
    tech_specifications: dict
    warranty: str
    rating: str


user_agent = "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 YaBrowser/23.5.3.904 Yowser/2.5 Safari/537.36"


def web_driver():
    opt = webdriver.ChromeOptions()
    opt.add_argument("--disable-blink-features=AutomationControlled")
    opt.add_argument('Access-Control-Allow-Origin=https://www.2ip.ru')
    opt.add_argument('--proxy-server=38.154.88.110:8000')
    opt.add_argument(user_agent)

    return webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), options=opt
    )


class Parsing:
    def __init__(self, soup_obj: BeautifulSoup):
        self.soup = soup_obj

    def parsing_title(self) -> str:  # Метод получения названия товара
        res = self.soup.find('div', class_='pKTE7p')
        return res.find('h1').text.strip()

    def parsing_image(self) -> str:  # Метод получения ссылки на картинку
        res = self.soup.find('div', class_='_3MbT74')
        return res.find('img').get('src')

    def parsing_price(self) -> str:  # Метод получения цены
        res = self.soup.find('div', class_='df5X3i')
        return res.find('p').text.strip()

    def parsing_descr(self) -> str:  # Метод получения описания
        res = self.soup.find('div', itemprop="description")
        return res.find('p').text.strip()

    def parsing_tech(self) -> dict:  # Метод получения характеристик в словаре
        divs = self.soup.find_all('div', class_='mbBW2z')
        dict_value = {"Teхнические характеристики": {}}
        for div in divs:
            key = div.find('span').text.strip()
            value = div.find_next_sibling().text.strip()
            dict_value["Teхнические характеристики"].update({key: value})
        return dict_value

    def parsing_warranty(self) -> str:  # Метод получения гарантии
        res = self.soup.find('div', class_="EJUM2Y")
        return res.find('p').text.strip()

    def parsing_article(self) -> str:  # Метод получения кода товара
        res = self.soup.find('div', class_="kZIDtu")
        return res.find('span').text.strip()

    def parsing_rating(self) -> str:  # Метод получения рейтинга
        res = self.soup.find('div', class_="hReTi1")
        return res.find('p').text.strip()


def del_file(path_file):
    if os.path.isfile(path_file):
        os.remove(path_file)
        print('File deleted!')
    else:
        print('File doesnt exists!')


def get_cookies(bro: webdriver, path_f):
    pickle.dump(bro.get_cookies(), open(path_f, 'wb'))


def load_cookies(bro: webdriver, path_f):
    try:
        cookies = pickle.load(open(path_f, "rb"))
        for cookie in cookies:
            bro.add_cookie(cookie)
        bro.refresh()
    except Exception as e:
        print(e)
