import json
import time

import requests
from bs4 import BeautifulSoup

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}

# persons_url_list = []
# urls = f"https://www.bundestag.de/ajax/filterlist/en/members/863330-863330?limit=12&noFilterSet=true&offset=720"
# req = requests.get(urls)
# soup = BeautifulSoup(req.content, "lxml")
# persons = soup.find_all("div", class_="bt-slide-content")
#
# for i in persons:
#
#     print(i.find("a").get("href"))


# for i in range(0, 747, 12):
#     urls = f"https://www.bundestag.de/ajax/filterlist/en/members/863330-863330?limit=12&noFilterSet=true&offset={i}"
#     req = requests.get(urls)
#
#     result = req.content
#     soup = BeautifulSoup(result, "lxml")
#     persons = soup.find_all(class_="bt-slide-content")
#
#     for person in persons:
#         person_page_url = person.find("a").get("href")
#         persons_url_list.append(person_page_url)
#
# with open("data/person_url_list.txt", "a", encoding="utf-8") as file:
#     for line in persons_url_list:
#         file.write(f"{line}\n")
#####################################

data_dict = []
count = 0
with open("data/person_url_list.txt") as file:
    lines = [line.strip() for line in file.readlines()]
    for line in lines:
        req = requests.get(line, headers=headers)
        result = req.content
        soup = BeautifulSoup(result, "lxml")
        try:
            person = soup.find(class_="bt-biografie-name").find("h3").text
        except Exception as e:
            with open("data/data_person.json", "w") as f:
                json.dump(data_dict, f, indent=4)



        person_name_company = person.strip().split(',')
        person_name = person_name_company[0]
        person_company = person_name_company[1].strip()

        social_networks = soup.find_all(class_="bt-link-extern")
        social_networks_urls = []
        for item in social_networks:
            social_networks_urls.append(item.get("href"))

        data = {
            "person_name": person_name,
            "person_company": person_company,
            "social_networks_urls": social_networks_urls,
        }

        count -= 1
        print(f"#{count}: {line} is done")
        data_dict.append(data)
        time.sleep(1)

with open("data/data_person.json", "w") as f:
    json.dump(data_dict, f, indent=4)
