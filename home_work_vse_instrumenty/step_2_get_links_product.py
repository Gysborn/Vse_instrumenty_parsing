from home_work_vse_instrumenty.lib import *
from bs4 import BeautifulSoup
import lxml


# Цель: Получить текстовый файл ссылок на товары, всего 2000

def main():
    for i in range(1, 101):
        with open(f"data/page_{i}.html", encoding='utf-8') as file:
            src = file.read()  # Считываем html страничку в переменную

        soup = BeautifulSoup(src, 'lxml')
        result = soup.find_all("div", class_="E-Geio")  # Собираем все ссылки со страницы 20шт.
        if i == 1:
            result += soup.find_all("div", class_="Z6EojR Z9UMXC")
        collect = []
        for link in result:
            href = "https://rostov.vseinstrumenti.ru/" + link.find("a").get("href")  # 1 ссылка 1 товар
            collect.append(href)
        try:
            with open("data/product_links", "a", encoding="utf-8") as f:  # Сохраняем в текстовый файл
                for line in collect:
                    f.write(f"{line}\n")
        except Exception as error:
            print(error)


if __name__ == '__main__':
    main()
