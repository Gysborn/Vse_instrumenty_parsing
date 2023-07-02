import json
import time
import pickle
import requests as requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


def get_chromedriver(user_agent=None):  # Получаем наш виртуальный браузер Chrome
    options = webdriver.ChromeOptions()  # Создаем объект опций
    options.add_argument(f'--user-agent={user_agent}')  # Добавляем в опции user-agent
    # options.add_argument('--proxy-server=38.154.88.110:8000')
    options.add_argument("--disable-blink-features=AutomationControlled")
    service = Service(executable_path="home_work_vse_instrumenty/chromedriver.exe")  # Создаем сервис в который передаем путь до драйвера
    return webdriver.Chrome(service=service, options=options)  # Возвращаем сконфигурированный объект браузера


# from requests_html import HTMLSession
# url = "https://spb.vseinstrumenti.ru/category/rychazhnye-trubnye-klyuchi-shvedskogo-tipa-13495/"
# url1 = "https://www.vseinstrumenti.ru/category/rychazhnye-trubnye-klyuchi-shvedskogo-tipa-13495/"
# local = "http://localhost:63342/parser_part2_health-diet/home_work_vse_instrumenty/data/vi_index.html?_ijt=jk2fdtoom4d49fv900oiq1nd20&_ij_reload=RELOAD_ON_SAVE"
# user_agent = "Mozilla/5.0 (hp-tablet; Linux; hpwOS/3.0.5; U; en-US) AppleWebKit/534.6 (KHTML, like Gecko) wOSBrowser/234.83 Safari/534.6 TouchPad/1.0"

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
#user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
# session = HTMLSession()
# r = session.get(url=url)
# print(r)
headers = {
    "User-Agent": user_agent
}
def main():
    try:  # Получаем наш браузер с user-agent ом
        browser = get_chromedriver(user_agent=user_agent)
        browser.get(url=url1)  # Передаем урл в браузер
        cookies = pickle.load(open("vi_cookies", "rb"))
        for cookie in cookies:
            browser.add_cookie(cookie)
            browser.refresh()
        time.sleep(10)

        print("куки загружены")
        elements = browser.find_elements(By.CLASS_NAME, "Z6EojR Z9UMXC")
        if not elements:
            print("None")
        for element in elements:
            print(element)
        hrefs = browser.find_element(By.CLASS_NAME, "Z6EojR Z9UMXC")
        print(hrefs)
        with open("data/vi_index.html", "w", encoding="utf-8") as file:
             file.write(browser.page_source)  # Сохраняем страничку в файл методом page_source
        with open("data/vi_index.html", encoding='utf-8') as file:
            src = file.read()# Считываем
        soup = BeautifulSoup(src, "lxml")
        result = soup.find_all("div", class_="Z6EojR Z9UMXC")
        collect = []
        for res in result:
            href = "https://www.vseinstrumenti.ru/" + res.find("a").get("href")
            collect.append(href)
        with open("data/vi_links.txt", "w", encoding="utf-8") as f:
            for line in collect:
                f.write(f"{line}\n")

        # with open("data/instr_index.html", encoding="utf-8") as f:
        #     src = f.read()
        # print(src)
    except Exception as e:
        print(e)
    # finally:
    #     browser.close()  # Закрываем
    #     browser.quit()  # Выходим


if __name__ == '__main__':
    main()
