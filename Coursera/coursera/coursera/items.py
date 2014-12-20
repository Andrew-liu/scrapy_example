# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class CourseraItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = Field()
    mp4_url = Field()
    #pdf_url = Field()
    #txt_url = Field()
    #srt_url = Field()
