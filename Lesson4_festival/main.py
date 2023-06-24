import json
import time

import requests
from bs4 import BeautifulSoup

"""
Собираем данные о всех фестивалях с сайта https://www.skiddle.com
Часть первая в ветке master
"""
# создаем загловок чтобы нас не забанили
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}
fest_url_list = []# Лист для ссылок на фестивали из которых будем формировать карточки
for i in range(0, 378, 24):# Запускаем цикл по страницам 24 фестиваля на страницу, всего 378
    url = f"https://www.skiddle.com/festivals/search/?ajaxing=1&sort=0&fest_name=&from_date=24%20Jun%202023&to_date=&maxprice=500&o={i}&bannertitle=July"

    req = requests.get(url, headers)# Получаем страничку из 24 фестов
    json_data = json.loads(req.text)# Полученный ресурс в json
    response_html = json_data["html"]# Транслируем его в словарь и извлекаем html
    soup = BeautifulSoup(response_html, "lxml")# Скармливаем супу
    fest_data = soup.find_all("div", class_="card flex-height lvl-1 brt-5px bg-white relative has-details")# Достаем
    for fest in fest_data:# Интересующий нас клас
        fest_url = "https://www.skiddle.com/" + fest.find("a").get("href")# А из него берем ссылку
        fest_url_list.append(fest_url)#Сохраняем в наш лист ссылок
try:
    with open("data/fest_url_list_1.txt", "a", encoding="utf-8") as file:#Скидываем в файл
        for line in fest_url_list:
            file.write(f"{line}\n")
except Exception as e:
    print(e)

# with open("data/fest_url_list.txt") as file:
#     src = file.read()
# stc = src.split("\n")
# for url in stc[0:1]:
#     req = requests.get(url, headers)
#     print(req.text)
#     json_data = json.loads(req.text)
#     print(json_data)
#
#     try:
#         soup = BeautifulSoup(req.text, "lxml")
#         fest_name = soup.find("h1", class_="MuiTypography-root").text.strip()
#         fest = soup.find_all(class_="MuiGrid-root MuiGrid-item MuiGrid-grid-xs-11 css-twt0ol")
#         print(fest)
#
#         # fest_date = fest_date[0].text + fest_date[1].text
#     except Exception as e:
#         print("Шляпа")
#         print(e)
#     continue
