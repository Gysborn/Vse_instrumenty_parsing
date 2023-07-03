import undetected_chromedriver
from home_work_vse_instrumenty.lib import *
import json
import time


# Цель: распарсить страницы товара по ссылкам из product_links

def main():
    data_tools = []
    with open('data/product_links') as file:  # Открываем файл со ссылками
        links = iter(file.readlines())  # Передаем в ленивый итератор что бы не загружать память
    try:
        browser = undetected_chromedriver.Chrome()
        for _ in range(1):
            url = next(links)  # Запускаем цикл, по кол. ссылок и достаем по одной
            browser.get(url)  # Передаем в браузер
            time.sleep(5)
            with open(f"data/page{_}.html", "w", encoding="utf-8") as f:  # Записываем в файл html
                f.write(browser.page_source)  # По другому не знаю как бороться с кодировкой

            with open(f"data/page{_}.html", encoding="utf-8") as f:  # Открываем этот же файл
                src = f.read()  # В переменную

            print(f"parsing... {_+1}")
            soup = BeautifulSoup(src, 'lxml')  # Инициализируем суп...
            pars = Parsing(soup)  # Наш класс для парсинга
            prod = Product(
                title=pars.parsing_title(),  # И пидантик дата класс
                image=pars.parsing_image(),
                price=pars.parsing_price().replace('\xa0', ''),
                description=pars.parsing_descr(),
                tech_specifications=pars.parsing_tech(),
                warranty=pars.parsing_warranty(),
                article=pars.parsing_article(),
                rating=pars.parsing_rating()
            )
            dict_data = prod.dict()  # Сериализуем данные из пидантика в словарь
            data_tools.append(dict_data)

            del_file(f"data/page{_}.html")  # Удаляем файл html(подумал что 2000 файлов это туматч)
            print(f"{_ + 1} json is ready, {2000 - _ + 1} left")

        with open("data/data_tool.json", "w", encoding='utf-8') as fjson:  # И записываем в файл
            json.dump(data_tools, fjson, ensure_ascii=False, indent=4)

    except Exception as e:
        print(e)
    finally:
        browser.close()
        browser.quit()  # Завершаем работу браузера


if __name__ == '__main__':
    main()
