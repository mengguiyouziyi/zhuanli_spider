# -*- coding: utf-8 -*-
import scrapy
import requests
import json
from random import random
from urllib.parse import urljoin
from cnipr.items import CniprItem
from util.info import startup_nodes, user_dict
from rediscluster import StrictRedisCluster
from scrapy.exceptions import CloseSpider


class TouzishijianSpider(scrapy.Spider):
	name = 'FVVW001_biaodashi'
	custom_settings = {
		'DEFAULT_REQUEST_HEADERS': {
			'content-type': "application/x-www-form-urlencoded",
		},
	}

	def __init__(self):
		self.sources = 'FMZL,SYXX,WGZL,FMSQ,TWZL,HKPATENT,USPATENT,EPPATENT,JPPATENT,WOPATENT,GBPATENT,CHPATENT,DEPATENT,KRPATENT,FRPATENT,RUPATENT,ASPATENT,ATPATENT,GCPATENT,ITPATENT,AUPATENT,APPATENT,CAPATENT,SEPATENT,ESPATENT,OTHERPATENT'
		# self.rc = StrictRedisCluster(startup_nodes=startup_nodes, decode_responses=True)
		self.user = user_dict['FVVW001']
		self.cookie_dict = self.login()
		print(self.cookie_dict)

	def login(self):
		login_url = 'http://search.cnipr.com/login.action?rd={}'.format(random())
		print(self.user)
		response = requests.request(method="POST", url=login_url, data=self.user)
		print(response.text)
		j_res = response.json()
		if j_res.get('msg') == 'alreadylogin':
			print('alreadylogin.....')
			goonlogin_url = 'http://search.cnipr.com/login!goonlogin.action?rd={}'.format(random())
			response = requests.request(method="POST", url=goonlogin_url, data=self.user)
		print(response.text)
		cookie_dict = dict(response.cookies.items())
		return cookie_dict

	def start_requests(self):
		for i in range(140):
			item = CniprItem()
			gongkai_url = 'http://search.cnipr.com/search!doDetailSearch.action'
			gongkai = 'strWhere=%E4%B8%BB%E5%88%86%E7%B1%BB%E5%8F%B7%3D%28%EF%BC%88G01S17%2F06+or+G01S17%2F08+or+G01S17%2F10+or+G01S17%2F32+or+G01S17%2F36+or+G01S17%2F42+or+G01S17%2F46+or+G01S17%2F48%EF%BC%89%29+and+%E5%90%8D%E7%A7%B0%2C%E6%91%98%E8%A6%81%2C%E6%9D%83%E5%88%A9%E8%A6%81%E6%B1%82%E4%B9%A6%2B%3D%28%E6%BF%80%E5%85%89%E9%9B%B7%E8%BE%BE+and+%28%E4%BD%8D%E7%BD%AE+or+%E5%9D%90%E6%A0%87+or+%E8%B7%9D%E7%A6%BB+or+%E9%95%BF%E5%BA%A6+or+%E5%AE%BD%E5%BA%A6%29%29&start={start}&recordCursor={cur}&limit=1&option=2&iHitPointType=115&strSortMethod=RELEVANCE&strSources=FMZL%2CSYXX%2CWGZL%2CFMSQ%2CTWZL%2CHKPATENT%2CUSPATENT%2CEPPATENT%2CJPPATENT%2CWOPATENT%2CGBPATENT%2CCHPATENT%2CDEPATENT%2CKRPATENT%2CFRPATENT%2CRUPATENT%2CASPATENT%2CATPATENT%2CGCPATENT%2CITPATENT%2CAUPATENT%2CAPPATENT%2CCAPATENT%2CSEPATENT%2CESPATENT%2COTHERPATENT&strSynonymous=&yuyijs=&filterChannel=&otherWhere='
			item['origin_id'] = -1
			item['only_id'] = ''
			item['comp_full_name'] = ''
			item['cursorPage'] = -1
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
			if i < 10:
				start = 1
			elif 10 <= i < 20:
				start = 2
			elif 20 <= i < 30:
				start = 3
			elif 30 <= i < 40:
				start = 4
			elif 40 <= i < 50:
				start = 5
			elif 50 <= i < 60:
				start = 6
			elif 60 <= i < 70:
				start = 7
			elif 70 <= i < 80:
				start = 8
			elif 80 <= i < 90:
				start = 9
			elif 90 <= i < 100:
				start = 10
			elif 100 <= i < 110:
				start = 11
			elif 110 <= i < 120:
				start = 12
			elif 120 <= i < 130:
				start = 13
			else:
				start = 14
			yield scrapy.Request(gongkai_url, method='POST', body=gongkai.format(start=start, cur=i),
			                     cookies=self.cookie_dict, meta={'item': item})

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
			# res = requests.get('http://search.cnipr.com/RandomCode?nocache={}'.format(int(time.time()*1000)), cookies=self.cookie_dict)
			# with open('y.jpeg', 'wb') as f:
			# 	f.write(res.content)

			# self.rc.lpush('cnipr_fail', cnipr_comp)
			print('您的操作过于频繁，公司为:{si}，指针为:{zhen}'.format(si=item['comp_full_name'], zhen=item['cursorPage']))
			raise CloseSpider('no datas')
		item = response.meta.get('item')
		select = scrapy.Selector(text=response.text)
		familyid = select.xpath('//input[@id="familyid"]/@value').extract_first()  # 70054101
		paramAn = select.xpath('//input[@id="paramAn"]/@value').extract_first()  # CN201310571770.7  申请(专利)号
		if not paramAn:
			# self.rc.lpush('cnipr_fail', cnipr_comp)
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
				abs = select.xpath('//span[@name="patab"]//text()').extract()
				abs = self._solStrip(abs)
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
				abs = select.xpath('//div[@class="txt"]//text()').extract()
				abs = self._solStrip(abs)
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
				abs = select.xpath('//div[@class="nc_left"]/p[1]//text()').extract()
				abs = self._solStrip(abs)
				zhuquan = select.xpath('//div[@class="nc_left"]/p[2]//text()').extract()  # 主权项
				zhuquan = self._solStrip(zhuquan)
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
			abs = select.xpath('//div[@class="nc_left"]/p[1]//text()').extract()
			abs = self._solStrip(abs)
			zhuquan = select.xpath('//div[@class="nc_left"]/p[2]//text()').extract()  # 主权项
			zhuquan = self._solStrip(zhuquan)
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

	def _solStrip(self, liebiao):
		return ''.join([l.strip() for l in liebiao if l]) if liebiao else ''