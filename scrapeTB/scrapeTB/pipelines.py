# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import sqlite3
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
class ScrapetbPipeline(object):
    #spider开始工作时执行的函数
    def open_spider(self,spider):
        #创建数据库
        dbpath = "{0}/db".format(os.getcwd())
        mkdir(dbpath)
        self.conn = sqlite3.connect("{0}/已买到的宝贝.db".format(dbpath))
        self.c = self.conn.cursor()
        try:
            self.c.execute('''CREATE TABLE boughtlist
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
            self.c.execute("DROP TABLE boughtlist")
            self.c.execute('''CREATE TABLE boughtlist
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
        pass
    def close_spider(self,spider):
        self.conn.close()
        pass
    def process_item(self, item, spider):
        self.c.execute()
        item['ID']
        return item
