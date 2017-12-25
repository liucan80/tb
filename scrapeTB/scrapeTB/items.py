# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class ScrapetbItem(scrapy.Item):
    # define the fields for your item here like:
    #订单ID,由本程序产生
    ID=scrapy.Field()
    #订单创建日期
    DateOfOrder=scrapy.Field()
    #订单号
    OrderNumber=scrapy.Field()
    #由于可能出现一个订单多种商品，所以定义一个父订单号，用来保证数据的层级关系
    ParentOrder=scrapy.Field()
    #店铺名称
    NameOfShop=scrapy.Field()
    #店铺的链接
    LinkOfShop=scrapy.Field()

    #宝贝名称
    Production=scrapy.Field()
    #宝贝链接
    LinkOfProduction=scrapy.Field()
    #宝贝图片(s缩略图)
    ProductionPic=scrapy.Field()
    #宝贝单价
    UnitPrice=scrapy.Field()
    #订购数量
    Quantity=scrapy.Field()
    #实际价格
    ActualCost=scrapy.Field()
    #订单状态
    StatusOfTrade=scrapy.Field()

