import time
import undetected_chromedriver
from home_work_vse_instrumenty.lib import *

# Цель: Получить 100 html файлов содержащих по 20 товаров

"""
Код ниже что бы получить куки
"""


# browser = web_driver()  # Получаем браузер

# driver.get('https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html')
# driver.get("https://www.vindecoderz.com/EN/check-lookup/ZDMMADBMXHB001652")
# driver.get("https://vseinstrumenti.ru/")

# time.sleep(30)
# get_cookies(browser, "vi_rostov_cookies")
# time.sleep(30)

# har = browser.get_log('browser')
# res = har[0]['message']
# print(res)


def main_one():
    url = 'https://rostov.vseinstrumenti.ru/category/bolgarki-ushm-123/'
    url2 = 'https://rostov.vseinstrumenti.ru/category/bolgarki-ushm-123/page'
    cookie_path = "vi_rostov_cookies"
    try:
        browser = undetected_chromedriver.Chrome()
        for i in range(1, 4):
            if i != 1:  # На первой итерации нам нужен именно url
                url = url2 + f"{i}/"  # На остальных url2
            browser.get(url)  # Открываем ссылку
            # load_cookies(browser, cookie_path)
            # browser.refresh()
            time.sleep(10)
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


main_one()
