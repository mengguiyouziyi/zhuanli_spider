# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import hashlib
from scrapy.exceptions import CloseSpider
from scrapy.exceptions import DropItem
from cnipr.items import CniprItem
from util.info import etl, startup_nodes
from rediscluster import StrictRedisCluster


class MysqlPipeline(object):
	def __init__(self, crawler):
		self.crawler = crawler

		# self.rc = StrictRedisCluster(startup_nodes=startup_nodes, decode_responses=True)
		self.conn = etl
		self.cursor = self.conn.cursor()
		self.col_list = self._get_column('patent_cnipr_all_test')[1:-1]
		self.col_str = ','.join(self.col_list)
		self.val_str = self._handle_str(len(self.col_list))

	@classmethod
	def from_crawler(cls, crawler):
		return cls(crawler)

	def _get_column(self, tab):
		"""
		获取mysql表 字段字符串
		:param con:
		:param table_in:
		:return:
		"""
		sql = """select group_concat(column_name) from information_schema.columns WHERE table_name = '{tab}' and table_schema = 'spider'""".format(
			tab=tab)
		try:
			self.cursor.execute(sql)
		except Exception as e:
			print(e)
			print('获取数据表字段错误....')
			exit(1)
		results = self.cursor.fetchall()
		col_str = results[0]['group_concat(column_name)']
		col_list = col_str.split(',')
		return col_list

	def _handle_str(self, num):
		"""
		根据插入字段数量来构造sql语句
		:param num: 插入字段数量
		:return: sql的value字符串
		"""
		x = "%s"
		y = ", %s"
		for i in range(num - 1):
			x += y
		return x

	def process_item(self, item, spider):
		if isinstance(item, CniprItem):
			sql = """insert into patent_cnipr_all_test ({col}) VALUES ({val})""".format(col=self.col_str, val=self.val_str)
			args = [item[i] for i in self.col_list]
		else:
			raise CloseSpider('no item match...')
		try:
			self.cursor.execute(sql, args)
			self.conn.commit()
			print(item['title'])
		except Exception as e:
			cnipr_comp = str(item['origin_id']) + '~' + str(item['only_id']) + '~' + str(
				item['comp_full_name']) + '~' + str(item['cursorPage'])
			# self.rc.lpush('cnipr_fail', cnipr_comp)
			print(e)
			print('mysql error，公司为:{si}，指针为:{zhen}'.format(si=item['comp_full_name'], zhen=item['cursorPage']))
			self.crawler.engine.close_spider(spider, 'mysql error')


