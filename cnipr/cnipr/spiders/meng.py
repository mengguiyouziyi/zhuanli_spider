# -*- coding: utf-8 -*-
import scrapy
import requests
import json, time
from random import random
from urllib.parse import urljoin
from cnipr.items import CniprItem
from util.info import startup_nodes, user_dict
from rediscluster import StrictRedisCluster
from scrapy.exceptions import CloseSpider


class TouzishijianSpider(scrapy.Spider):
	name = 'meng'
	custom_settings = {
		'DEFAULT_REQUEST_HEADERS': {
			'content-type': "application/x-www-form-urlencoded",
		},
	}
	proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
		"host": "http-cla.abuyun.com",
		"port": "9030",
		"user": "H5JQ2D5J51RO184C",
		"pass": "ED5CACF63DA1A566",
	}
	proxies = {
		"http": proxyMeta,
		"https": proxyMeta,
	}

	def __init__(self):
		self.sources = 'FMZL,SYXX,WGZL,FMSQ,TWZL,HKPATENT,USPATENT,EPPATENT,JPPATENT,WOPATENT,GBPATENT,CHPATENT,DEPATENT,KRPATENT,FRPATENT,RUPATENT,ASPATENT,ATPATENT,GCPATENT,ITPATENT,AUPATENT,APPATENT,CAPATENT,SEPATENT,ESPATENT,OTHERPATENT'
		self.rc = StrictRedisCluster(startup_nodes=startup_nodes, decode_responses=True)
		self.user = user_dict['mengguiyouziyi']
		self.cookie_dict = self.login()
		print(self.cookie_dict)

	def login(self):
		login_url = 'http://search.cnipr.com/login.action?rd={}'.format(random())
		# payloads = 'username=mengguiyouziyi&password=3646287'
		print(self.user)
		response = requests.request("POST", login_url, data=self.user)
		j_res = response.json()
		print(response.text)
		if j_res.get('msg') == 'alreadylogin':
			print('alreadylogin.....')
			goonlogin_url = 'http://search.cnipr.com/login!goonlogin.action?rd={}'.format(random())
			response = requests.request("POST", goonlogin_url, data=self.user)
		print(response.text)
		cookie_dict = dict(response.cookies.items())
		return cookie_dict

	def start_requests(self):
		while True:
			comp = self.rc.rpop('cnipr_comp')
			if not comp:
				raise CloseSpider('no datas')
			# comps = [
			# 	'1~10347203625134653463~国家电网公司',
			# 	'2~15251839184792798233~华为技术有限公司',
			# 	'3~ad~中兴通讯股份有限公司',
			# 	'4~sdf~三星电子株式会社',
			# 	'4~sdf~松下电器产业株式会社',
			# 	'4~sdf~浙江大学',
			# 	'4~sdf~中国石油化工股份有限公司',
			# 	'4~sdf~鸿海精密工业股份有限公司',
			# 	'4~sdf~清华大学',
			# 	'4~sdf~东南大学',
			# 	'4~sdf~上海交通大学',
			# 	'4~sdf~鸿富锦精密工业(深圳)有限公司',
			# 	'4~sdf~中国石油大学(华东)',
			# 	'4~sdf~佳能株式会社',
			# ]
			# for comp in comps:
			# comp = '1~10347203625134653463~国家电网公司'
			v_l = comp.split('~')
			origin_id = v_l[0]
			only_id = v_l[1]
			comp_full_name = v_l[2]
			item = CniprItem()
			gongkai_url = 'http://search.cnipr.com/search!doDetailSearch.action'
			gongkai = 'strWhere=%(where)s&recordCursor=%(cursor)s&iOption=&iHitPointType=115&strSortMethod=RELEVANCE&strSources=%(sources)s&strSynonymous=&yuyijs=&otherWhere=&gotolight=' % {
				'where': '申请（专利权）人=(%s)' % self._hanBracket(comp_full_name),
				'sources': self.sources,
				'cursor': '0',
			}
			item['origin_id'] = origin_id
			item['only_id'] = only_id
			item['comp_full_name'] = comp_full_name
			item['cursorPage'] = '0'
			item['tifvalue'] = ''
			item['xmlvalue'] = ''
			item['pdfvalue'] = ''
			item['pdfvalue2'] = ''
			item['patentStatus'] = ''
			item['familyid'] = -1
			item['paramAn'] = ''
			item['paramPn'] = ''
			item['paramPd'] = ''
			item['paramCount'] = -1
			item['paramDB'] = ''
			item['paramPages'] = -1
			item['sysid'] = ''
			item['appid'] = ''
			item['title'] = ''
			item['abs'] = ''
			item['zhuquan'] = ''
			item['applicatDate'] = ''
			item['mainClassNum'] = ''
			item['classNum'] = ''
			item['eurMainClassNum'] = ''
			item['eurClassNum'] = ''
			item['rightHolder'] = ''
			item['inventDesigner'] = ''
			item['addr'] = ''
			item['countryCode'] = ''
			item['agency'] = ''
			item['agent'] = ''
			item['examinant'] = ''
			item['priority'] = ''
			item['internatApply'] = ''
			item['internatPub'] = ''
			item['entryDate'] = ''
			item['cateClass'] = ''
			item['certifyDay'] = ''
			item['caseApply'] = ''
			item['caseApplyNum'] = ''
			item['sameDayApply'] = ''
			item['apply_pdf_url'] = ''
			item['author_pdf_url'] = ''
			item['abs_pic'] = ''
			item['desc_pics'] = ''
			item['paramPn_shouq'] = ''
			item['paramPd_shouq'] = ''
			item['listLegalInfo'] = ''
			item['sqryzzlList'] = ''
			item['patentList'] = ''
			item['claim'] = ''
			item['description'] = ''
			item['shoufeeList'] = ''
			yield scrapy.Request(gongkai_url, method='POST', body=gongkai, cookies=self.cookie_dict,
			                     meta={'item': item})

	def parse(self, response):
		"""公开信息"""

		item = response.meta.get('item')
		cnipr_comp = str(item['origin_id']) + '~' + str(item['only_id']) + '~' + str(
			item['comp_full_name']) + '~' + str(item['cursorPage'])
		if '对不起，没有您访问的内容' in response.text:
			print('对不起，没有您访问的内容')
			# self.rc.lpush('cnipr_no_result', cnipr_comp)
			yield item
			return
		elif '您的操作过于频繁' in response.text:
			res = requests.get('http://search.cnipr.com/RandomCode?nocache={}'.format(int(time.time()*1000)), cookies=self.cookie_dict)
			with open('y.jpeg', 'wb') as f:
				f.write(res.content)
			# self.rc.lpush('cnipr_fail', cnipr_comp)
			print('您的操作过于频繁，公司为:{si}，指针为:{zhen}'.format(si=item['comp_full_name'], zhen=item['cursorPage']))
			raise CloseSpider('no datas')
		item = response.meta.get('item')
		select = scrapy.Selector(text=response.text)
		familyid = select.xpath('//input[@id="familyid"]/@value').extract_first()  # 70054101
		paramAn = select.xpath('//input[@id="paramAn"]/@value').extract_first()  # CN201310571770.7  申请(专利)号
		if not paramAn:
			self.rc.lpush('cnipr_fail', cnipr_comp)
			print('no paramAn，公司为:{si}，指针为:{zhen}'.format(si=item['comp_full_name'], zhen=item['cursorPage']))
			raise CloseSpider('no datas')
		paramPn = select.xpath('//input[@id="paramPn"]/@value').extract_first()  # CN104636980A  申请公布号
		paramPd = select.xpath('//input[@id="paramPd"]/@value').extract_first()  # 2015.05.20  公开公告日
		paramCount = select.xpath('//input[@id="paramCount"]/@value').extract_first()  # 53434  专利数量
		paramDB = select.xpath('//input[@id="paramDB"]/@value').extract_first()  # FMZL  专利类型
		paramPages = select.xpath('//input[@id="paramPages"]/@value').extract_first()  # 10  pdf页数
		sysid = select.xpath('//input[@id="sysid"]/@value').extract_first()  # 8901760804FBA43E4F27BA92E0081C56
		appid = select.xpath('//input[@id="appid"]/@value').extract_first()  # 201310571770.7
		zhuquan = ''
		applicatDate = ''
		mainClassNum = ''
		classNum = ''
		eurMainClassNum = ''
		eurClassNum = ''
		rightHolder = ''
		inventDesigner = ''
		addr = ''
		countryCode = ''
		agency = ''
		agent = ''
		examinant = ''  # 审查员
		priority = ''
		internatApply = ''
		internatPub = ''
		entryDate = ''
		cateClass = ''  # 范畴分类
		certifyDay = ''  # 颁证日
		caseApply = ''  # 分案申请
		caseApplyNum = ''  # 分案原申请号
		sameDayApply = ''
		apply_pdf_url = ''
		author_pdf_url = ''  # 授权公告pdf url
		abs_pic = ''
		desc_pics = ''
		paramPn_shouq = ''
		paramPd_shouq = ''
		shouquan_text = select.xpath('//a[@class="icon1"]/text()').extract_first()
		if not shouquan_text:
			if '说明书链接' in response.text:
				title = select.xpath('//div[@name="patti"]/text()').extract_first()
				abs = select.xpath('//span[@name="patab"]/text()').extract_first()
				ta_tag = select.xpath('//div[@class="nc3"]/table')
				applicatDate = ta_tag.xpath('./tr[2]/td[4]/span/text()').extract_first()
				mainClassNum = ta_tag.xpath('./tr[4]/td[2]/span/text()').extract_first()
				classNum = ta_tag.xpath('./tr[4]/td[4]/span/text()').extract()
				classNum = self._hanWu('; ', classNum)
				eurMainClassNum = ta_tag.xpath('./tr[5]/td[2]/span/text()').extract_first()
				eurClassNum = ta_tag.xpath('./tr[5]/td[4]/span/text()').extract()
				eurClassNum = self._hanWu('; ', eurClassNum)
				ats = ta_tag.xpath('./tr[6]/td[2]/a')
				holders = []
				for at in ats:
					holder = at.xpath('.//text()').extract()
					holder = ''.join(holder)
					holders.append(holder)
				rightHolder = '; '.join(holders)
				rightHolder = self._hanWu('', rightHolder)
				inventDesigner = ta_tag.xpath('./tr[6]/td[4]/a/text()').extract()
				inventDesigner = self._hanWu('; ', inventDesigner)
				priority = ta_tag.xpath('./tr[7]/td[2]/text()').extract()
				priority = self._hanWu('', priority)
				abs_pic = select.xpath('//div[@class="sum_img"]/img/@src').extract_first()
				abs_pic = abs_pic if 'images/en_img1.jpg' != abs_pic else ''
			elif '授权公布（公报）' in response.text:
				title = select.xpath('//div[@class="tp_left"]/h3/text()').extract_first()
				abs = select.xpath('//div[@class="txt"]//text()').extract_first()
				ta_tag = select.xpath('//div[@class="x_table"]/table')
				applicatDate = ta_tag.xpath('./tr[1]/td[2]/span[2]/text()').extract_first()
				paramPn_shouq = paramPn
				paramPd_shouq = paramPd
				ats = ta_tag.xpath('./tr[2]/td/a')
				holders = []
				for at in ats:
					holder = at.xpath('.//text()').extract()
					holder = ''.join(holder)
					holders.append(holder)
				rightHolder = '; '.join(holders)
				inventDesigner = ta_tag.xpath('./tr[3]/td/a//text()').extract()
				inventDesigner = self._uniteList(inventDesigner)
				addr = ta_tag.xpath('./tr[4]/td[1]/text()').extract_first()
				countryCode = ta_tag.xpath('./tr[4]/td[2]/text()').extract_first()
				mainClassNum = ta_tag.xpath('./tr[5]/td[1]/span[2]/text()').extract_first()
				classNum = ta_tag.xpath('./tr[5]/td[2]/span[2]/text()').extract_first()
				priority = ta_tag.xpath('./tr[6]/td/text()').extract_first()
				agency = ta_tag.xpath('./tr[7]/td[1]/text()').extract_first()
				agent = ta_tag.xpath('./tr[7]/td[2]/text()').extract_first()
				examinant = ta_tag.xpath('./tr[7]/td[3]/text()').extract_first()
				internatApply = ta_tag.xpath('./tr[8]/td[1]/text()').extract_first()
				internatPub = ta_tag.xpath('./tr[8]/td[2]/text()').extract_first()
				entryDate = ta_tag.xpath('./tr[8]/td[3]/text()').extract_first()
				cateClass = ta_tag.xpath('./tr[9]/td[1]/text()').extract_first()
				certifyDay = ta_tag.xpath('./tr[9]/td[2]/text()').extract_first()
				caseApply = ta_tag.xpath('./tr[9]/td[3]/text()').extract_first()
				author_pdf_url = select.xpath('//a[@class="pctquanwenlianjie"]/@href').extract_first()
			else:
				title = select.xpath('//div[@class="nc_left"]/h3/text()').extract_first()
				abs = select.xpath('//div[@class="nc_left"]/p[1]/text()').extract_first()
				zhuquan = select.xpath('//div[@class="nc_left"]/p[2]/text()').extract_first()  # 主权项
				tr_tags = select.xpath('//div[@class="nc_right"]/table/tr')
				for tr in tr_tags:
					text = tr.xpath('./td[@class="tit"]/text()').extract()
					text = ''.join(text) if text else ''
					auxs = tr.xpath('./td/span//text()').extract()
					aux = self._hanWu('; ', auxs)
					atexts = tr.xpath('./td/a//text()').extract()
					atext = self._hanWu('', atexts)
					tdtexts = tr.xpath('./td[2]//text()').extract()
					tdtext = self._hanWu('', tdtexts)
					if '申请日' in text:
						applicatDate = aux
					elif '主分类号' in text:
						mainClassNum = aux
					elif '分类号' in text and '主' not in text:
						classNum = aux
					elif '申请权利人' in text:
						ats = tr.xpath('./td/a')
						holders = []
						for at in ats:
							holder = at.xpath('.//text()').extract()
							holder = ''.join(holder)
							holders.append(holder)
						rightHolder = '; '.join(holders)
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
						case = self._hanWu('', auxs)
						caseApplyNum = case
					elif '同日申请' in text:
						sameday_url = tr.xpath('./td/span/a/@href').extract_first()
						sameDayApply = urljoin(response.url, sameday_url) if sameday_url else ''
				pdf_tags = select.xpath('//a[@class="shouquangongbu"]')
				for pdf in pdf_tags:
					pdf_text = pdf.xpath('./text()').extract_first()
					pdf_url = pdf.xpath('./@href').extract_first()
					if '申请公布' in pdf_text:
						apply_pdf_url = pdf_url
					elif '授权公告' in pdf_text:
						author_pdf_url = pdf_url
				abs_pic = select.xpath('//*[@id="gallery"]/a/@href').extract_first()
				abs_pic = abs_pic if 'images/ganlan_pic1.gif' != abs_pic else ''
			item['familyid'] = familyid if familyid else -1
			item['paramAn'] = paramAn if paramAn else ''
			item['paramPn'] = paramPn if paramPn else ''
			item['paramPd'] = paramPd if paramPd else ''
			item['paramCount'] = paramCount if paramCount else -1
			item['paramDB'] = paramDB if paramDB else ''
			item['paramPages'] = paramPages if paramPages else -1
			item['sysid'] = sysid if sysid else ''
			item['appid'] = appid if appid else ''
			item['title'] = title if title else ''
			item['abs'] = abs if abs else ''
			item['zhuquan'] = zhuquan if zhuquan else ''
			item['applicatDate'] = applicatDate if applicatDate else ''
			item['mainClassNum'] = mainClassNum if mainClassNum else ''
			item['classNum'] = classNum if classNum else ''
			item['eurMainClassNum'] = eurMainClassNum if eurMainClassNum else ''
			item['eurClassNum'] = eurClassNum if eurClassNum else ''
			item['rightHolder'] = rightHolder if rightHolder else ''
			item['inventDesigner'] = inventDesigner if inventDesigner else ''
			item['addr'] = addr if addr else ''
			item['countryCode'] = countryCode if countryCode else ''
			item['agency'] = agency if agency else ''
			item['agent'] = agent if agent else ''
			item['examinant'] = examinant if examinant else ''
			item['priority'] = priority if priority else ''
			item['internatApply'] = internatApply if internatApply else ''
			item['internatPub'] = internatPub if internatPub else ''
			item['entryDate'] = entryDate if entryDate else ''
			item['cateClass'] = cateClass if cateClass else ''
			item['certifyDay'] = certifyDay if certifyDay else ''
			item['caseApply'] = caseApply if caseApply else ''
			item['caseApplyNum'] = caseApplyNum if caseApplyNum else ''
			item['sameDayApply'] = sameDayApply if sameDayApply else ''
			item['apply_pdf_url'] = apply_pdf_url if apply_pdf_url else ''
			item['author_pdf_url'] = author_pdf_url if author_pdf_url else ''
			item['abs_pic'] = abs_pic if abs_pic else ''
			item['desc_pics'] = desc_pics if desc_pics else ''
			item['paramPn_shouq'] = paramPn_shouq if paramPn_shouq else ''
			item['paramPd_shouq'] = paramPd_shouq if paramPd_shouq else ''
			legal_url = 'http://search.cnipr.com/search!doLegalSearchByAn.action?rd=%(rd)s&strAn=%(strAn)s' % {
				'rd': random(),
				'strAn': paramAn
			}
			yield scrapy.Request(legal_url, cookies=self.cookie_dict, callback=self.legal, meta={'item': item})
		else:
			title = select.xpath('//div[@class="nc_left"]/h3/text()').extract_first()
			abs = select.xpath('//div[@class="nc_left"]/p[1]/text()').extract_first()
			zhuquan = select.xpath('//div[@class="nc_left"]/p[2]/text()').extract_first()  # 主权项
			tr_tags = select.xpath('//div[@class="nc_right"]/table/tr')
			for tr in tr_tags:
				text = tr.xpath('./td[@class="tit"]/text()').extract()
				text = ''.join(text) if text else ''
				auxs = tr.xpath('./td/span//text()').extract()
				aux = self._hanWu('; ', auxs)
				atexts = tr.xpath('./td/a//text()').extract()
				atext = self._hanWu('', atexts)
				tdtexts = tr.xpath('./td[2]//text()').extract()
				tdtext = self._hanWu('', tdtexts)
				if '申请日' in text:
					applicatDate = aux
				elif '主分类号' in text:
					mainClassNum = aux
				elif '分类号' in text and '主' not in text:
					classNum = aux
				elif '申请权利人' in text:
					ats = tr.xpath('./td/a')
					holders = []
					for at in ats:
						holder = at.xpath('.//text()').extract()
						holder = ''.join(holder)
						holders.append(holder)
					rightHolder = '; '.join(holders)
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
					case = self._hanWu('', auxs)
					caseApplyNum = case
				elif '同日申请' in text:
					sameday_url = tr.xpath('./td/span/a/@href').extract_first()
					sameDayApply = urljoin(response.url, sameday_url) if sameday_url else ''
			pdf_tags = select.xpath('//a[@class="shouquangongbu"]')
			for pdf in pdf_tags:
				pdf_text = pdf.xpath('./text()').extract_first()
				pdf_url = pdf.xpath('./@href').extract_first()
				if '申请公布' in pdf_text:
					apply_pdf_url = pdf_url
				elif '授权公告' in pdf_text:
					author_pdf_url = pdf_url
			abs_pic = select.xpath('//*[@id="gallery"]/a/@href').extract_first()
			abs_pic = abs_pic if 'images/ganlan_pic1.gif' != abs_pic else ''
			item['familyid'] = familyid if familyid else -1
			item['paramAn'] = paramAn if paramAn else ''
			item['paramPn'] = paramPn if paramPn else ''
			item['paramPd'] = paramPd if paramPd else ''
			item['paramCount'] = paramCount if paramCount else -1
			item['paramDB'] = paramDB if paramDB else ''
			item['paramPages'] = paramPages if paramPages else -1
			item['sysid'] = sysid if sysid else ''
			item['appid'] = appid if appid else ''
			item['title'] = title if title else ''
			item['abs'] = abs if abs else ''
			item['zhuquan'] = zhuquan if zhuquan else ''
			item['applicatDate'] = applicatDate if applicatDate else ''
			item['mainClassNum'] = mainClassNum if mainClassNum else ''
			item['classNum'] = classNum if classNum else ''
			item['eurMainClassNum'] = eurMainClassNum if eurMainClassNum else ''
			item['eurClassNum'] = eurClassNum if eurClassNum else ''
			item['rightHolder'] = rightHolder if rightHolder else ''
			item['inventDesigner'] = inventDesigner if inventDesigner else ''
			item['addr'] = addr if addr else ''
			item['countryCode'] = countryCode if countryCode else ''
			item['agency'] = agency if agency else ''
			item['agent'] = agent if agent else ''
			item['examinant'] = examinant if examinant else ''
			item['priority'] = priority if priority else ''
			item['internatApply'] = internatApply if internatApply else ''
			item['internatPub'] = internatPub if internatPub else ''
			item['entryDate'] = entryDate if entryDate else ''
			item['cateClass'] = cateClass if cateClass else ''
			item['certifyDay'] = certifyDay if certifyDay else ''
			item['caseApply'] = caseApply if caseApply else ''
			item['caseApplyNum'] = caseApplyNum if caseApplyNum else ''
			item['sameDayApply'] = sameDayApply if sameDayApply else ''
			item['apply_pdf_url'] = apply_pdf_url if apply_pdf_url else ''
			item['author_pdf_url'] = author_pdf_url if author_pdf_url else ''
			item['abs_pic'] = abs_pic if abs_pic else ''
			item['desc_pics'] = desc_pics if desc_pics else ''
			item['paramPn_shouq'] = paramPn_shouq if paramPn_shouq else ''
			item['paramPd_shouq'] = paramPd_shouq if paramPd_shouq else ''
			shouquan_url = 'http://search.cnipr.com/search!viewDetail.action'
			shouquan = 'an=%(an)s&allsources=%(sources)s&strSources=%(strSources)s' % {
				'an': paramAn,
				'sources': self.sources,
				'strSources': paramDB
			}
			yield scrapy.Request(shouquan_url, method='POST', body=shouquan,
			                     cookies=self.cookie_dict, callback=self.parse_shouquan, meta={'item': item})

	def parse_shouquan(self, response):
		"""授权信息"""
		item = response.meta.get('item')
		cnipr_comp = str(item['origin_id']) + '~' + str(item['only_id']) + '~' + str(
			item['comp_full_name']) + '~' + str(item['cursorPage'])
		if '您的操作过于频繁' in response.text:
			# self.rc.lpush('cnipr_fail', cnipr_comp)
			print('您的操作过于频繁，公司为:{si}，指针为:{zhen}'.format(si=item['comp_full_name'], zhen=item['cursorPage']))
			raise CloseSpider('no datas')
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
		yield scrapy.Request(legal_url, cookies=self.cookie_dict, callback=self.legal, meta={'item': item})

	def legal(self, response):
		"""法律状态"""
		item = response.meta.get('item')
		cnipr_comp = str(item['origin_id']) + '~' + str(item['only_id']) + '~' + str(
			item['comp_full_name']) + '~' + str(item['cursorPage'])
		if '您的操作过于频繁' in response.text:
			# self.rc.lpush('cnipr_fail', cnipr_comp)
			print('您的操作过于频繁，公司为:{si}，指针为:{zhen}'.format(si=item['comp_full_name'], zhen=item['cursorPage']))
			raise CloseSpider('no datas')
		try:
			text = json.loads(response.text)
		except:
			# self.rc.lpush('cnipr_fail', cnipr_comp)
			print('no legal，公司为:{si}，指针为:{zhen}'.format(si=item['comp_full_name'], zhen=item['cursorPage']))
			raise CloseSpider('no datas')
		paramPn = item['paramPn']
		listLegalInfo = text.get('listLegalInfo')
		legal_dict = {'listLegalInfo': listLegalInfo} if listLegalInfo else {}
		item['listLegalInfo'] = json.dumps(legal_dict) if legal_dict else ''
		cnReference_url = 'http://search.cnipr.com/reference!getCnReference.action?rd=%(rd)s&patnum=%(patnum)s' % {
			'rd': random(),
			'patnum': paramPn
		}
		yield scrapy.Request(cnReference_url, cookies=self.cookie_dict, callback=self.cnReference, meta={'item': item})

	def cnReference(self, response):
		"""引证文献"""
		item = response.meta.get('item')
		cnipr_comp = str(item['origin_id']) + '~' + str(item['only_id']) + '~' + str(
			item['comp_full_name']) + '~' + str(item['cursorPage'])
		if '您的操作过于频繁' in response.text:
			# self.rc.lpush('cnipr_fail', cnipr_comp)
			print('您的操作过于频繁，公司为:{si}，指针为:{zhen}'.format(si=item['comp_full_name'], zhen=item['cursorPage']))
			raise CloseSpider('no datas')
		try:
			text = json.loads(response.text)
		except:
			# self.rc.lpush('cnipr_fail', cnipr_comp)
			print('no cnReference，公司为:{si}，指针为:{zhen}'.format(si=item['comp_full_name'], zhen=item['cursorPage']))
			raise CloseSpider('no datas')
		familyid = item['familyid']
		dto = text.get('dto')
		sqryzzlList = dto.get('sqryzzlList', []) if dto else []
		cn_dict = {'sqryzzlList': sqryzzlList} if sqryzzlList else {}
		item['sqryzzlList'] = json.dumps(cn_dict) if cn_dict else ''
		patentList_url = 'http://search.cnipr.com/wordtips!familyPatentSearch.action?rd=%(rd)s&an=%(an)s' % {
			'rd': random(),
			'an': familyid
		}
		yield scrapy.Request(patentList_url, cookies=self.cookie_dict, callback=self.patentList, meta={'item': item})

	def patentList(self, response):
		"""同族专利"""
		item = response.meta.get('item')
		cnipr_comp = str(item['origin_id']) + '~' + str(item['only_id']) + '~' + str(
			item['comp_full_name']) + '~' + str(item['cursorPage'])
		if '您的操作过于频繁' in response.text:
			# self.rc.lpush('cnipr_fail', cnipr_comp)
			print('您的操作过于频繁，公司为:{si}，指针为:{zhen}'.format(si=item['comp_full_name'], zhen=item['cursorPage']))
			raise CloseSpider('no datas')
		try:
			text = json.loads(response.text)
		except:
			# self.rc.lpush('cnipr_fail', cnipr_comp)
			print('no patentList，公司为:{si}，指针为:{zhen}'.format(si=item['comp_full_name'], zhen=item['cursorPage']))
			raise CloseSpider('no datas')
		paramAn = item['paramAn']
		patentList = text.get('patentList')
		patentList_dict = {'patentList': patentList} if patentList else {}
		item['patentList'] = json.dumps(patentList_dict) if patentList_dict else ''
		shoufei_url = 'http://search.cnipr.com/search!doNianjinByAn.action?rd=%(rd)s&strAn=%(strAn)s' % {
			'rd': random(),
			'strAn': paramAn
		}
		yield scrapy.Request(shoufei_url, cookies=self.cookie_dict, callback=self.shoufei, meta={'item': item})

	def shoufei(self, response):
		"""收费信息"""
		item = response.meta.get('item')
		cnipr_comp = str(item['origin_id']) + '~' + str(item['only_id']) + '~' + str(
			item['comp_full_name']) + '~' + str(item['cursorPage'])
		if '您的操作过于频繁' in response.text:
			# self.rc.lpush('cnipr_fail', cnipr_comp)
			print('您的操作过于频繁，公司为:{si}，指针为:{zhen}'.format(si=item['comp_full_name'], zhen=item['cursorPage']))
			raise CloseSpider('no datas')
		try:
			text = json.loads(response.text)
		except:
			# self.rc.lpush('cnipr_fail', cnipr_comp)
			print('no shoufei，公司为:{si}，指针为:{zhen}'.format(si=item['comp_full_name'], zhen=item['cursorPage']))
			raise CloseSpider('no datas')
		shoufeeList = text.get('shoufeeList')
		shoufeeList_dict = {'shoufeeList': shoufeeList} if shoufeeList else {}
		item['shoufeeList'] = json.dumps(shoufeeList_dict) if shoufeeList_dict else ''
		yield item

	# 	paramAn = item['paramAn']
	# 	paramPd = item['paramPd']
	# 	paramDB = item['paramDB']
	# 	quanli_url = 'http://search.cnipr.com/loaddata!loadXml.action?rd=%(rd)s&an=%(an)s&strSource=%(strSource)s&pd=%(pd)s&xmltype=CLM' % {
	# 		'rd': random(),
	# 		'an': paramAn,
	# 		'strSource': paramDB,
	# 		'pd': paramPd,
	# 	}
	# 	yield scrapy.Request(quanli_url, cookies=self.cookie_dict, callback=self.quanli,
	# 	                     meta={'item': item})
	#
	# def quanli(self, response):
	# 	"""权利要求书"""
	# 	item = response.meta.get('item')
	# 	paramAn = item['paramAn']
	# 	paramPd = item['paramPd']
	# 	paramDB = item['paramDB']
	# 	text = json.loads(response.text)
	# 	xml = text.get('xml')
	# 	item['claim'] = xml
	# 	shuoming_url = 'http://search.cnipr.com/loaddata!loadXml.action?rd=%(rd)s&an=%(an)s&strSource=%(strSource)s&pd=%(pd)s&xmltype=DES' % {
	# 		'rd': random(),
	# 		'an': paramAn,
	# 		'strSource': paramDB,
	# 		'pd': paramPd,
	# 	}
	# 	yield scrapy.Request(shuoming_url, cookies=self.cookie_dict, callback=self.shuoming,
	# 	                     meta={'item': item})
	#
	# def shuoming(self, response):
	# 	"""说明书"""
	# 	item = response.meta.get('item')
	# 	text = json.loads(response.text)
	# 	xml = text.get('xml')
	# 	item['description'] = xml

	def _hanBracket(self, s):
		return s.replace('(', r'\(').replace(')', r'\)').replace('（', r'\（').replace('）', r'\）')

	def _solSpace(self, s):
		return s.strip().replace('\t', '').replace('\r', '').replace('\n', '')

	def _uniteList(self, vl, sep='; '):
		vl_1 = sep.join([self._solSpace(v) for v in vl if v]) if vl else ''
		return vl_1

	def _hanWu(self, sep, vl):
		vl_1 = sep.join([self._solSpace(v) for v in vl if v]) if vl else ''
		vl_2 = vl_1 if '无' != vl_1 else ''
		return vl_2
