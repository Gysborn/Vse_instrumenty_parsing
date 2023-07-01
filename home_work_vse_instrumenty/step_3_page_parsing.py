from home_work_vse_instrumenty.lib import *
import json


def main():
    with open('data/vi_links.txt') as file:# Открываем файл со ссылками
        links = iter(file.readlines())# Передаем в ленивый итератор что бы не загружать память
    try:
        browser = web_driver()# Получаем объект браузера
        for _ in range(40):
            url = next(links)# Запускаем цикл, по кол. ссылок и достаем по одной
            browser.get(url)# Передаем в браузер
            with open(f"data/page{_}.html", "w", encoding="utf-8") as f:# Записываем в файл html
                f.write(browser.page_source)# По другому не знаю как бороться с кодировкой

            with open(f"data/page{_}.html", encoding="utf-8") as f:# Открываем этот же файл
                src = f.read()# В переменную
            print("parsing...")
            soup = BeautifulSoup(src, 'lxml')# Инициализируем суп...
            pars = Parsing(soup)# Наш класс для парсинга
            prod = Product(
                title=pars.parsing_title(),# И пидантик дата класс
                image=pars.parsing_image(),
                price=pars.parsing_price(),
                description=pars.parsing_descr(),
                tech_specifications={'Teхнические характеристики': pars.parsing_tech()},
                warranty=pars.parsing_warranty(),
                article={'Код товара': pars.parsing_article()},
                rating=pars.parsing_rating()
            )
            json_data = prod.json(ensure_ascii=False)# Сериализуем данные из пидантика в json
            with open("data/data_tool.json", "a") as fjson:# И записываем в файл
                json.dump(json_data, fjson, indent=4)

            del_file(f"data/page{_}.html")# Удаляем файл html(подумал что 2000 файлов это туматч)
            print(f"{_} json is ready {2000 - _} left")
    except Exception as e:
        print(e)
    finally:
        browser.close()
        browser.quit()# Завершаем работу браузера


if __name__ == '__main__':
    main()
