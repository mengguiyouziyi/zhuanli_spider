# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
import hashlib
import time
# from scrapy.xlib.pydispatch import dispatcher
# from scrapy import signals
from scrapy.exceptions import DropItem
from cnipr.items import CniprItem


class MysqlPipeline(object):
	def __init__(self):
		try:
			self.conn = pymysql.connect(host='172.31.215.38', port=3306, user='spider', password='spider', db='spider',
			                            charset='utf8', cursorclass=pymysql.cursors.DictCursor)
		except Exception as e:
			print(e)
			time.sleep(2)
			self.__init__()
		self.cursor = self.conn.cursor()

	# self.item_list = []
	# dispatcher.connect(self.spider_closed, signals.spider_closed)

	# def __init__(self):
	#     self.browser = webdriver.Chrome(executable_path="D:/Temp/chromedriver.exe")
	#     super(JobboleSpider, self).__init__()
	#     dispatcher.connect(self.spider_closed, signals.spider_closed)
	#
	# def spider_closed(self, spider):
	# 	# 当爬虫退出的时候关闭chrome
	# 	print("spider closed")
	# 	sql = """insert into jianjie_shunqi_all_copy (comp_url, comp_name, intro, city) VALUES(%s, %s, %s, %s)"""
	# 	self.cursor.executemany(sql, self.item_list)
	# 	self.conn.commit()
	# 	print('%s insert' % len(self.item_list))

	def process_item(self, item, spider):
		if isinstance(item, CniprItem):
			sql = """insert into jianjie_shunqi_all (comp_url, comp_name, intro, city) VALUES(%s, %s, %s, %s)"""
			args = [item['comp_url'], item['comp_name'], item['intro'], item['city']]
			self.cursor.execute(sql, args)
			self.conn.commit()
		# print(str(item['comp_url']) + ' ' + str(item['comp_name']))
		# if len(self.item_list) == 500:
		# 	sql = """insert into jianjie_shunqi_all_copy (comp_url, comp_name, intro, city) VALUES(%s, %s, %s, %s)"""
		# 	self.cursor.executemany(sql, self.item_list)
		# 	self.conn.commit()
		# 	self.item_list.clear()
		# 	print('200 insert')
		# else:
		# 	self.item_list.append([item['comp_url'], item['comp_name'], item['intro'], item['city']])


class DuplicatesPipeline(object):
	def __init__(self):
		self.item_set = set()

	def process_item(self, item, spider):
		m = self.gen_md5(item['comp_url'])
		if m in self.item_set:
			raise DropItem("Duplicate item found")
		else:
			self.item_set.add(m)
			return item

	def gen_md5(self, comp_name):
		"""
		生成唯一id
		:return:
		0cc2662f5eb157c8ffcd43c145de499f2ab27a71
		72843135390705548651698998647502012318670289521
		a3f4a5b080e2a4ef4a708b9c9f5ad003
		217934444328053067635429399579879723011
		"""
		m = hashlib.md5()
		m.update(comp_name.encode('utf-8'))
		comp_md5 = m.hexdigest()
		# only_id_full = int(comp_md5, 16)
		# return str(only_id_full)
		return comp_md5
