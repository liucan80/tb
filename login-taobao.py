from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from  selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import sqlite3
driver=webdriver.Chrome()
#driver=webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
driver.get("https://www.taobao.com")
driver.implicitly_wait(5)
driver.find_element_by_id("J_SiteNavMytaobao").click()
driver.implicitly_wait(5)
driver.maximize_window()
conn = sqlite3.connect("/home/luna/PycharmProjects/tb/test.db")
print("Opened database successfully")
c = conn.cursor()
c.execute('''CREATE TABLE boughtlist
              (ID INT PRIMARY KEY     NOT NULL,
              DateOfOrder           TEXT    NOT NULL,
              OrderNumber            TEXT   NOT NUll,
              NameOfShop             TEXT   NOT NULL ,
              LinkOfShop             TEXT   NOT NULL 
              );''')
print("Table created successfully")
try:
    print("请扫描二维码")
    element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "bought"))
    )
    # driver.find_element_by_css_selector("#J_SiteNavMytaobao > div.site-nav-menu-hd > a").click()
    driver.maximize_window()
    # time.sleep(5)
    # driver.implicitly_wait(5)
    driver.find_element_by_id("bought").click()
    driver.implicitly_wait(10)
    boughttables = driver.find_elements_by_class_name("bought-wrapper-mod__head-info-cell___29cDO")
    print(boughttables)
    i = 0
    for table in boughttables:
        print(table)
        i = i + 1
        DateOfOrder = table.find_element_by_class_name("bought-wrapper-mod__checkbox-label___3Va60").text
        print(DateOfOrder)
        c.execute("INSERT INTO boughtlist VALUES(%d,'%s','test','California','test')" % (i, DateOfOrder))
    conn.commit()
    conn.close()
except:
    c.execute('''DROP TABLE boughtlist;''')
    conn.commit()
    conn.close()
    print("未扫描二维码")
finally:
    print("done")
