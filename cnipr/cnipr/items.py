# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CniprItem(scrapy.Item):
	"""
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
		item['paramPn_shouq'] = paramPn_shouq
		item['paramPd_shouq'] = paramPd_shouq
		item['listLegalInfo'] = str(listLegalInfo)
		item['sqryzzlList'] = str(sqryzzlList)
		item['claim'] = xml
		item['description'] = xml
		item['patentList'] = str(patentList)

	"""
	familyid = scrapy.Field()
	paramAn = scrapy.Field()
	paramPn = scrapy.Field()
	paramPd = scrapy.Field()
	paramCount = scrapy.Field()
	paramDB = scrapy.Field()
	paramPages = scrapy.Field()
	sysid = scrapy.Field()
	appid = scrapy.Field()
	title = scrapy.Field()
	abs = scrapy.Field()
	zhuquan = scrapy.Field()
	applicatDate = scrapy.Field()
	mainClassNum = scrapy.Field()
	classNum = scrapy.Field()
	rightHolder = scrapy.Field()
	inventDesigner = scrapy.Field()
	addr = scrapy.Field()
	countryCode = scrapy.Field()
	agency = scrapy.Field()
	agent = scrapy.Field()
	priority = scrapy.Field()
	internatApply = scrapy.Field()
	internatPub = scrapy.Field()
	entryDate = scrapy.Field()
	caseApplyNum = scrapy.Field()
	sameDayApply = scrapy.Field()
	paramPn_shouq = scrapy.Field()
	paramPd_shouq = scrapy.Field()
	listLegalInfo = scrapy.Field()
	sqryzzlList = scrapy.Field()
	claim = scrapy.Field()
	description = scrapy.Field()
	patentList = scrapy.Field()
