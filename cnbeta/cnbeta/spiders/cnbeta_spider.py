from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector
from cnbeta.items import CnbetaItem
 
class CBSpider(CrawlSpider):
    name = 'cnbeta'
    allowed_domains = ['cnbeta.com']
    start_urls = ['http://www.cnbeta.com']
 
    rules = (
        Rule(SgmlLinkExtractor(allow = ('/articles/.*\.htm', )),
             callback = 'parse_page', follow = True),
    )
 
    def parse_page(self, response):
        item = CnbetaItem()
        sel = Selector(response)
        item['title'] = sel.xpath('//title/text()').extract()
        item['url'] = response.url
        return item