# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WechatspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    wechatID=scrapy.Field()

class DataspiderItem(scrapy.Item):
    pass