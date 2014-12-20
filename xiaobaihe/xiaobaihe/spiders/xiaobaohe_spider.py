#!/usr/bin/env python
# -*- coding:utf-8 -*-

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from xiaobaihe.items import XiaobaiheItem
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
import sys
reload(sys)
sys.setdefaultencoding('utf8')

class XiaoBaiHeSpider(CrawlSpider) :

    name = "xiaobaihe"
    allowed_domains = ["bbs.nju.edu.cn"]
    start_urls = ["http://bbs.nju.edu.cn/bbstdoc?board=D_Computer"]
    rules = (
        #对上一页网页加入url列表
        Rule(SgmlLinkExtractor(allow = ('http://bbs\.nju\.edu\.cn/bbstdoc\?board=D_Computer&start=\d+')), follow = True),
        #将读取的网页进行分析
        Rule(SgmlLinkExtractor(allow = ('http://bbs\.nju\.edu\.cn/bbstcon\?board=D_Computer&file=M\.\d+\.A')), callback = 'parse_page')
        )

    def parse_page(self, response) :
        sel = Selector(response)
        item = XiaobaiheItem()
        item['username'] = sel.xpath('//table/tr/td/a/text()').extract()[2]
        item['text'] = sel.xpath("//textarea/text()").extract()[0]
        return item

