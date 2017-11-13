# -*- coding: utf-8 -*-
import scrapy
from random import choice
from urllib.parse import urljoin
from scrapy.selector import Selector
from cnipr.items import CniprItem


# from cnipr.utils.bloomfilter import rc


class TouzishijianSpider(scrapy.Spider):
	name = 'cnipr_app'
	custom_settings = {
		'DEFAULT_REQUEST_HEADERS': {
			# 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
			# 'Accept-Encoding': 'gzip, deflate',
			# 'Accept-Language': 'zh-cn',
			'Connection': 'keep-alive',
			# 'Cookie': 'TailorID=3208de0a93dfd94e069897797de339da92c4',
			'Host': 'm.cnipr.com:8081',
			'Referer': 'http://m.cnipr.com:8081/tailor/http://192.168.201.132:8080/index',
			# 'Upgrade-Insecure-Requests': '1',
			# 'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0_3 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Mobile/15A432'
		}
	}

	# cookies = ['TailorID=3208de0a93dfd94e069897797de339da92c4']
	# cookie_dict = dict((line.split('=') for line in choice(cookies).strip().split(";")))

	def start_requests(self):
		# login_url = 'http://m.cnipr.com:8081/tailor/http://192.168.201.132:8080/login!goonlogin.action?rd=0.3424056342857026'
		login_url = "http://search.cnipr.com/login.action?rd=0.3424056342857026"
		payload = {'username': 'wlglzx', 'password': '!QAZ2wsx'}
		return [scrapy.FormRequest(login_url, formdata=payload, callback=self.check_login)]

	def check_login(self, response):
		comp_name = '江苏远东电机制造有限公司'
		valid_url = 'http://m.cnipr.com:8081/tailor/http://192.168.201.132:8080/search!doOverviewSearch4Index.action?DATA-start=1&limit=30&strWhere={}&yuyijs=&saveFlag=1&keyword2Save=&key2Save=&dbScope=1&type=Valid'.format(
			comp_name)
		yield scrapy.Request(valid_url)
		other_urls = [
			'http://m.cnipr.com:8081/tailor/http://192.168.201.132:8080/search!doOverviewSearch4Index.AJAX-action?DATA-start=2&limit=30&strWhere={}&yuyijs=&saveFlag=1&keyword2Save=&key2Save=&dbScope=1&type={}'.format(
				comp_name, cat) for cat in ['AtTrial', 'inValid']]
		for ourl in other_urls:
			yield scrapy.Request(ourl, callback=self.parse_trial)
		detail_url = 'http://m.cnipr.com:8081/tailor/http://192.168.201.132:8080/search!doDetailSearch.action?Data=strWhere={}&start=4&recordCursor=39&limit=1&option=2&iHitPointType=115&strSortMethod=RELEVANCE&strSources=FMZL%2CSYXX%2CWGZL%2CTWZL%2CHKPATENT%2CUSPATENT%2CJPPATENT%2CEPPATENT%2CWOPATENT%2CGBPATENT%2CDEPATENT%2CFRPATENT%2CCHPATENT%2CKRPATENT%2CRUPATENT%2CAPPATENT%2CATPATENT%2CAUPATENT%2CITPATENT%2CSEPATENT%2CCAPATENT%2CESPATENT%2CGCPATENT%2CASPATENT%2COTHERPATENT%2CTWPATENT&strSynonymous=&yuyijs=&filterChannel=&otherWhere=%5B%7B%22kind%22%3A%22%E4%B8%93%E5%88%A9%E6%9D%83%E7%8A%B6%E6%80%81%22%2C%22showwhere%22%3A%22%E6%9C%89%E6%95%88%22%2C%22where%22%3A%2210%22%7D%5D&title=10.%E4%B8%80%E7%A7%8D%E5%A4%A7%E5%8F%A3%E5%BE%84%E9%AB%98%E6%B8%A9%E8%80%90%E7%A3%A8%E5%B9%B3%E6%9D%BF%E9%97%B8%E9%98%80&keyword=%E4%B8%AD%E7%9F%B3%E5%8C%96'.format(
			comp_name)
		yield scrapy.Request(detail_url, callback=self.parse_detail)

	def parse(self, response):
		select = Selector(text=response.text)
		print(response.url)
		with open('list1.html', 'w') as f:
			f.writelines(response.text)

	def parse_trial(self, response):
		select = Selector(text=response.text)
		print(response.url)
		html_path = 'list2.html' if 'AtTrial' in response.url else 'list3.html'
		with open(html_path, 'w') as f:
			f.writelines(response.text)

	def parse_detail(self, response):
		select = Selector(text=response.text)
		print(response.url)
		with open('detail.html', 'w') as f:
			f.writelines(response.text)
