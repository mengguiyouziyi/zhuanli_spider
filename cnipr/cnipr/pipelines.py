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
	def __init__(self):
		self.rc = StrictRedisCluster(startup_nodes=startup_nodes, decode_responses=True)
		self.conn = etl
		self.cursor = self.conn.cursor()

	def _get_column(self, tab):
		"""
		获取mysql表 字段字符串
		:param con:
		:param table_in:
		:return:
		"""
		sql = """select group_concat(column_name) from information_schema.columns WHERE table_name = '{tab}' and table_schema = 'spider'""".format(
			tab=tab)
		self.cursor.execute(sql)
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
			col_list = self._get_column('patent_cnipr_all')[1:-1]
			col_str = ','.join(col_list)
			val_str = self._handle_str(len(col_list))
			sql = """insert into patent_cnipr_all ({col}) VALUES ({val})""".format(col=col_str, val=val_str)
			args = [item[i] for i in col_list]
		else:
			raise CloseSpider('no item match...')
		try:
			self.cursor.execute(sql, args)
			self.conn.commit()
			print(item['title'])
		except Exception as e:
			cnipr_comp = str(item['origin_id']) + '~' + str(item['only_id']) + '~' + str(
				item['comp_full_name']) + '~' + str(item['cursorPage'])
			self.rc.lpush('cnipr_mysql_error', cnipr_comp)
			print(e)
			print('mysql error，公司为:{si}，指针为:{zhen}'.format(si=item['comp_full_name'], zhen=item['cursorPage']))
			raise CloseSpider('no datas')


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
