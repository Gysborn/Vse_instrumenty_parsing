import json
import time

import requests as requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def get_chromedriver(user_agent=None):# Получаем наш виртуальный браузер Chrome
    options = webdriver.ChromeOptions()# Создаем объект опций
    options.add_argument(f'--user-agent={user_agent}')# Добавляем в опции user-agent
   # options.add_argument('--proxy-server=192.109.91.109:8000')
    service = Service(executable_path="Lesson6_selenium/Chromedriver/chromedriver.exe")# Создаем сервис в который передаем путь до драйвера
    return webdriver.Chrome(service=service, options=options)# Возвращаем сконфигурированный объект браузера


url = "https://spb.vseinstrumenti.ru/category/shurupoverty-1774/"


def main():
    try: # Получаем наш браузер с user-agent ом
        browse = get_chromedriver(
            user_agent="Mozilla/5.0 (Macintosh; U; Intel Mac OS X 13_0_0; en-US; Valve Steam GameOverlay/1666144119; ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36")
        browse.get(url=url)# Передаем урл в браузер
        time.sleep(20)
        with open("instr_index.html", "w", encoding="utf-8") as file:
            file.write(browse.page_source)# Сохраняем страничку в файл методом page_source
    except Exception as e:
        print(e)
    finally:
        browse.close()# Закрываем
        browse.quit()# Выходим

    # with open("tury_index.html", encoding='utf-8') as file:
    #     src = file.read()# Считываем файл в переменную
    # # Далее вытягиваем данные
    # soup = BeautifulSoup(src, "lxml")
    # hotel_cards = soup.find_all("div", class_="reviews-travel__info")
    # hotel_url = [hotel.find("a").get("href") for hotel in hotel_cards]
    # print(hotel_url)


if __name__ == '__main__':
    main()
