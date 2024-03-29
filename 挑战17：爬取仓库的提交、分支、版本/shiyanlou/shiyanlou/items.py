# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MultipageCourseItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    update_time = scrapy.Field()
    commits = scrapy.Field()
    branches = scrapy.Field()
    releases = scrapy.Field()
