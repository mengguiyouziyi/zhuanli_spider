# -*- coding: utf-8 -*-
import scrapy
import requests
import json
from random import choice
from urllib.parse import urljoin
from scrapy.selector import Selector
from cnipr.items import CniprItem


# from cnipr.utils.bloomfilter import rc


class TouzishijianSpider(scrapy.Spider):
	name = 'cnipr_app'
	# cookies = ['TailorID=3208de0a93dfd94e069897797de339da92c4']
	# cookie_dict = dict((line.split('=') for line in choice(cookies).strip().split(";")))
	custom_settings = {
		'DEFAULT_REQUEST_HEADERS': {
			'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
			'Accept-Encoding': 'gzip, deflate',
			'Accept-Language': 'zh-cn',
			'Connection': 'keep-alive',
			# 'Cookie': 'TailorID=3208de0a93dfd94e069897797de339da92c4',
			'Host': 'm.cnipr.com:8081',
			'Referer': 'http://m.cnipr.com:8081/tailor/http://192.168.201.132:8080/index',
			'Upgrade-Insecure-Requests': '1',
		},
		'USER_AGENT_CHOICES': [
			'Mozilla/5.0 (Linux; Android 5.1.1; vivo X6S A Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/35.0.1916.138 Mobile Safari/537.36 T7/6.3 baiduboxapp/7.3.1 (Baidu; P1 5.1.1)',
			# 'Mozilla/5.0 (Linux; U; Android 5.0.2; zh-CN; Letv X501 Build/DBXCNOP5501304131S) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/10.10.0.800 U3/0.8.0 Mobile Safari/534.30',
			# 'Mozilla/5.0 (Linux; U; Android 5.0.2; zh-cn; Letv X501 Build/DBXCNOP5501304131S) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/6.7 Mobile Safari/537.36',
			# 'Mozilla/5.0 (Linux; U; Android 4.3; zh-cn; N5117 Build/JLS36C) AppleWebKit/534.24 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.24 T5/2.0 baiduboxapp/7.0 (Baidu; P1 4.3)',
			# 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_2_1 like Mac OS X; zh-CN) AppleWebKit/537.51.1 (KHTML, like Gecko) Mobile/13D15 UCBrowser/10.9.15.793 Mobile',
			# 'Mozilla/5.0 (iPhone 6p; CPU iPhone OS 9_2_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/6.0 MQQBrowser/6.7 Mobile/13D15 Safari/8536.25 MttCustomUA/2',
			# 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_2_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13D15 Safari/601.1',
			# 'Mozilla/5.0 (Linux; U; Android 4.1.2; zh-cn; GT-S7572 Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/6.7 Mobile Safari/537.36',
			# 'Mozilla/5.0 (Linux; U; Android 5.1.1; zh-cn; SM-J3109 Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/6.6 Mobile Safari/537.36',
			# 'Mozilla/5.0 (Linux; U; Android 4.4.4; zh-cn; Coolpad 8297-T01 Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/6.6 Mobile Safari/537.36',
			# 'Mozilla/5.0 (Linux; U; Android 5.1.1; zh-CN; MX4 Pro Build/LMY48W) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/10.10.0.800 U3/0.8.0 Mobile Safari/534.30',
			# 'Mozilla/5.0 (Linux; Android 5.1; m2 note Build/LMY47D) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.114 Mobile Safari/537.36',
			# 'Mozilla/5.0 (Linux; U; Android 5.1; zh-CN; m2 note Build/LMY47D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/10.9.10.788 U3/0.8.0 Mobile Safari/534.30',
			# 'Mozilla/5.0 (Linux; U; Android 5.1; zh-cn; m2 note Build/LMY47D) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/6.6 Mobile Safari/537.36',
			# 'Mozilla/5.0 (Linux; U; Android 4.4.4; zh-cn; CHM-CL00 Build/CHM-CL00) AppleWebKit/534.24 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.24 T5/2.0 baiduboxapp/7.1 (Baidu; P1 4.4.4)',
			# 'Mozilla/5.0 (Linux; Android 5.0.1; HUAWEI GRA-TL00 Build/HUAWEIGRA-TL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36 MxBrowser/4.5.9.3000',
			# 'Mozilla/5.0 (Linux; Android 5.0.1; HUAWEI GRA-CL00 Build/HUAWEIGRA-CL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/35.0.1916.138 Mobile Safari/537.36 T7/6.3 baiduboxapp/7.3.1 (Baidu; P1 5.0.1)',
			# 'Mozilla/5.0 (Linux; Android 5.0.2; Redmi Note 2 Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/35.0.1916.138 Mobile Safari/537.36 T7/6.3 baiduboxapp/7.3.1 (Baidu; P1 5.0.2)',
			# 'Mozilla/5.0 (Linux; Android 4.4.4; Che1-CL10 Build/Che1-CL10) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/35.0.1916.138 Mobile Safari/537.36 T7/6.3 baiduboxapp/7.3.1 (Baidu; P1 4.4.4)',
			# 'Mozilla/5.0 (Linux; U; Android 4.4.2; zh-cn; HUAWEI P6-C00 Build/HuaweiP6-C00) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/6.7 Mobile Safari/537.36',
		]
	}
	headers = {'User-Agent': choice(custom_settings.get('USER_AGENT_CHOICES'))}
	headers.update(custom_settings.get('DEFAULT_REQUEST_HEADERS'))
	proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
		"host": "http-dyn.abuyun.com",
		"port": "9020",
		"user": "HJ3F19379O94DO9D",
		"pass": "D1766F5002A70BC4",
	}
	proxies = {
		"http": proxyMeta,
		"https": proxyMeta,
	}

	def __init__(self):
		self.cookie_dict = self.login()

	def login(self):
		login_url = 'http://m.cnipr.com:8081/tailor/http://192.168.201.132:8080/login!goonlogin.action?rd=0.3424056342857026'
		payloads = [{'username': 'wlglzx', 'password': '!QAZ2wsx'},
		            {'username': 'mengguiyouziyi', 'password': '3646287'}]
		response = requests.request("POST", login_url, headers=self.headers, data=choice(payloads))
		cookie_dict = dict(response.cookies.items())
		print('cookie', cookie_dict)
		return cookie_dict

	def start_requests(self):
		comp_name = '北京纳米能源与系统研究所'
		valid_url = 'http://m.cnipr.com:8081/tailor/http://192.168.201.132:8080/search!doOverviewSearch4Index.action?DATA-start=1&limit=10&strWhere={}&yuyijs=&saveFlag=1&keyword2Save=&key2Save=&dbScope=1&type=Valid'.format(
			comp_name)
		yield scrapy.Request(valid_url, cookies=self.cookie_dict)

	# other_urls = [
	# 	'http://m.cnipr.com:8081/tailor/http://192.168.201.132:8080/search!doOverviewSearch4Index.AJAX-action?DATA-start=2&limit=10&strWhere={}&yuyijs=&saveFlag=1&keyword2Save=&key2Save=&dbScope=1&type={}'.format(
	# 		comp_name, cat) for cat in ['AtTrial', 'inValid']]
	# for ourl in other_urls:
	# 	yield scrapy.Request(ourl, callback=self.parse_trial, cookies=self.cookie_dict)
	# detail_url = 'http://m.cnipr.com:8081/tailor/http://192.168.201.132:8080/search!doDetailSearch.action?Data=strWhere={}&start=4&recordCursor=39&limit=1&option=2&iHitPointType=115&strSortMethod=RELEVANCE&strSources=FMZL%2CSYXX%2CWGZL%2CTWZL%2CHKPATENT%2CUSPATENT%2CJPPATENT%2CEPPATENT%2CWOPATENT%2CGBPATENT%2CDEPATENT%2CFRPATENT%2CCHPATENT%2CKRPATENT%2CRUPATENT%2CAPPATENT%2CATPATENT%2CAUPATENT%2CITPATENT%2CSEPATENT%2CCAPATENT%2CESPATENT%2CGCPATENT%2CASPATENT%2COTHERPATENT%2CTWPATENT&strSynonymous=&yuyijs=&filterChannel=&otherWhere=%5B%7B%22kind%22%3A%22%E4%B8%93%E5%88%A9%E6%9D%83%E7%8A%B6%E6%80%81%22%2C%22showwhere%22%3A%22%E6%9C%89%E6%95%88%22%2C%22where%22%3A%2210%22%7D%5D&title=10.%E4%B8%80%E7%A7%8D%E5%A4%A7%E5%8F%A3%E5%BE%84%E9%AB%98%E6%B8%A9%E8%80%90%E7%A3%A8%E5%B9%B3%E6%9D%BF%E9%97%B8%E9%98%80&keyword=%E4%B8%AD%E7%9F%B3%E5%8C%96'.format(
	# 	comp_name)
	# yield scrapy.Request(detail_url, callback=self.parse_detail, cookies=self.cookie_dict)

	def captcha(self, response):
		# t = self.session.get(captcha_url, headers=self.headers)
		with open("captcha.jpg", "wb") as f:
			f.write(response.body)
		from PIL import Image
		try:
			im = Image.open("captcha.jpg")
			im.show()
			im.close()
		except:
			pass
		captcha = input("输入验证码\n>")
		url = 'http://m.cnipr.com:8081/tailor/http://192.168.201.132:8080/checkcode.action?checkCode={}'.format(captcha)
		yield scrapy.Request(url, cookies=self.cookie_dict)

	def check_captcha(self, response):
		if 'true' in response.text:
			print('验证码正确')
			self.start_requests()

	def parse(self, response):
		print(response.url)
		if '申请号：' not in response.text:
			cap_url = 'http://m.cnipr.com:8081/tailor/http://192.168.201.132:8080/RandomCode'
			yield scrapy.Request(cap_url, callback=self.captcha, cookies=self.cookie_dict)
			return
		select = Selector(text=response.text)
		with open('list1.html', 'w') as f:
			f.writelines(response.text)

	def parse_trial(self, response):
		print(response.url)
		text = json.loads(response.text)
		img_code = text.get('imgCode')
		if not img_code:
			return
		select = Selector(text=img_code)
		html_path = 'list2.html' if 'AtTrial' in response.url else 'list3.html'
		with open(html_path, 'w') as f:
			f.writelines(text)

	def parse_detail(self, response):
		select = Selector(text=response.text)
		print(response.url)
		with open('detail.html', 'w') as f:
			f.writelines(response.text)
