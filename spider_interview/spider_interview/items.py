# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SpiderInterviewItem(scrapy.Item):
    # define the fields for your item here like:
    date = scrapy.Field()
    star_name = scrapy.Field()
    fortune = scrapy.Field()
    pass
