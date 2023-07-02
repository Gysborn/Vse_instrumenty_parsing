import json
import time

import requests as requests
from bs4 import BeautifulSoup
from pydantic import BaseModel

"""
Собираем данные о всех фестивалях с сайта https://www.skiddle.com
Часть первая в ветке master
"""
# создаем загловок чтобы нас не забанили
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}

fest_dict = []
with open("data/fest_url_list.txt") as file:
    src = file.read()
stc = src.split("\n")
for url in stc[0:1]:
    req = requests.get(url, headers)
    result = req.text
    try:
        soup = BeautifulSoup(result, "lxml")
        tmp = soup.find("data-testid", string="LocationOnIcon")
        print(tmp)
        fest_data_all = soup.find("div", class_="MuiGrid-root MuiGrid-item MuiGrid-grid-xs-11 css-twt0ol")
        fest_name = soup.find("h1", class_="MuiTypography-root").text.strip()
        fest_data = fest_data_all[0].find_all("span")
        fest_date = fest_data[0].target + '\n' + fest_data[1].target
        fest_title_about = soup.find("h2", class_="MuiTypography-root MuiTypography-h2 css-1w169lz").text
        fest_about_all = soup.find_all("div", class_="MuiBox-root css-0")
        fest_about = fest_about_all[-1].next_element.next_element.text
        fest_location = fest_data_all[1].find("span").text
        fest_tiket = fest_data_all[2].find("span").text
        data = {
            "fest_name": fest_name,
            "fest_location": fest_location,
            fest_title_about: fest_about,
            "fest_tiket": fest_tiket,
        }
        fest_dict.append(data)
    except Exception as e:
        print("Шляпа")
        print(e)
    finally:
        print("ok")
print("jl")

  
