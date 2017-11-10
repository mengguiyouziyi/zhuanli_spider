# -*- coding: utf-8 -*-
import scrapy
from random import choice
from urllib.parse import urljoin
from scrapy.selector import Selector
from cnipr.items import CniprItem


# from cnipr.utils.bloomfilter import rc


class TouzishijianSpider(scrapy.Spider):
	name = 'zhuanl'
	custom_settings = {
		'DEFAULT_REQUEST_HEADERS': {
			'origin': "http://search.cnipr.com",
			'x-devtools-emulate-network-conditions-client-id': "3453ed57-0010-4d33-b890-5baa0b0e0088",
			'upgrade-insecure-requests': "1",
			# 'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36",
			'content-type': "application/x-www-form-urlencoded",
			'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
			'referer': "http://search.cnipr.com/pages!advSearch.action",
			'accept-encoding': "gzip, deflate",
			'accept-language': "zh-CN,zh;q=0.8",
			# 'cookie': "checkedwords=0%2C1%2C2%2C3%2C4; advchannel=FMZL%2CSYXX%2CWGZL%2CFMSQ%2CTWZL%2CHKPATENT%2CUSPATENT%2CEPPATENT%2CJPPATENT%2CWOPATENT%2CGBPATENT%2CCHPATENT%2CDEPATENT%2CKRPATENT%2CFRPATENT%2CRUPATENT%2CASPATENT%2CATPATENT%2CGCPATENT%2CITPATENT%2CAUPATENT%2CAPPATENT%2CCAPATENT%2CSEPATENT%2CESPATENT%2COTHERPATENT; JSESSIONID=E01845BD9F2004DFC729DB303A324CC0; cniprAutoLogin=mengguiyouziyi%7C3646287; _gscu_719616686=0950182114s1dh12; _gscs_719616686=t10195927cruhrz13|pv:5; _gscbrs_719616686=1; _trs_uv=j9geerzw_1186_brj5; _trs_ua_s_1=j9rvnveo_1186_b9tl",
			# 'cookie': "yunsuo_session_verify=450304a51a18108086355b1d67d81ee2; _ubm_ref.jEVZOqlU=%5B%22%22%2C%22%22%2C1510214249%2C%22http%3A%2F%2Fsearch.cnipr.com%2Fpages!advSearch.action%22%5D; _ubm_id.jEVZOqlU=5dbeb122d94854a8; checkedwords=0%2C1%2C2%2C3%2C4; advchannel=FMZL%2CSYXX%2CWGZL%2CFMSQ%2CTWZL%2CHKPATENT%2CUSPATENT%2CEPPATENT%2CJPPATENT%2CWOPATENT%2CGBPATENT%2CCHPATENT%2CDEPATENT%2CKRPATENT%2CFRPATENT%2CRUPATENT%2CASPATENT%2CATPATENT%2CGCPATENT%2CITPATENT%2CAUPATENT%2CAPPATENT%2CCAPATENT%2CSEPATENT%2CESPATENT%2COTHERPATENT; searchcol=%u7533%u8BF7%uFF08%u4E13%u5229%u6743%uFF09%u4EBA; yunsuo_session_verify=450304a51a18108086355b1d67d81ee2; _ubm_ref.jEVZOqlU=%5B%22%22%2C%22%22%2C1510214249%2C%22http%3A%2F%2Fsearch.cnipr.com%2Fpages!advSearch.action%22%5D; _ubm_id.jEVZOqlU=5dbeb122d94854a8; _ubm_ses.jEVZOqlU=*; _gscu_719616686=0950182114s1dh12; _gscs_719616686=t10195927cruhrz13|pv:14; _gscbrs_719616686=1; _trs_uv=j9geerzw_1186_brj5; _gscu_719616686=0950182114s1dh12; _gscbrs_719616686=1; _trs_uv=j9geerzw_1186_brj5; JSESSIONID=85855B60771EC5F937770982B5B26331",
			'cache-control': "no-cache",
			'postman-token': "a7c276c9-00c8-f51b-0ccd-325e41a05cbd"
		}
	}
	cookies = "yunsuo_session_verify=450304a51a18108086355b1d67d81ee2; _ubm_ref.jEVZOqlU=%5B%22%22%2C%22%22%2C1510214249%2C%22http%3A%2F%2Fsearch.cnipr.com%2Fpages!advSearch.action%22%5D; _ubm_id.jEVZOqlU=5dbeb122d94854a8; checkedwords=0%2C1%2C2%2C3%2C4; advchannel=FMZL%2CSYXX%2CWGZL%2CFMSQ%2CTWZL%2CHKPATENT%2CUSPATENT%2CEPPATENT%2CJPPATENT%2CWOPATENT%2CGBPATENT%2CCHPATENT%2CDEPATENT%2CKRPATENT%2CFRPATENT%2CRUPATENT%2CASPATENT%2CATPATENT%2CGCPATENT%2CITPATENT%2CAUPATENT%2CAPPATENT%2CCAPATENT%2CSEPATENT%2CESPATENT%2COTHERPATENT; searchcol=%u7533%u8BF7%uFF08%u4E13%u5229%u6743%uFF09%u4EBA; yunsuo_session_verify=450304a51a18108086355b1d67d81ee2; _ubm_ref.jEVZOqlU=%5B%22%22%2C%22%22%2C1510214249%2C%22http%3A%2F%2Fsearch.cnipr.com%2Fpages!advSearch.action%22%5D; _ubm_id.jEVZOqlU=5dbeb122d94854a8; _ubm_ses.jEVZOqlU=*; _gscu_719616686=0950182114s1dh12; _gscs_719616686=t10195927cruhrz13|pv:14; _gscbrs_719616686=1; _trs_uv=j9geerzw_1186_brj5; JSESSIONID=85855B60771EC5F937770982B5B26331; _gscu_719616686=0950182114s1dh12; _gscs_719616686=t10195927cruhrz13|pv:20; _gscbrs_719616686=1; _trs_uv=j9geerzw_1186_brj5; _trs_ua_s_1=j9sc0g06_1186_k5zc",
	cookie_dict = dict((line.split('=') for line in choice(cookies).strip().split(";")))

	def start_requests(self):
		start_url = "http://search.cnipr.com/search%21doOverviewSearch.action"
		f = 'strWhere=%E7%94%B3%E8%AF%B7%EF%BC%88%E4%B8%93%E5%88%A9%E6%9D%83%EF%BC%89%E4%BA%BA%3D%28%E4%B8%AD%E5%9B%BD%E7%9F%B3%E6%B2%B9%E5%8C%96%E5%B7%A5%E8%82%A1%E4%BB%BD%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8%29&yuyijs=&start=1&saveFlag=1&limit=10&strSynonymous=&crossLanguage=&islogicsearch=false&saveExp=&showhint=&mpage=null&channelId=FMZL&channelId=SYXX&channelId=WGZL&channelId=FMSQ&channelId=TWZL&channelId=HKPATENT&channelId=USPATENT&channelId=EPPATENT&channelId=JPPATENT&channelId=WOPATENT&channelId=GBPATENT&channelId=CHPATENT&channelId=DEPATENT&channelId=KRPATENT&channelId=FRPATENT&channelId=RUPATENT&channelId=ASPATENT&channelId=ATPATENT&channelId=GCPATENT&channelId=ITPATENT&channelId=AUPATENT&channelId=APPATENT&channelId=CAPATENT&channelId=SEPATENT&channelId=ESPATENT&channelId=OTHERPATENT&trsq=1&dan=1&txt_A=&txt_B=&txt_C=&txt_D=&txt_E=&txt_F=&txt_Q=&txt_R=&txt_I=%E4%B8%AD%E5%9B%BD%E7%9F%B3%E6%B2%B9%E5%8C%96%E5%B7%A5%E8%82%A1%E4%BB%BD%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8&txt_J=&txt_G=&txt_H=&txt_L=&txt_O=&text=&txt_K=&txt_M=&txt_N=&txt_U=&txt_T=&txt_V=&txt_X=&mpage=advsch'
		# formdata = dict([m.split('=') for m in f.split('&')])
		yield scrapy.Request(start_url, method='POST', body=f, cookies=self.cookie_dict)

	def parse(self, response):
		print(response.text)

	# select = Selector(text=response.text)
	# print(response.url)




