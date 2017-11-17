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
	custom_settings = {
		'DEFAULT_REQUEST_HEADERS': {
			'origin': "http://search.cnipr.com",
			'x-devtools-emulate-network-conditions-client-id': "3453ed57-0010-4d33-b890-5baa0b0e0088",
			'upgrade-insecure-requests': "1",
			'content-type': "application/x-www-form-urlencoded",
			'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
			'referer': "http://search.cnipr.com/pages!advSearch.action",
			'accept-encoding': "gzip, deflate",
			'accept-language': "zh-CN,zh;q=0.8",
			'cache-control': "no-cache",
			'postman-token': "a7c276c9-00c8-f51b-0ccd-325e41a05cbd"
		},
		'USER_AGENT_CHOICES': [
			'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0_3 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Mobile/15A432',
			# 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
			# 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
			# 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
			# 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; InfoPath.3; rv:11.0) like Gecko',
			# 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;',
			# 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;',
			# 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
			# 'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
			# 'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11',
			# 'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11',
			# 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
			# 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)',
			# 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)',
			# 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
			# 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)',
			# 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)',
			# 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)',
			# 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser)',
			# 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
			# "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
			# "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
			# "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
			# "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
			# "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
			# "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
			# "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
			# "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
			# "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
			# "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
			# "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
			# "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
			# "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
			# "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
			# "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
			# "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
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
		# c = self.login()
		# cookies = "yunsuo_session_verify=450304a51a18108086355b1d67d81ee2; checkedwords=0%2C1%2C2%2C3%2C4; searchcol=%u7533%u8BF7%uFF08%u4E13%u5229%u6743%uFF09%u4EBA; yunsuo_session_verify=450304a51a18108086355b1d67d81ee2; _ubm_ref.jEVZOqlU=%5B%22%22%2C%22%22%2C1510214249%2C%22http%3A%2F%2Fsearch.cnipr.com%2Fpages!advSearch.action%22%5D; _ubm_id.jEVZOqlU=5dbeb122d94854a8; _ubm_ses.jEVZOqlU=*; _gscu_719616686=0950182114s1dh12; _gscs_719616686=t10195927cruhrz13|pv:14; _gscbrs_719616686=1; _trs_uv=j9geerzw_1186_brj5; searchtype=2; _ubm_ref.jEVZOqlU=%5B%22%22%2C%22%22%2C1510379379%2C%22http%3A%2F%2Fsearch.cnipr.com%2Fpages!advSearch.action%22%5D; _ubm_id.jEVZOqlU=5dbeb122d94854a8; JSESSIONID=8EEA2DA98B5DD3B141948502A7D4B56F; advchannel=FMZL%2CSYXX%2CWGZL%2CFMSQ%2CTWZL%2CHKPATENT%2CUSPATENT%2CEPPATENT%2CJPPATENT%2CWOPATENT%2CGBPATENT%2CCHPATENT%2CDEPATENT%2CKRPATENT%2CFRPATENT%2CRUPATENT%2CASPATENT%2CATPATENT%2CGCPATENT%2CITPATENT%2CAUPATENT%2CAPPATENT%2CCAPATENT%2CSEPATENT%2CESPATENT%2COTHERPATENT; _trs_uv=j9geerzw_1186_brj5; _trs_ua_s_1=ja0ub157_1186_i0o0; _gscu_719616686=0950182114s1dh12; _gscs_719616686=t10195927cruhrz13|pv:22; _gscbrs_719616686=1",
		# self.cookie_dict = dict((line.split('=') for line in choice(cookies).strip().split(";")))
		# self.cookie_dict.update(c)
		self.cookie_dict = self.login()

	def login(self):
		cookies = 'yunsuo_session_verify=450304a51a18108086355b1d67d81ee2; checkedwords=0%2C1%2C2%2C3%2C4; searchcol=%u7533%u8BF7%uFF08%u4E13%u5229%u6743%uFF09%u4EBA; yunsuo_session_verify=450304a51a18108086355b1d67d81ee2; _ubm_ref.jEVZOqlU=%5B%22%22%2C%22%22%2C1510214249%2C%22http%3A%2F%2Fsearch.cnipr.com%2Fpages!advSearch.action%22%5D; _ubm_id.jEVZOqlU=5dbeb122d94854a8; _ubm_ses.jEVZOqlU=*; _gscu_719616686=0950182114s1dh12; _gscs_719616686=t10195927cruhrz13|pv:14; _gscbrs_719616686=1; _trs_uv=j9geerzw_1186_brj5; searchtype=2; _ubm_ref.jEVZOqlU=%5B%22%22%2C%22%22%2C1510379379%2C%22http%3A%2F%2Fsearch.cnipr.com%2Fpages!advSearch.action%22%5D; _ubm_id.jEVZOqlU=5dbeb122d94854a8; JSESSIONID=8EEA2DA98B5DD3B141948502A7D4B56F; advchannel=FMZL%2CSYXX%2CWGZL%2CFMSQ%2CTWZL%2CHKPATENT%2CUSPATENT%2CEPPATENT%2CJPPATENT%2CWOPATENT%2CGBPATENT%2CCHPATENT%2CDEPATENT%2CKRPATENT%2CFRPATENT%2CRUPATENT%2CASPATENT%2CATPATENT%2CGCPATENT%2CITPATENT%2CAUPATENT%2CAPPATENT%2CCAPATENT%2CSEPATENT%2CESPATENT%2COTHERPATENT; _gscu_719616686=0950182114s1dh12; _gscs_719616686=t10195927cruhrz13|pv:23; _gscbrs_719616686=1; _trs_uv=j9geerzw_1186_brj5; _trs_ua_s_1=ja0ub157_1186_i0o0'
		cookie_dict = dict((line.split('=') for line in choice(cookies).strip().split(";")))
		login_url = 'http://search.cnipr.com/login.action?rd=0.4289715556717164'
		payloads = [
			# {'username': 'wlglzx', 'password': '!QAZ2wsx'},
			{'username': 'mengguiyouziyi', 'password': '3646287'}
		]
		response = requests.request("POST", login_url, headers=self.headers, data=choice(payloads), cookies=cookie_dict)
		cookie_dict = dict(response.cookies.items())
		print('cookie', cookie_dict)
		return cookie_dict

	# def login(self):
	# 	# login_url = 'http://m.cnipr.com:8081/tailor/http://192.168.201.132:8080/login!goonlogin.action?rd=0.3424056342857026'
	# 	# login_url = 'http://search.cnipr.com/user!gotoLogin.action?forward='
	# 	login_url = 'http://search.cnipr.com/login.action?rd=0.4289715556717164'
	# 	payloads = [
	# 		# {'username': 'wlglzx', 'password': '!QAZ2wsx'},
	# 		{'username': 'mengguiyouziyi', 'password': '3646287'}
	# 	]
	# 	response = requests.request("POST", login_url, headers=self.headers, data=choice(payloads))
	# 	cookie_dict = dict(response.cookies.items())
	# 	print('cookie', cookie_dict)
	# 	return cookie_dict

	def start_requests(self):
		start_url = "http://search.cnipr.com/search%21doOverviewSearch.action"
		f = 'strWhere=%E7%94%B3%E8%AF%B7%EF%BC%88%E4%B8%93%E5%88%A9%E6%9D%83%EF%BC%89%E4%BA%BA%3D%28%E4%B8%AD%E5%9B%BD%E7%9F%B3%E6%B2%B9%E5%8C%96%E5%B7%A5%E8%82%A1%E4%BB%BD%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8%29&yuyijs=&start=1&saveFlag=1&limit=10&strSynonymous=&crossLanguage=&islogicsearch=false&saveExp=&showhint=&mpage=null&channelId=FMZL&channelId=SYXX&channelId=WGZL&channelId=FMSQ&channelId=TWZL&channelId=HKPATENT&channelId=USPATENT&channelId=EPPATENT&channelId=JPPATENT&channelId=WOPATENT&channelId=GBPATENT&channelId=CHPATENT&channelId=DEPATENT&channelId=KRPATENT&channelId=FRPATENT&channelId=RUPATENT&channelId=ASPATENT&channelId=ATPATENT&channelId=GCPATENT&channelId=ITPATENT&channelId=AUPATENT&channelId=APPATENT&channelId=CAPATENT&channelId=SEPATENT&channelId=ESPATENT&channelId=OTHERPATENT&trsq=1&dan=1&txt_A=&txt_B=&txt_C=&txt_D=&txt_E=&txt_F=&txt_Q=&txt_R=&txt_I=%E4%B8%AD%E5%9B%BD%E7%9F%B3%E6%B2%B9%E5%8C%96%E5%B7%A5%E8%82%A1%E4%BB%BD%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8&txt_J=&txt_G=&txt_H=&txt_L=&txt_O=&text=&txt_K=&txt_M=&txt_N=&txt_U=&txt_T=&txt_V=&txt_X=&mpage=advsch'
		# formdata = dict([m.split('=') for m in f.split('&')])
		yield scrapy.Request(start_url, method='POST', body=f, cookies=self.cookie_dict)

	def parse(self, response):
		with open('list.html', 'w') as f:
			f.writelines(response.text)
		print(response.text)
