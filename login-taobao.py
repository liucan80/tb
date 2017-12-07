from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from  selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import sqlite3
import re
import platform
import urllib.request
import sys
import os


def mkdir(path):
    # 引入模块
    import os

    # 去除首位空格
    path = path.strip()
    # 去除尾部 \ 符号
    path = path.rstrip("\\")

    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists = os.path.exists(path)

    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(path)
        print(path + ' 创建成功')

        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print(path + ' 目录已存在')
        return False
def readImage(path):
    try:
        fin = open(path, "rb")
        img = fin.read()
        return img
    except IOError:

        print("2")
        sys.exit(1)

    finally:

        if fin:
            fin.close()
def findandstore(pagenumber,ID):

    if pagenumber==1:
        driver.implicitly_wait(10)
        boughttables = driver.find_elements_by_class_name("bought-wrapper-mod__table___3xFFM")
        for table in boughttables:
            ID = ID + 1
            # print(table)
            print(table.text)
            # OrderNumber=re.findall(r"\d{4}-\d{2}-\d{2}",table.text)
            DateOfOrder = table.find_element_by_class_name("bought-wrapper-mod__checkbox-label___3Va60").text
            print(DateOfOrder)
            OrderNumber = "".join(re.findall(r"\d{15,18}", table.text))
            print(OrderNumber)
            ParentOrder = OrderNumber
            NameOfShop = table.find_element_by_class_name("bought-wrapper-mod__seller-container___3dAK3").text
            print(NameOfShop)
            LinkOfShop = table.find_element_by_tag_name("a").get_attribute('href')
            print(LinkOfShop)
            c.execute("INSERT INTO boughtlist VALUES(%d,'%s','%s','%s','%s','','','','','','','','')" % (
            ID, DateOfOrder, OrderNumber, NameOfShop, LinkOfShop))

            ProductionListsBody = table.find_elements_by_tag_name("tbody")
            del ProductionListsBody[0]
            for ProductionLists in ProductionListsBody:
                trs = ProductionLists.find_elements_by_tag_name("tr")
                for Productionlist in trs:
                    Colms = Productionlist.find_elements_by_tag_name("td")

                    Production = Colms[0].find_element_by_class_name("suborder-mod__production___3WebF").text
                    LinkOfProduction = Colms[0].find_element_by_tag_name("a").get_attribute('href')
                    if Production == '保险服务':
                        break
                    try:
                        ProductionPiclink = Colms[0].find_element_by_tag_name("a").find_element_by_tag_name("img").get_attribute('src')
                        ProductionPic=urllib.request.urlopen(ProductionPiclink).read()
                        PicPath=("{0}/{1}.jpg".format(picturespath,ID))
                        tempdile = open(PicPath, 'wb')
                        tempdile.write(ProductionPic)
                        tempdile.close()
                        data = readImage(PicPath)
                        #ProductionPic = sqlite3.Binary(ProductionPic)
                        ProductionPic = sqlite3.Binary(data)
                        #c.execute("INSERT INTO Images(Data) VALUES (?)", (ProductionPic,))
                        # tempdile = open('c:/tes1.png', 'wb')
                        # tempdile.write(ProductionPic)
                    except:
                        ProductionPic='test'
                        print("未找到图片")

                    UnitPrice = Colms[1].text
                    Quantity = Colms[2].text
                    ActualCost = Colms[4].text
                    StatusOfTrade = Colms[5].text
                    ID = ID + 1
                    c.execute(
                        "INSERT INTO boughtlist VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)",  (
                            ID, DateOfOrder, OrderNumber, NameOfShop, LinkOfShop, ParentOrder, ProductionPic, Production,
                            LinkOfProduction,
                            UnitPrice, Quantity, ActualCost, StatusOfTrade))
                    #     SubOrders=table.find_elements_by_class_name("suborder-mod__production___3WebF")
        conn.commit()
        return ID
    elif pagenumber>1:
        driver.implicitly_wait(10)
        boughttables = driver.find_elements_by_class_name("bought-wrapper-mod__table___3xFFM")
        for table in boughttables:
            ID = ID + 1
            # print(table)
            print(table.text)
            # OrderNumber=re.findall(r"\d{4}-\d{2}-\d{2}",table.text)
            DateOfOrder = table.find_element_by_class_name("bought-wrapper-mod__checkbox-label___3Va60").text
            print(DateOfOrder)
            OrderNumber = "".join(re.findall(r"\d{15,18}", table.text))
            print(OrderNumber)
            ParentOrder = OrderNumber
            NameOfShop = table.find_element_by_class_name("bought-wrapper-mod__seller-container___3dAK3").text
            print(NameOfShop)
            LinkOfShop = table.find_element_by_tag_name("a").get_attribute('href')
            print(LinkOfShop)
            c.execute("INSERT INTO boughtlist VALUES(%d,'%s','%s','%s','%s','','','','','','','','')" % (
                ID, DateOfOrder, OrderNumber, NameOfShop, LinkOfShop))

            ProductionListsBody = table.find_elements_by_tag_name("tbody")
            del ProductionListsBody[0]
            for ProductionLists in ProductionListsBody:
                trs = ProductionLists.find_elements_by_tag_name("tr")
                for Productionlist in trs:
                    Colms = Productionlist.find_elements_by_tag_name("td")
                    try:
                        Production = Colms[0].find_element_by_class_name("suborder-mod__production___3WebF").text
                        LinkOfProduction = Colms[0].find_element_by_tag_name("a").get_attribute('href')
                    except:
                        Production=Colms[0].text
                        LinkOfProduction = ''
                    if Production == '保险服务':
                        break
                    try:
                        ProductionPiclink = Colms[0].find_element_by_tag_name("a").find_element_by_tag_name(
                            "img").get_attribute('src')
                        ProductionPic = urllib.request.urlopen(ProductionPiclink).read()
                        PicPath = ("{0}/{1}.jpg".format(picturespath, ID))
                        tempdile = open(PicPath, 'wb')
                        tempdile.write(ProductionPic)
                        tempdile.close()
                        data = readImage(PicPath)
                        # ProductionPic = sqlite3.Binary(ProductionPic)
                        ProductionPic = sqlite3.Binary(data)
                        # c.execute("INSERT INTO Images(Data) VALUES (?)", (ProductionPic,))
                        # tempdile = open('c:/tes1.png', 'wb')
                        # tempdile.write(ProductionPic)
                    except:
                        ProductionPic = 'test'
                        print("未找到图片")

                    UnitPrice = Colms[1].text
                    Quantity = Colms[2].text
                    ActualCost=Colms[4].text
                    # try:
                    #     ActualCost = Colms[4].find_element_by_class_name("price-mod__withIcon___z4CVt").text
                    # except:
                    #     ActualCost = Colms[4].text
                    # finally:
                    #     print("")
                    StatusOfTrade = Colms[5].text
                    ID = ID + 1
                    c.execute(
                        "INSERT INTO boughtlist VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)", (
                            ID, DateOfOrder, OrderNumber, NameOfShop, LinkOfShop, ParentOrder, ProductionPic,
                            Production,
                            LinkOfProduction,
                            UnitPrice, Quantity, ActualCost, StatusOfTrade))
                    #     SubOrders=table.find_elements_by_class_name("suborder-mod__production___3WebF")
        conn.commit()
        return ID
    else:
        print("完成")
        return ID
picturespath="{0}/prictures".format(os.getcwd())
dbpath="{0}/db".format(os.getcwd())
mkdir(picturespath)
mkdir(dbpath)

if platform.system()=="Windows":
    driver = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
    conn=sqlite3.connect("{0}/已买到的宝贝.db".format(dbpath))
else:
    driver = webdriver.Chrome()
    conn = sqlite3.connect("{0}/已买到的宝贝.db".format(dbpath))
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
                      ProductionPic         BLOB    NULL, 
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
                  ProductionPic         BLOB    NULL, 
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
    element = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.ID, "bought"))
    )
    driver.maximize_window()
    driver.find_element_by_id("bought").click()
    driver.implicitly_wait(10)
    pagenumber=1
    ID=0
    contents = driver.find_element_by_class_name("simple-pagination-mod__container___2bG5u").find_elements_by_tag_name(
        "button")
    while True:
        if pagenumber>=1:
            ID=findandstore(pagenumber, ID)
            contents[1].click()
            time.sleep(6)
            pagenumber=pagenumber+1
            if not contents[1].is_enabled():
                ID = findandstore(pagenumber, ID)
                break




    conn.close()
except Exception as e:
   # c.execute('''DROP TABLE boughtlist;''')
    print(e)
    conn.commit()
    conn.close()
    print("未扫描二维码")
finally:
    print("done")

