import time
from home_work_vse_instrumenty.lib import *

# Цель: Получить 100 html файлов содержащих по 20 товаров

"""
Код ниже что бы получить куки
"""

browser = web_driver()  # Получаем браузер
browser.get('https://vseinstrumenti.ru/')
get_cookies(browser, "vi_rostov_cookies")
time.sleep(30)

har = browser.get_log('browser')
res = har[0]['message']
print(res)


def main_one():
    url = 'https://rostov.vseinstrumenti.ru/category/bolgarki-ushm-123/'
    url2 = 'https://rostov.vseinstrumenti.ru/category/bolgarki-ushm-123/page'
    cookie_path = "vi_rostov_cookies"
    try:
        browser = web_driver()  # Получаем браузер
        for i in range(1, 2):
            if i != 1:  # На первой итерации нам нужен именно url
                url = url2 + f"{i}/"  # На остальных url2
            browser.get(url)  # Открываем ссылку
            load_cookies(browser, cookie_path)
            browser.refresh()
            time.sleep(5)
            har = browser.get_log('browser')
            res = har[0]['message']
            print(res)
            # if '200' in res:
            #     raise Exception('ошибка')
            with open(f"data/page_{i}.html", "w", encoding="utf-8") as file:
                file.write(browser.page_source)  # Сохраняем страничку в файл методом page_source с расш. html
            print(f"{i}_page записана")
    except Exception as e:
        print(e)
    finally:
        browser.close()
        browser.quit()

# main_one()
