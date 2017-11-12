from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class ZhongGuoZhiZaoCrawlSpider(CrawlSpider):
	name = 'zhong'
	allowed_domains = ['cn.made-in-china.com/']
	start_urls = ['http://cn.made-in-china.com/gongsi/']

	rules = (
		Rule(LinkExtractor(allow='-gongsi-\d+\.html$')),
		Rule(LinkExtractor(allow=('/showroom/', '\w+\.cn\.made-in-china\.com$')), callback='parse_item')
	)

	def parse_item(self, response):
		pass
