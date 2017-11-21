# -*- coding: utf-8 -*-
import scrapy
import requests
from random import choice
from urllib.parse import urljoin
from scrapy.selector import Selector
# from cnipr.utils.bloomfilter import rc
from cnipr.items import CniprItem


class TouzishijianSpider(scrapy.Spider):
	name = 'cnipr'

	# custom_settings = {
	# 	'DEFAULT_REQUEST_HEADERS': {
	# 		'accept': "text/html,application/xhtml+xm…plication/xml;q=0.9,*/*;q=0.8:",
	# 		'accept-encoding': "gzip, deflate:",
	# 		'accept-language': "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2:",
	# 		'connection': "keep-alive:",
	# 		'host': "search.cnipr.com:",
	# 		'upgrade-insecure-requests': "1:",
	# 		'user-agent': "Mozilla/5.0 (Macintosh; Intel …) Gecko/20100101 Firefox/57.0:",
	# 		'cache-control': "no-cache",
	# 		'postman-token': "95b41227-4271-a619-d6c6-51fb69af28e4"
	# 	},
	# 	'USER_AGENT_CHOICES': [
	# 		'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0_3 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Mobile/15A432',
	# 		# 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
	# 		# 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
	# 		# 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
	# 		# 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; InfoPath.3; rv:11.0) like Gecko',
	# 		# 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;',
	# 		# 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;',
	# 		# 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
	# 		# 'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
	# 		# 'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11',
	# 		# 'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11',
	# 		# 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
	# 		# 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)',
	# 		# 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)',
	# 		# 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
	# 		# 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)',
	# 		# 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)',
	# 		# 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)',
	# 		# 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser)',
	# 		# 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
	# 		# "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
	# 		# "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
	# 		# "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
	# 		# "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
	# 		# "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
	# 		# "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
	# 		# "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
	# 		# "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
	# 		# "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
	# 		# "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
	# 		# "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
	# 		# "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
	# 		# "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
	# 		# "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
	# 		# "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
	# 		# "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
	# 	]
	# }

	# headers = {'User-Agent': choice(custom_settings.get('USER_AGENT_CHOICES'))}
	# headers.update(custom_settings.get('DEFAULT_REQUEST_HEADERS'))
	# proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
	# 	"host": "http-dyn.abuyun.com",
	# 	"port": "9020",
	# 	"user": "HJ3F19379O94DO9D",
	# 	"pass": "D1766F5002A70BC4",
	# }
	# proxies = {
	# 	"http": proxyMeta,
	# 	"https": proxyMeta,
	# }

	# def __init__(self):
	# 	self.cookie_dict = self.login()

	# def login(self):
	# 	login_url = 'http://search.cnipr.com/login.action?rd=0.4289715556717164'
	# 	payloads = [
	# 		# {'username': 'wlglzx', 'password': '!QAZ2wsx'},
	# 		{'username': 'mengguiyouziyi', 'password': '3646287'}
	# 	]
	# 	response = requests.request("POST", login_url, data=choice(payloads))
	# 	cookie_dict = dict(response.cookies.items())
	# 	print('cookie', cookie_dict)
	# 	return cookie_dict

	def start_requests(self):
		headers = {
			'host': "search.cnipr.com",
			'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:57.0) Gecko/20100101 Firefox/57.0",
			'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
			'accept-language': "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
			'accept-encoding': "gzip, deflate",
			'connection': "keep-alive",
			'upgrade-insecure-requests': "1",
			'cache-control': "no-cache",
			'postman-token': "39717c81-4ef8-8cfd-004a-97afa3493a13"
		}
		url = 'http://search.cnipr.com/login.action'
		yield scrapy.Request(url, headers=headers)

	def parse(self, response):
		headers = {
			# 'host': "search.cnipr.com",
			# 'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:57.0) Gecko/20100101 Firefox/57.0",
			# 'accept': "*/*",
			# 'accept-language': "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
			# 'accept-encoding': "gzip, deflate",
			# 'referer': "http://search.cnipr.com/login.action",
			'content-type': "application/x-www-form-urlencoded",
			# 'x-requested-with': "XMLHttpRequest",
			# 'content-length': "33",
			# 'cookie': "JSESSIONID=A324C01B7A086473DFBF33DA0071AD2E",
			# 'connection': "keep-alive",
			# 'cache-control': "no-cache",
			# 'postman-token': "b061ecc6-fca0-dcb8-b1da-6439b6f1c07d"
		}
		# login_url = 'http://m.cnipr.com:8081/tailor/http://192.168.201.132:8080/login!goonlogin.action?rd=0.3424056342857026'
		# login_url = 'http://search.cnipr.com/user!gotoLogin.action?forward='
		login_url = 'http://search.cnipr.com/login.action?rd=0.6589196511445976'
		# payloads = [
		# {'username': 'wlglzx', 'password': '!QAZ2wsx'},
		# {'username': 'mengguiyouziyi', 'password': '3646287'}
		# ]
		# payloads = {'username': 'mengguiyouziyi', 'password': '3646287'}

		# cookies = "JSESSIONID=A324C01B7A086473DFBF33DA0071AD2E",
		# cookie_dict = dict((line.split('=') for line in choice(cookies).strip().split(";")))
		payloads = 'username=mengguiyouziyi&password=3646287'
		yield scrapy.Request(method="POST", url=login_url, body=payloads, callback=self.parse_1, headers=headers)
		# return [scrapy.FormRequest(login_url, formdata=payloads, headers=headers, callback=self.parse_1)]

	# cookie_dict = dict(response.cookies.items())
	# print('cookie', cookie_dict)
	# 	return cookie_dict

	def parse_1(self, response):
		headers = {
			# 'host': "search.cnipr.com",
			# 'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:57.0) Gecko/20100101 Firefox/57.0",
			# 'accept': "*/*",
			# 'accept-language': "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
			# 'accept-encoding': "gzip, deflate",
			# 'referer': "http://search.cnipr.com/login.action",
			'content-type': "application/x-www-form-urlencoded",
			# 'x-requested-with': "XMLHttpRequest",
			# 'content-length': "33",
			# 'cookie': "JSESSIONID=1692D75AD24053A93768D8C212EDD288; _trs_uv=ja7xjh9r_1186_cmc6; _trs_ua_s_1=ja7xjh9r_1186_dajq; _gscu_719616686=11166540rtuice38; _gscs_719616686=11166540zttkjz38|pv:2; _gscbrs_719616686=1",
			# 'connection': "keep-alive",
			# 'cache-control': "no-cache",
			# 'postman-token': "c9e8a3f6-4fdd-203f-cc4d-f6cda6624cb5"
		}
		start_url = "http://search.cnipr.com/search%21doOverviewSearch.action"
		f = 'strWhere=%E7%94%B3%E8%AF%B7%EF%BC%88%E4%B8%93%E5%88%A9%E6%9D%83%EF%BC%89%E4%BA%BA%3D%28%E4%B8%AD%E5%9B%BD%E7%9F%B3%E6%B2%B9%E5%8C%96%E5%B7%A5%E8%82%A1%E4%BB%BD%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8%29&yuyijs=&start=1&saveFlag=1&limit=10&strSynonymous=&crossLanguage=&islogicsearch=false&saveExp=&showhint=&mpage=null&channelId=FMZL&channelId=SYXX&channelId=WGZL&channelId=FMSQ&channelId=TWZL&channelId=HKPATENT&channelId=USPATENT&channelId=EPPATENT&channelId=JPPATENT&channelId=WOPATENT&channelId=GBPATENT&channelId=CHPATENT&channelId=DEPATENT&channelId=KRPATENT&channelId=FRPATENT&channelId=RUPATENT&channelId=ASPATENT&channelId=ATPATENT&channelId=GCPATENT&channelId=ITPATENT&channelId=AUPATENT&channelId=APPATENT&channelId=CAPATENT&channelId=SEPATENT&channelId=ESPATENT&channelId=OTHERPATENT&trsq=1&dan=1&txt_A=&txt_B=&txt_C=&txt_D=&txt_E=&txt_F=&txt_Q=&txt_R=&txt_I=%E4%B8%AD%E5%9B%BD%E7%9F%B3%E6%B2%B9%E5%8C%96%E5%B7%A5%E8%82%A1%E4%BB%BD%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8&txt_J=&txt_G=&txt_H=&txt_L=&txt_O=&text=&txt_K=&txt_M=&txt_N=&txt_U=&txt_T=&txt_V=&txt_X=&mpage=advsch'
		# formdata = dict([m.split('=') for m in f.split('&')])
		yield scrapy.Request(start_url, method='POST', body=f, callback=self.parse_login, headers=headers)

	def parse_login(self, response):
		with open('list.html', 'w') as f:
			f.writelines(response.text)







	# 	headers = {
	# 		# 'host': "search.cnipr.com",
	# 		'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
	# 		# 'accept': "*/*",
	# 		# 'accept-language': "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
	# 		# 'accept-encoding': "gzip, deflate",
	# 		# 'referer': "http://search.cnipr.com/search%21doOverviewSearch.action",
	# 		# 'content-type': "application/x-www-form-urlencoded",
	# 		# 'x-requested-with': "XMLHttpRequest",
	# 		# 'content-length': "33",
	# 		# 'cookie': "JSESSIONID=1692D75AD24053A93768D8C212EDD288; _trs_uv=ja7xjh9r_1186_cmc6; _trs_ua_s_1=ja7xjh9r_1186_dajq; _gscu_719616686=11166540rtuice38; _gscs_719616686=11166540zttkjz38|pv:2; _gscbrs_719616686=1",
	# 		# 'connection': "keep-alive",
	# 		# 'cache-control': "no-cache",
	# 		# 'postman-token': "c9e8a3f6-4fdd-203f-cc4d-f6cda6624cb5"
	# 	}
	#
	# 	start_url = "http://search.cnipr.com"
	# 	yield scrapy.Request(start_url, headers=headers)
	#
	# def parse(self, response):
	# 	headers = {
	# 		# 'host': "search.cnipr.com",
	# 		'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
	# 		# 'accept': "*/*",
	# 		# 'accept-language': "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
	# 		# 'accept-encoding': "gzip, deflate",
	# 		# 'referer': "http://search.cnipr.com/search%21doOverviewSearch.action",
	# 		# 'content-type': "application/x-www-form-urlencoded",
	# 		# 'x-requested-with': "XMLHttpRequest",
	# 		# 'content-length': "33",
	# 		# 'cookie': "JSESSIONID=1692D75AD24053A93768D8C212EDD288; _trs_uv=ja7xjh9r_1186_cmc6; _trs_ua_s_1=ja7xjh9r_1186_dajq; _gscu_719616686=11166540rtuice38; _gscs_719616686=11166540zttkjz38|pv:2; _gscbrs_719616686=1",
	# 		# 'connection': "keep-alive",
	# 		# 'cache-control': "no-cache",
	# 		# 'postman-token': "c9e8a3f6-4fdd-203f-cc4d-f6cda6624cb5"
	# 	}
	# 	login_url = 'http://search.cnipr.com/login.action?rd=0.6589196511445976'
	# 	payloads = 'username=mengguiyouziyi&password=3646287'
	# 	yield scrapy.Request(method="POST", url=login_url, body=payloads, callback=self.parse_1, headers=headers)
	#
	# def parse_1(self, response):
	# 	headers = {
	# 		# 'host': "search.cnipr.com",
	# 		# 'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
	# 		# 'accept': "*/*",
	# 		# 'accept-language': "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
	# 		# 'accept-encoding': "gzip, deflate",
	# 		# 'referer': "http://search.cnipr.com/search%21doOverviewSearch.action",
	# 		'content-type': "application/x-www-form-urlencoded",
	# 		# 'x-requested-with': "XMLHttpRequest",
	# 		# 'content-length': "33",
	# 		# 'cookie': "JSESSIONID=1692D75AD24053A93768D8C212EDD288; _trs_uv=ja7xjh9r_1186_cmc6; _trs_ua_s_1=ja7xjh9r_1186_dajq; _gscu_719616686=11166540rtuice38; _gscs_719616686=11166540zttkjz38|pv:2; _gscbrs_719616686=1",
	# 		# 'connection': "keep-alive",
	# 		# 'cache-control': "no-cache",
	# 		# 'postman-token': "c9e8a3f6-4fdd-203f-cc4d-f6cda6624cb5"
	# 	}
	#
	# 	start_url = "http://search.cnipr.com/search%21doOverviewSearch.action"
	# 	f = "strWhere=%E7%94%B3%E8%AF%B7%EF%BC%88%E4%B8%93%E5%88%A9%E6%9D%83%EF%BC%89%E4%BA%BA%3D%28%E4%B8%AD%E5%9B%BD%E7%9F%B3%E6%B2%B9%E5%8C%96%E5%B7%A5%E8%82%A1%E4%BB%BD%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8%29&yuyijs=&start=1&saveFlag=1&limit=10&strSynonymous=&crossLanguage=&islogicsearch=false&saveExp=&showhint=&mpage=null&channelId=FMZL&channelId=SYXX&channelId=WGZL&channelId=FMSQ&channelId=TWZL&channelId=HKPATENT&channelId=USPATENT&channelId=EPPATENT&channelId=JPPATENT&channelId=WOPATENT&channelId=GBPATENT&channelId=CHPATENT&channelId=DEPATENT&channelId=KRPATENT&channelId=FRPATENT&channelId=RUPATENT&channelId=ASPATENT&channelId=ATPATENT&channelId=GCPATENT&channelId=ITPATENT&channelId=AUPATENT&channelId=APPATENT&channelId=CAPATENT&channelId=SEPATENT&channelId=ESPATENT&channelId=OTHERPATENT&trsq=1&dan=1&txt_A=&txt_B=&txt_C=&txt_D=&txt_E=&txt_F=&txt_Q=&txt_R=&txt_I=%E4%B8%AD%E5%9B%BD%E7%9F%B3%E6%B2%B9%E5%8C%96%E5%B7%A5%E8%82%A1%E4%BB%BD%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8&txt_J=&txt_G=&txt_H=&txt_L=&txt_O=&text=&txt_K=&txt_M=&txt_N=&txt_U=&txt_T=&txt_V=&txt_X=&mpage=advsch"
	# 	# formdata = dict([m.split('=') for m in f.split('&')])
	# 	yield scrapy.Request(start_url, method='POST', body=f, headers=headers, callback=self.parse_2)
	#
	# # 	headers = {
	# # 		'host': "search.cnipr.com",
	# # 		'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:57.0) Gecko/20100101 Firefox/57.0",
	# # 		'accept': "*/*",
	# # 		'accept-language': "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
	# # 		'accept-encoding': "gzip, deflate",
	# # 		'referer': "http://search.cnipr.com/login.action",
	# # 		'content-type': "application/x-www-form-urlencoded",
	# # 		'x-requested-with': "XMLHttpRequest",
	# # 		'content-length': "33",
	# # 		# 'cookie': "JSESSIONID=A324C01B7A086473DFBF33DA0071AD2E",
	# # 		'connection': "keep-alive",
	# # 		'cache-control': "no-cache",
	# # 		'postman-token': "b061ecc6-fca0-dcb8-b1da-6439b6f1c07d"
	# # 	}
	# # 	# login_url = 'http://m.cnipr.com:8081/tailor/http://192.168.201.132:8080/login!goonlogin.action?rd=0.3424056342857026'
	# # 	# login_url = 'http://search.cnipr.com/user!gotoLogin.action?forward='
	# # 	login_url = 'http://search.cnipr.com/login.action?rd=0.6589196511445976'
	# # 	# payloads = [
	# # 	# {'username': 'wlglzx', 'password': '!QAZ2wsx'},
	# # 	# {'username': 'mengguiyouziyi', 'password': '3646287'}
	# # 	# ]
	# # 	payloads = {'username': 'mengguiyouziyi', 'password': '3646287'}
	# #
	# # 	cookies = "JSESSIONID=A324C01B7A086473DFBF33DA0071AD2E",
	# # 	cookie_dict = dict((line.split('=') for line in choice(cookies).strip().split(";")))
	# # 	# payloads = 'username=mengguiyouziyi&password=3646287'
	# # 	# yield scrapy.Request(method="POST", url=login_url, body=payloads, callback=self.parse_1, headers=headers)
	# # 	return [scrapy.FormRequest(login_url, formdata=payloads, headers=headers, callback=self.parse_1, cookies=cookie_dict)]
	# #
	# # # cookie_dict = dict(response.cookies.items())
	# # # print('cookie', cookie_dict)
	# # # 	return cookie_dict
	# #
	# # def parse_1(self, response):
	# # 	headers = {
	# # 		'host': "search.cnipr.com",
	# # 		'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:57.0) Gecko/20100101 Firefox/57.0",
	# # 		'accept': "*/*",
	# # 		'accept-language': "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
	# # 		'accept-encoding': "gzip, deflate",
	# # 		'referer': "http://search.cnipr.com/login.action",
	# # 		'content-type': "application/x-www-form-urlencoded",
	# # 		'x-requested-with': "XMLHttpRequest",
	# # 		'content-length': "33",
	# # 		# 'cookie': "JSESSIONID=1692D75AD24053A93768D8C212EDD288; _trs_uv=ja7xjh9r_1186_cmc6; _trs_ua_s_1=ja7xjh9r_1186_dajq; _gscu_719616686=11166540rtuice38; _gscs_719616686=11166540zttkjz38|pv:2; _gscbrs_719616686=1",
	# # 		'connection': "keep-alive",
	# # 		'cache-control': "no-cache",
	# # 		'postman-token': "c9e8a3f6-4fdd-203f-cc4d-f6cda6624cb5"
	# # 	}
	# # 	start_url = "http://search.cnipr.com/search%21doOverviewSearch.action"
	# # 	f = 'strWhere=%E7%94%B3%E8%AF%B7%EF%BC%88%E4%B8%93%E5%88%A9%E6%9D%83%EF%BC%89%E4%BA%BA%3D%28%E4%B8%AD%E5%9B%BD%E7%9F%B3%E6%B2%B9%E5%8C%96%E5%B7%A5%E8%82%A1%E4%BB%BD%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8%29&yuyijs=&start=1&saveFlag=1&limit=10&strSynonymous=&crossLanguage=&islogicsearch=false&saveExp=&showhint=&mpage=null&channelId=FMZL&channelId=SYXX&channelId=WGZL&channelId=FMSQ&channelId=TWZL&channelId=HKPATENT&channelId=USPATENT&channelId=EPPATENT&channelId=JPPATENT&channelId=WOPATENT&channelId=GBPATENT&channelId=CHPATENT&channelId=DEPATENT&channelId=KRPATENT&channelId=FRPATENT&channelId=RUPATENT&channelId=ASPATENT&channelId=ATPATENT&channelId=GCPATENT&channelId=ITPATENT&channelId=AUPATENT&channelId=APPATENT&channelId=CAPATENT&channelId=SEPATENT&channelId=ESPATENT&channelId=OTHERPATENT&trsq=1&dan=1&txt_A=&txt_B=&txt_C=&txt_D=&txt_E=&txt_F=&txt_Q=&txt_R=&txt_I=%E4%B8%AD%E5%9B%BD%E7%9F%B3%E6%B2%B9%E5%8C%96%E5%B7%A5%E8%82%A1%E4%BB%BD%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8&txt_J=&txt_G=&txt_H=&txt_L=&txt_O=&text=&txt_K=&txt_M=&txt_N=&txt_U=&txt_T=&txt_V=&txt_X=&mpage=advsch'
	# # 	# formdata = dict([m.split('=') for m in f.split('&')])
	# # 	yield scrapy.Request(start_url, method='POST', body=f, callback=self.parse_login, headers=headers)
	# #
	# def parse_2(self, response):
	# 	with open('list.html', 'w') as f:
	# 		f.writelines(response.text)
