from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from pydantic import BaseModel
from bs4 import BeautifulSoup
import itertools as it
import pickle

import os


class Product(BaseModel):
    title: str
    image: str
    article: dict = {}
    price: int
    description: str
    tech_specifications: dict = {}
    warranty: str
    rating: float


user_agent = "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 YaBrowser/23.5.3.904 Yowser/2.5 Safari/537.36"


def web_driver():
    opt = webdriver.ChromeOptions()
    opt.add_argument("--disable-blink-features=AutomationControlled")
    opt.add_argument('Access-Control-Allow-Origin=https://www.vseinstrumenti.ru')
    opt.add_argument(user_agent)

    return webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), options=opt
    )


class Parsing:
    def __init__(self, soup_obj: BeautifulSoup):
        self.soup = soup_obj
        # Создаем лист из названий характеристик что бы затем объединить его в словарь
        # со значениями
        self.tech_title = [
            'Напряжение', 'Мощность', 'Диаметр диска', 'Посадочный диаметр', 'Число оборотов',
            'Min число оборотов', 'Электр. регулировка оборотов', 'Вид кнопки включения',
            'Кнопка фиксации пуска', 'Суперфланец', 'Быстрозажимная гайка SDS',
            'Защита от непреднамеренного пуска', 'Работа по бетону (камню)', 'Подача воды',
            'Регулировка положения кожуха без инструмента',
            'Поддержание постоянных оборотов под нагрузкой', 'Возможность подключения к пылесосу',
            'Наличие виброручки', 'Длина кабеля', 'Плавный пуск', ' Кожух для пылеудаления',
            'Упаковка', 'Вес нетто', 'Тип двигателя', 'Резьба шпинделя', 'Диск в комплекте',
            'Блокировка шпинделя при заклинивании диска', 'Количество положений рукоятки',
            'Защита от перегрева двигателя', 'Max глубина реза',
        ]

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
        res = self.soup.find_all('span', itemprop="value")
        list_value = [v.text.strip() if v else None for v in res]
        obj = dict(it.zip_longest(self.tech_title, list_value))
        return obj

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
