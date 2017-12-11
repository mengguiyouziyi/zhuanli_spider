"""
将zhuanli 10张表融合
"""
import math
from use.utility.info import etl
from more_itertools import chunked


class Huizong(object):
	def __init__(self, tab_in, tab_out, conn=etl):
		self.conn = conn
		self.cur = self.conn.cursor()
		self.tab_in = tab_in
		self.tab_out = tab_out

	def get_results(self, tab, sta):
		sql = """select * from {tab} limit {sta}, 200000""".format(tab=tab, sta=sta)
		self.cur.execute(sql)
		results = self.cur.fetchall()
		# print(len(results))
		return results

	def _get_column(self, tab):
		"""
		获取mysql表 字段字符串
		:param con:
		:param table_in:
		:return:
		"""
		sql = """select group_concat(column_name) from information_schema.columns WHERE table_name = '{tab}' and table_schema = 'spider'""".format(
			tab=tab)
		self.cur.execute(sql)
		results = self.cur.fetchall()
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

	def hui_zong(self, args_list):
		"""
		专利信息入库
		:param insert_con:
		:param tab:
		:param args_list:
		:return:
		"""
		col_list = self._get_column(self.tab_in)[1:-1]
		col_str = ','.join(col_list)
		val_str = self._handle_str(len(col_list))
		insql = """insert into {tab} ({col}) VALUES ({val})""".format(tab=self.tab_in, col=col_str, val=val_str)
		# 确保入库的时候都在50条以下
		l = len(args_list)
		if l >= 2000:
			aux = list(chunked(args_list, math.ceil(l / 2)))
			for a in aux:
				self.cur.executemany(insql, a)
				self.conn.commit()
				print('insert ', len(a))
		else:
			self.cur.executemany(insql, args_list)
			self.conn.commit()
			print('insert ', len(args_list))


if __name__ == '__main__':
	tab_in = 'zhuanli_info_all'
	tab_out = 'zhuanli_info_all'
	huizong = Huizong(tab_in=tab_in, tab_out=tab_out)
	for num in range(10):
		tab_out = tab_out + '_' + str(num)
		sta = 0
		while True:
			results = huizong.get_results(tab=tab_out, sta=sta)
			if not results:
				break
			print('handle table ', num, ' start ', sta)
			sta += len(results)
			col_list = huizong._get_column(tab_in)[1:-1]
			args_list = [[result[k] for k in col_list] for result in results]
			huizong.hui_zong(args_list)
		# sql = """select * from zhuanli_info_all limit 0, 10"""
		# cur = etl.cursor()
		# cur.execute(sql)
		# r = cur.fetchall()
		# print(r)
