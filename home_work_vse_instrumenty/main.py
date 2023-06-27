import json
import time

import requests as requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

def get_chromedriver(user_agent=None):  # Получаем наш виртуальный браузер Chrome
    options = webdriver.ChromeOptions()  # Создаем объект опций
    options.add_argument(f'--user-agent={user_agent}')  # Добавляем в опции user-agent
    # options.add_argument('--proxy-server=192.109.91.109:8000')
    service = Service(
        executable_path="home_work_vse_instrumenty/chromedriver.exe")  # Создаем сервис в который передаем путь до драйвера
    return webdriver.Chrome(service=service, options=options)  # Возвращаем сконфигурированный объект браузера


url = "https://www.vseinstrumenti.ru/category/akkumulyatornye-bolgarki-ushm-11807/page2/"
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"


def main():
    try:  # Получаем наш браузер с user-agent ом
        browse = get_chromedriver(user_agent=user_agent)
        browse.get(url=url)  # Передаем урл в браузер
        time.sleep(100)
        # hrefs = browse.find_element(By.CLASS_NAME, "Z6EojR Z9UMXC")
        # print(hrefs)
        # with open("data/instr_index.html", "w", encoding="utf-8") as file:
        #     file.write(browse.page_source)  # Сохраняем страничку в файл методом page_source
        #
        # with open("data/instr_index.html", encoding="utf-8") as f:
        #     src = f.read()
        # print(src)
    except Exception as e:
        print(e)
    finally:
        browse.close()  # Закрываем
        browse.quit()  # Выходим


if __name__ == '__main__':
    main()
