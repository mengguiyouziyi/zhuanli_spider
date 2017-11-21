# -*- coding: utf-8 -*-
import scrapy
import time
import json
from random import random
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from cnipr.items import CniprItem


class TouzishijianSpider(scrapy.Spider):
	name = 'cnipr_selenium'
	headers = {
		# 'host': "search.cnipr.com",
		# 'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
		# 'accept': "*/*",
		# 'accept-language': "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
		# 'accept-encoding': "gzip, deflate",
		# 'referer': "http://search.cnipr.com/search%21doOverviewSearch.action",
		'content-type': "application/x-www-form-urlencoded",
		# 'x-requested-with': "XMLHttpRequest",
		# 'content-length': "33",
		# 'cookie': "JSESSIONID=1692D75AD24053A93768D8C212EDD288; _trs_uv=ja7xjh9r_1186_cmc6; _trs_ua_s_1=ja7xjh9r_1186_dajq; _gscu_719616686=11166540rtuice38; _gscs_719616686=11166540zttkjz38|pv:2; _gscbrs_719616686=1",
		# 'connection': "keep-alive",
		# 'cache-control': "no-cache",
	}

	def __init__(self):
		self.sources = 'FMZL,SYXX,WGZL,FMSQ,TWZL,HKPATENT,USPATENT,EPPATENT,JPPATENT,WOPATENT,GBPATENT,CHPATENT,DEPATENT,KRPATENT,FRPATENT,RUPATENT,ASPATENT,ATPATENT,GCPATENT,ITPATENT,AUPATENT,APPATENT,CAPATENT,SEPATENT,ESPATENT,OTHERPATENT'
		self.browser = webdriver.Chrome(
			executable_path='/Users/menggui/.pyenv/versions/Anaconda3-4.3.0/bin/chromedriver')
		self.cookie_dict = self.login()

	def login(self):
		self.browser.get('http://search.cnipr.com/login.action')
		self.browser.find_element_by_name('username').send_keys('mengguiyouziyi')
		self.browser.find_element_by_name('password').send_keys('3646287')
		self.browser.find_element_by_xpath('//input[@type="submit"]').click()
		time.sleep(1)
		Alert(self.browser).accept()
		time.sleep(1)
		# self.browser.get('http://search.cnipr.com/pages!advSearch.action')
		# time.sleep(1)
		# self.browser.find_element_by_id('txt_I').send_keys('中国石油化工股份有限公司')
		# self.browser.execute_script("window.scrollTo(document.body.scrollWidth, document.body.scrollHeight)")
		# self.browser.find_element_by_class_name('a2').click()
		# time.sleep(2)
		# print(self.browser.get_cookies())
		cookie_list = self.browser.get_cookies()
		self.browser.quit()
		cookie_dict = {v['name']: v['value'] for v in cookie_list}
		return cookie_dict

	def start_requests(self):
		# start_url = "http://search.cnipr.com/search%21doOverviewSearch.action"
		# f = "strWhere=%E7%94%B3%E8%AF%B7%EF%BC%88%E4%B8%93%E5%88%A9%E6%9D%83%EF%BC%89%E4%BA%BA%3D%28%E4%B8%AD%E5%9B%BD%E7%9F%B3%E6%B2%B9%E5%8C%96%E5%B7%A5%E8%82%A1%E4%BB%BD%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8%29&yuyijs=&start=1&saveFlag=1&limit=10&strSynonymous=&crossLanguage=&islogicsearch=false&saveExp=&showhint=&mpage=null&channelId=FMZL&channelId=SYXX&channelId=WGZL&channelId=FMSQ&channelId=TWZL&channelId=HKPATENT&channelId=USPATENT&channelId=EPPATENT&channelId=JPPATENT&channelId=WOPATENT&channelId=GBPATENT&channelId=CHPATENT&channelId=DEPATENT&channelId=KRPATENT&channelId=FRPATENT&channelId=RUPATENT&channelId=ASPATENT&channelId=ATPATENT&channelId=GCPATENT&channelId=ITPATENT&channelId=AUPATENT&channelId=APPATENT&channelId=CAPATENT&channelId=SEPATENT&channelId=ESPATENT&channelId=OTHERPATENT&trsq=1&dan=1&txt_A=&txt_B=&txt_C=&txt_D=&txt_E=&txt_F=&txt_Q=&txt_R=&txt_I=%E4%B8%AD%E5%9B%BD%E7%9F%B3%E6%B2%B9%E5%8C%96%E5%B7%A5%E8%82%A1%E4%BB%BD%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8&txt_J=&txt_G=&txt_H=&txt_L=&txt_O=&text=&txt_K=&txt_M=&txt_N=&txt_U=&txt_T=&txt_V=&txt_X=&mpage=advsch"
		# yield scrapy.Request(start_url, method='POST', body=f, headers=headers, cookies=self.cookie_dict)
		# f_2 = "wgViewmodle=&strWhere=%E7%94%B3%E8%AF%B7%EF%BC%88%E4%B8%93%E5%88%A9%E6%9D%83%EF%BC%89%E4%BA%BA%3D%28%E4%B8%AD%E5%9B%BD%E7%9F%B3%E6%B2%B9%E5%8C%96%E5%B7%A5%E8%82%A1%E4%BB%BD%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8%29&start=2&limit=10&option=2&iHitPointType=115&strSortMethod=RELEVANCE&strSources=FMZL%2CSYXX%2CWGZL%2CFMSQ%2CTWZL%2CHKPATENT%2CUSPATENT%2CEPPATENT%2CJPPATENT%2CWOPATENT%2CGBPATENT%2CCHPATENT%2CDEPATENT%2CKRPATENT%2CFRPATENT%2CRUPATENT%2CASPATENT%2CATPATENT%2CGCPATENT%2CITPATENT%2CAUPATENT%2CAPPATENT%2CCAPATENT%2CSEPATENT%2CESPATENT%2COTHERPATENT&strSynonymous=&yuyijs=&filterChannel=&keyword2Save=&key2Save=&forward=&otherWhere=&username=&password="
		# yield scrapy.Request(start_url, method='POST', body=f_2, headers=headers, cookies=self.cookie_dict, callback=self.parse_2)
		gongkai_url = 'http://search.cnipr.com/search!doDetailSearch.action'
		# gongkai = 'strWhere=%(where)s&start=%(start)s&recordCursor=%(cursor)s&limit=1&option=2&iHitPointType=115&strSortMethod=RELEVANCE&strSources=%(sources)s&strSynonymous=&yuyijs=&filterChannel=&otherWhere=' % {
		# 	'where': '申请（专利权）人=(中国石油化工股份有限公司)',
		# 	'sources': self.sources,
		# 	'start': '1',
		# 	'cursor': '0',
		# }
		gongkai = 'strWhere=%(where)s&recordCursor=%(cursor)s&iOption=&iHitPointType=115&strSortMethod=RELEVANCE&strSources=%(sources)s&strSynonymous=&yuyijs=&otherWhere=&gotolight=' % {
			'where': '申请（专利权）人=(中国石油化工股份有限公司)',
			'sources': self.sources,
			'cursor': '0',
		}
		yield scrapy.Request(gongkai_url, method='POST', body=gongkai, headers=self.headers, cookies=self.cookie_dict,
		                     callback=self.parse)

	def parse(self, response):
		"""公开信息"""
		select = scrapy.Selector(text=response.text)
		# p_sum = select.xpath('//div[@class="n_page"]/span[2]').extract_first()
		familyid = select.xpath('//input[@id="familyid"]/@value').extract_first()  # 70054101
		paramAn = select.xpath('//input[@id="paramAn"]/@value').extract_first()  # CN201310571770.7  申请(专利)号
		paramPn = select.xpath('//input[@id="paramPn"]/@value').extract_first()  # CN104636980A  申请公布号
		paramPd = select.xpath('//input[@id="paramPd"]/@value').extract_first()  # 2015.05.20  公开公告日
		paramCount = select.xpath('//input[@id="paramCount"]/@value').extract_first()  # 53434  专利数量
		paramDB = select.xpath('//input[@id="paramDB"]/@value').extract_first()  # FMZL  专利类型
		paramPages = select.xpath('//input[@id="paramPages"]/@value').extract_first()  # 10  pdf页数
		sysid = select.xpath('//input[@id="sysid"]/@value').extract_first()  # 8901760804FBA43E4F27BA92E0081C56
		appid = select.xpath('//input[@id="appid"]/@value').extract_first()  # 201310571770.7

		title = select.xpath('//div[@class="nc_left"]/h3').extract_first()
		abs = select.xpath('//div[@class="nc_left"]/p[1]').extract_first()
		zhuquan = select.xpath('//div[@class="nc_left"]/p[2]').extract_first()  # 主权项

		applicatDate = ''
		mainClassNum = ''
		classNum = ''
		rightHolder = ''
		inventDesigner = ''
		addr = ''
		countryCode = ''
		agency = ''
		agent = ''
		priority = ''
		internatApply = ''
		internatPub = ''
		entryDate = ''
		caseApplyNum = ''
		sameDayApply = ''
		tr_tags = select.xpath('//div[@class="nc_right"]／table/tr')
		for tr in tr_tags:
			text = tr.xpath('./td[@class="tit"]/text()').extract()
			text = ''.join(text) if text else ''
			auxs = tr.xpath('./td/span/text()').extract()
			aux = ';'.join(aux) if auxs else ''
			atexts = tr.xpath('./td/a/text()').extract()
			atext = ';'.join(atexts) if atexts else ''
			tdtexts = tr.xpath('./td[2]/text()').extract()
			tdtext = ''.join(tdtexts) if tdtexts else ''

			if '申请日' in text:
				applicatDate = aux
			elif '主分类号' in text:
				mainClassNum = aux
			elif '分类号' in text and '主' not in text:
				classNum = aux
			elif '申请权利人' in text:
				rightHolder = atext
			elif '发明设计人' in text:
				inventDesigner = atext
			elif '地址' in text:
				addr = tdtext
			elif '国省代码' in text:
				countryCode = tdtext
			elif '代理机构' in text:
				agency = tdtext
			elif '代理人' in text:
				agent = tdtext
			elif '优先权' in text:
				priority = tdtext
			elif '国际申请' in text:
				internatApply = tdtext
			elif '国际公布' in text:
				internatPub = tdtext
			elif '进入国家日期' in text:
				entryDate = tdtext
			elif '分案原申请号' in text:
				caseApplyNum = aux
			elif '同日申请' in text:
				sameDayApply = aux
		item = CniprItem()
		item['familyid'] = familyid
		item['paramAn'] = paramAn
		item['paramPn'] = paramPn
		item['paramPd'] = paramPd
		item['paramCount'] = paramCount
		item['paramDB'] = paramDB
		item['paramPages'] = paramPages
		item['sysid'] = sysid
		item['appid'] = appid
		item['title'] = title
		item['abs'] = abs
		item['zhuquan'] = zhuquan
		item['applicatDate'] = applicatDate
		item['mainClassNum'] = mainClassNum
		item['classNum'] = classNum
		item['rightHolder'] = rightHolder
		item['inventDesigner'] = inventDesigner
		item['addr'] = addr
		item['countryCode'] = countryCode
		item['agency'] = agency
		item['agent'] = agent
		item['priority'] = priority
		item['internatApply'] = internatApply
		item['internatPub'] = internatPub
		item['entryDate'] = entryDate
		item['caseApplyNum'] = caseApplyNum
		item['sameDayApply'] = sameDayApply

		shouquan_url = 'http://search.cnipr.com/search!viewDetail.action'
		shouquan = 'an=%(an)s&allsources=%(sources)s&strSources=%(strSources)s' % {
			'an': paramAn,
			'sources': self.sources,
			'strSources': paramDB
		}
		yield scrapy.Request(shouquan_url, method='POST', body=shouquan, headers=self.headers, cookies=self.cookie_dict,
		                     callback=self.parse_shouquan, meta={'item': item})

	def parse_shouquan(self, response):
		"""授权信息"""
		item = response.meta.get('item')
		paramAn = item['paramAn']
		select = scrapy.Selector(text=response.text)
		paramPn_shouq = select.xpath('//input[@id="paramPn"]/@value').extract_first()  # CN104174429B  授权公布号
		paramPd_shouq = select.xpath('//input[@id="paramPd"]/@value').extract_first()  # 2017.08.25  授权公告日
		item['paramPn_shouq'] = paramPn_shouq
		item['paramPd_shouq'] = paramPd_shouq

		legal_url = 'http://search.cnipr.com/search!doLegalSearchByAn.action?rd=%(rd)s&strAn=%(strAn)s' % {
			'rd': random(),
			'strAn': paramAn
		}
		yield scrapy.Request(legal_url, headers=self.headers, cookies=self.cookie_dict, callback=self.legal,
		                     meta={'item': item})

	def legal(self, response):
		"""法律状态"""
		item = response.meta.get('item')
		paramPn = item['paramPn']
		text = json.loads(response.text)
		listLegalInfo = text.get('listLegalInfo')  # dict，是不是可以直接json dumps？
		item['listLegalInfo'] = str(listLegalInfo)
		# for legalInfo in listLegalInfo:
		# 	strAn = legalInfo.get('strAn')  # CN201310520601.0
		# 	strLegalStatus = legalInfo.get('strLegalStatus')  # 授权
		# 	strLegalStatusDay = legalInfo.get('strLegalStatusDay')  # 2017.11.03
		# 	strStatusInfo = legalInfo.get('strStatusInfo')  # 授权<br/>
		# 	uuid = legalInfo.get('uuid')  # 771E3EDE77934849A91F94B97C4ED116

		cnReference_url = 'http://search.cnipr.com/reference!getCnReference.action?rd=%(rd)s&patnum=%(patnum)s' % {
			'rd': random(),
			'patnum': paramPn
		}
		yield scrapy.Request(cnReference_url, headers=self.headers, cookies=self.cookie_dict, callback=self.cnReference,
		                     meta={'item': item})

	def cnReference(self, response):
		"""引证文献"""
		item = response.meta.get('item')
		paramAn = item['paramAn']
		paramPd = item['paramPd']
		paramDB = item['paramDB']

		text = json.loads(response.text)
		dto = text.get('dto')
		sqryzzlList = dto.get('sqryzzlList') if dto else []
		item['sqryzzlList'] = str(sqryzzlList)

		quanli_url = 'http://search.cnipr.com/loaddata!loadXml.action?rd=%(rd)s&an=%(an)s&strSource=%(strSource)s&pd=%(pd)s&xmltype=CLM' % {
			'rd': random(),
			'an': paramAn,
			'strSource': paramDB,
			'pd': paramPd,
		}
		yield scrapy.Request(quanli_url, headers=self.headers, cookies=self.cookie_dict, callback=self.quanli,
		                     meta={'item': item})

	def quanli(self, response):
		"""权利要求书"""
		item = response.meta.get('item')
		paramAn = item['paramAn']
		paramPd = item['paramPd']
		paramDB = item['paramDB']
		text = json.loads(response.text)
		xml = text.get('xml')
		item['claim'] = xml
		# select = scrapy.Selector(text=xml)
		# claim_tags = select.xpath('//claim')
		# claim_list = []
		# for tag in claim_tags:
		# 	one = tag.xpath('.//text()').extract()
		# 	one = ''.join([o.strip() for o in one if o]) if one else ''
		# 	claim_list.append(one)
		# item['claim_list'] = str(claim_list)

		shuoming_url = 'http://search.cnipr.com/loaddata!loadXml.action?rd=%(rd)s&an=%(an)s&strSource=%(strSource)s&pd=%(pd)s&xmltype=DES' % {
			'rd': random(),
			'an': paramAn,
			'strSource': paramDB,
			'pd': paramPd,
		}
		yield scrapy.Request(shuoming_url, headers=self.headers, cookies=self.cookie_dict, callback=self.shuoming,
		                     meta={'item': item})

	def shuoming(self, response):
		"""说明书"""
		item = response.meta.get('item')
		familyid = item['familyid']
		text = json.loads(response.text)
		xml = text.get('xml')
		item['description'] = xml

		patentList_url = 'http://search.cnipr.com/wordtips!familyPatentSearch.action?rd=%(rd)s&an=%(an)s' % {
			'rd': random(),
			'an': familyid
		}
		yield scrapy.Request(patentList_url, headers=self.headers, cookies=self.cookie_dict, callback=self.patentList,
		                     meta={'item': item})

	def patentList(self, response):
		"""同族专利"""
		item = response.meta.get('item')
		text = json.loads(response.text)
		patentList = text.get('patentList')
		item['patentList'] = str(patentList)
		yield item
