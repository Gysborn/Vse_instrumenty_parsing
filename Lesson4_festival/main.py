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

with open("data/fest_url_list.txt") as file:
    src = file.read()
stc = src.split("\n")
for url in stc[0:1]:
    req = requests.get(url, headers)
    print(req.text)
    json_data = json.loads(req.text)
    print(json_data)

    try:
        soup = BeautifulSoup(req.text, "lxml")
        fest_name = soup.find("h1", class_="MuiTypography-root").text.strip()
        fest = soup.find_all(class_="MuiGrid-root MuiGrid-item MuiGrid-grid-xs-11 css-twt0ol")
        print(fest)

        # fest_date = fest_date[0].text + fest_date[1].text
    except Exception as e:
        print("Шляпа")
        print(e)
    continue
