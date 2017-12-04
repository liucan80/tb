from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from  selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import sqlite3
import re
import platform
import traceback
if platform.system()=="Windows":
    driver = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
    conn=sqlite3.connect("c:/test.db")
else:
    driver = webdriver.Chrome()
    conn = sqlite3.connect("/home/luna/PycharmProjects/tb/test.db")
print("Opened database successfully")
driver.get("https://www.taobao.com")
driver.implicitly_wait(5)
driver.find_element_by_id("J_SiteNavMytaobao").click()
driver.implicitly_wait(5)
driver.maximize_window()
c = conn.cursor()
try:
    c.execute('''CREATE TABLE boughtlist
                      (ID INT PRIMARY KEY     NOT NULL,
                      DateOfOrder           TEXT    NOT NULL,
                      OrderNumber            TEXT   NOT NULL,
                      NameOfShop             TEXT   NOT NULL,
                      LinkOfShop             TEXT   NOT NULL,
                      ParentOrder          TEXT     NOT NULL,
                      ProductionPic         TEXT    NULL, 
                      Production             TEXT   NULL,
                      LinkOfProduction      TEXT   NULL,
                      UnitPrice               TEXT  NULL,
                      Quantity                TEXT  NULL,
                      ActualCost             TEXT  NULL,
                      StatusOfTrade         TEXT  NULL    
                      );''')
    print("Table created successfully")
except:
    c.execute("DROP TABLE boughtlist")
    c.execute('''CREATE TABLE boughtlist
                  (ID INT PRIMARY KEY     NOT NULL,
                  DateOfOrder           TEXT    NOT NULL,
                  OrderNumber            TEXT   NOT NUll,
                  NameOfShop             TEXT   NOT NULL,
                  LinkOfShop             TEXT   NOT NULL,
                  ParentOrder          TEXT     NOT NULL,
                  ProductionPic         TEXT    NULL, 
                  Production             TEXT   NULL,
                  LinkOfProduction      TEXT   NULL,
                  UnitPrice               TEXT  NULL,
                  Quantity                TEXT  NULL,
                  ActualCost             TEXT  NULL,
                  StatusOfTrade         TEXT  NULL    
                  );''')
finally:
    print("成功创建数据表")
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
    boughttables = driver.find_elements_by_class_name("bought-wrapper-mod__table___3xFFM")
    #print(boughttables)
    i = 0
    for table in boughttables:
        i = i + 1
        #print(table)
        print(table.text)
        #OrderNumber=re.findall(r"\d{4}-\d{2}-\d{2}",table.text)
        DateOfOrder = table.find_element_by_class_name("bought-wrapper-mod__checkbox-label___3Va60").text
        print(DateOfOrder)
        OrderNumber = "".join(re.findall(r"\d{16,18}", table.text))
        print(OrderNumber)
        ParentOrder=OrderNumber
        NameOfShop = table.find_element_by_class_name("bought-wrapper-mod__seller-container___3dAK3").text
        print(NameOfShop)
        LinkOfShop = table.find_element_by_tag_name("a").get_attribute('href')
        print(LinkOfShop)
        c.execute("INSERT INTO boughtlist VALUES(%d,'%s','%s','%s','%s','','','','','','','','')" % (i, DateOfOrder, OrderNumber,NameOfShop,LinkOfShop))

        ProductionListsBody=table.find_elements_by_tag_name("tbody")
        del ProductionListsBody[0]
        for ProductionLists in ProductionListsBody:
            trs=ProductionLists.find_elements_by_tag_name("tr")
            for Productionlist in trs:
                Colms=Productionlist.find_elements_by_tag_name("td")
                Production=Colms[0].find_element_by_class_name("suborder-mod__production___3WebF").text
                LinkOfProduction=Colms[0].find_element_by_tag_name("a").get_attribute('href')
                if LinkOfProduction=="保险服务":
                    break
                UnitPrice=Colms[1].text
                Quantity=Colms[2].text
                try:
                    ActualCost=Colms[4].find_element_by_class_name("price-mod__withIcon___z4CVt").text
                except:
                    ActualCost=Colms[4].text
                finally:
                    print("")
                StatusOfTrade=Colms[5].text
                i=i+1
                c.execute(
                    "INSERT INTO boughtlist VALUES(%d,'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (
                    i, DateOfOrder, OrderNumber, NameOfShop, LinkOfShop, ParentOrder,'test', Production, LinkOfProduction,
                    UnitPrice,Quantity,ActualCost,StatusOfTrade))
                #     SubOrders=table.find_elements_by_class_name("suborder-mod__production___3WebF")
    #     print(SubOrders)
    #     UnitPrices=table.find_elements_by_class_name("price-mod__price___3Z88i")
    #     print(UnitPrices)
    #     a = 0
    #     for suborder in SubOrders:
    #
    #         LinkOfProduction=suborder.find_element_by_tag_name("a").get_attribute('href')
    #         Production=suborder.text
    #         UnitPrice=UnitPrices[a].text
    #         a=a+1
    #         if Production=="保险服务":
    #             break
    #         i = i + 1
    #         c.execute("INSERT INTO boughtlist VALUES(%d,'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','')" % (i, DateOfOrder, OrderNumber,NameOfShop,LinkOfShop,ParentOrder,Production,LinkOfProduction,'test',UnitPrice,'test','test','test'))
    conn.commit()
    conn.close()
except Exception as e:
   # c.execute('''DROP TABLE boughtlist;''')
    print(e)
    conn.commit()
    conn.close()
    print("未扫描二维码")
finally:
    print("done")
