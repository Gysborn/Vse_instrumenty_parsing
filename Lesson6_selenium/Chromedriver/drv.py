import time

from selenium import webdriver
import os

driver = webdriver.Chrome()
try:
    driver.get(url="https://automated-testing.info/")
    time.sleep(5)
    driver.get(url="https://tury.ru/")
except Exception as e:
    print(e)
finally:
    driver.close()
    driver.quit()
