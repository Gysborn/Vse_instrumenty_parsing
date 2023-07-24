import time
import undetected_chromedriver
from selenium.webdriver.common.by import By

from home_work_vse_instrumenty.lib import *

# Цель: Получить 100 html файлов содержащих по 20 товаров

"""
Ниже, тестируем драйвер на скрытность
"""
path_cookie = 'vi_cookies'


def check_driver():
    try:
        driver = undetected_chromedriver.Chrome()
        driver.get("https://vseinstrumenti.ru/")
        time.sleep(2)
        get_cookies(driver, path_cookie)
        driver.refresh()
        time.sleep(10)
    except Exception as e:
        print(e)
    finally:
        driver.close()
        driver.quit()


""" Тесты прошли успешно"""


def main_one():
    url = 'https://rostov.vseinstrumenti.ru/category/bolgarki-ushm-123/'
    url2 = 'https://vseinstrumenti.ru/category/bolgarki-ushm-123/page'
    try:
        browser = undetected_chromedriver.Chrome()
        for i in range(91, 101):
            if i != 1:  # На первой итерации нам нужен именно url
                url = url2 + f"{i}/"  # На остальных url2
            browser.get(url)  # Открываем ссылку
            # time.sleep(1)
            # load_cookies(browser, path_cookie)
            time.sleep(5)
            res = browser.find_element(By.CLASS_NAME, "E-Geio")
            if res:
                print(res.text[:21])
            with open(f"data/page_{i}.html", "w", encoding="utf-8") as file:
                file.write(browser.page_source)  # Сохраняем страничку в файл методом page_source с расш. html
            print(f"{i}_page записана")
    except Exception as e:
        print(e)
    finally:
        browser.close()
        browser.quit()


flag = 1
if __name__ == '__main__':
    if flag:
        main_one()
    else:
        check_driver()
