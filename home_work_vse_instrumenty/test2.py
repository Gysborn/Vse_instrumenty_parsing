from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
# from openpyxl import Workbook
# from openpyxl import load_workbook


# wb = load_workbook('sample.xlsx')
# sheets = wb.sheetnames
# if 'Sheet'in sheets:
#     del wb['Sheet']
# ws = wb.create_sheet('Sheet')
# ws = wb.active

url = 'https://rostov.vseinstrumenti.ru/category/bolgarki-ushm-123/page2/'

driver = webdriver.Chrome()


try:
    driver.get(url)
    time.sleep(100)
    elements = driver.find_elements(By.CLASS_NAME, 'Wk5Je9')
    print(elements)
    for e in elements:
        print(e)
        # row = e.text.split(sep='\n')
        # ws.append(row)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()

#wb.save("sample.xlsx")