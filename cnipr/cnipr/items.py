# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CniprItem(scrapy.Item):
	origin_id = scrapy.Field()
	only_id = scrapy.Field()
	comp_full_name = scrapy.Field()

	cursorPage = scrapy.Field()

	# 这部分后面补充
	tifvalue = scrapy.Field()
	xmlvalue = scrapy.Field()
	pdfvalue = scrapy.Field()
	pdfvalue2 = scrapy.Field()
	patentStatus = scrapy.Field()

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
	eurMainClassNum = scrapy.Field()
	eurClassNum = scrapy.Field()

	rightHolder = scrapy.Field()
	inventDesigner = scrapy.Field()
	addr = scrapy.Field()
	countryCode = scrapy.Field()
	agency = scrapy.Field()
	agent = scrapy.Field()

	examinant = scrapy.Field()

	priority = scrapy.Field()
	internatApply = scrapy.Field()
	internatPub = scrapy.Field()
	entryDate = scrapy.Field()

	cateClass = scrapy.Field()
	certifyDay = scrapy.Field()
	caseApply = scrapy.Field()

	caseApplyNum = scrapy.Field()
	sameDayApply = scrapy.Field()

	apply_pdf_url = scrapy.Field()
	author_pdf_url = scrapy.Field()
	abs_pic = scrapy.Field()
	desc_pics = scrapy.Field()

	paramPn_shouq = scrapy.Field()
	paramPd_shouq = scrapy.Field()

	listLegalInfo = scrapy.Field()
	sqryzzlList = scrapy.Field()
	patentList = scrapy.Field()
	claim = scrapy.Field()
	description = scrapy.Field()
	shoufeeList = scrapy.Field()
