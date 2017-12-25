# -*- coding: utf-8 -*-
import scrapy


class ScrapytaobaoSpider(scrapy.Spider):
    name = 'scrapytaobao'
    #allowed_domains = ['www.baidu.com']
    start_urls = ['https://buyertrade.taobao.com/trade/itemlist/list_bought_items.htm']

    def parse(self, response):
        print(response.body)


