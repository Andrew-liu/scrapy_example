#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
一个简单的Python爬虫, 用于抓取coursera网站的下载链接和pdf

Anthor: Andrew Liu
Version: 0.0.2
Date: 2014-12-15
Language: Python2.7.8
Editor: Sublime Text2
Operate: 具体操作请看README.md介绍
"""

import scrapy
import random, string
from scrapy.http import Request, FormRequest
from scrapy.selector import Selector
from coursera.items import CourseraItem

def random_string(length):
    """
    随机生成指定长度的字母和数字序列
    """
    return ''.join(random.choice(string.letters + string.digits) for i in xrange(length))

class CourseraSipder(scrapy.Spider) :
    name = "coursera"
    allowed_domains = ["coursera.org"]
    start_urls = [
        "https://class.coursera.org/pkuco-001/lecture"
    ]

    def make_header(self, response) :
        user_agent = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/38.0.2125.111 Safari/537.36")
        XCSRF2Cookie = 'csrf2_token_%s' % ''.join(random_string(8))
        XCSRF2Token = ''.join(random_string(24))
        XCSRFToken = ''.join(random_string(24))
        cookie = "csrftoken=%s; %s=%s" % (XCSRFToken, XCSRF2Cookie, XCSRF2Token)
        headers= {
                "Referer": response.url,  #对付防盗链设置, 为跳转来源的url
                "User-Agent": user_agent, #伪装成浏览器访问
                "X-Requested-With": "XMLHttpRequest",
                "X-CSRF2-Cookie": XCSRF2Cookie,
                "X-CSRF2-Token": XCSRF2Token,
                "X-CSRFToken": XCSRFToken,
                "Cookie": cookie
            }
        return headers


    def start_requests(self):
        print 'Preparing login'
        return [FormRequest("https://accounts.coursera.org/api/v1/login",
                            headers = self.make_header(response),
                            formdata = {
                            "email": "1095511864@qq.com",
                            "password": "HUAZANG.55789260",
                            "webrequest": "true"
                            },
                            callback = self.parse_page
                            )]


    def parse_page(self, response):
        course = Selector(response)
        item = CourseraItem()
        item['title'] = course.xpath('//pre/a/text()').extract()
        item['mp4_url'] = course.xpath('//pre/text()[2]').extract()
        return item
