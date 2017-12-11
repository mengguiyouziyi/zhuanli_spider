# coding:utf-8
"""
通过redis获取公司名称和所申请的页码
"""
import requests, time, math, sys
from datetime import datetime
from rediscluster import StrictRedisCluster
from more_itertools import chunked
from collections import OrderedDict
from pymysql.connections import err
from getToken import get_token
from util.info import etl, startup_nodes, key_list


class PatentApi(object):
	"""
	本项目逻辑：
		1、先把92万公司全部前100条（少于100条的就全部抓下来了）抓取一遍（已完成）
		2、通过日志（日志文件在服务器/menggui/zhuanli_spider/use/目录下所有的out文件）找出92万中没有抓取成功的，分析不成功的原因（比如超时、表达式的关键字含有api无法识别的符号，比如'('要变成'\('等），本阶段可以不做
		3、从11张表中取出公司和申请量，用total/100来获得页数，将公司、申请量、页码等循环打入redis，最后通过此代码获取
		4、所有错误的公司+游标都打入了另一个key（包括每天的overtimes超过调用次数的），最后不要忘了抓取
	注意：
		1、92万公司会有很多重复的、不规范的公司名称，会导致api返回的申请量不准确，所以需要统一一下这些公司的名称
		2、sh调用脚本和Linux crontab定时抓取已包含在文档中
	"""

	def __init__(self):
		self.conn = etl
		self.cursor = self.conn.cursor()
		self.tab = 'zhuanli_info_all'
		self.token = get_token()
		self.api_url = "http://114.251.8.193/api/patent/search/expression"
		self.session = requests.session()
		self.key_list = key_list
		self.ini_dict = {}.fromkeys(self.key_list, '')
		self.rc = StrictRedisCluster(startup_nodes=startup_nodes, decode_responses=True)

	def get_update_dicts(self, records):
		"""
		获取更新后的字典列表
		:param records:
		:return:
		"""
		long_records = []
		for record in records:
			temp = self.ini_dict.copy()
			low = {k.lower(): v for k, v in OrderedDict(record).items()}
			temp.update(low)
			long_records.append(temp)
		return long_records

	def get_values(self, values, add_list):
		"""
		将元素添加到list行首
		:param values:
		:param add_list:
		:return:
		"""
		values = [add_list + value for value in values]
		return values

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

	def _get_column(self, tab):
		"""
		获取mysql表 字段字符串
		:param tab:
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

	def in_zhuanli(self, args_list):
		"""
		每次插入申请回来的一批专利
		:param args_list:
		:return:
		"""
		last_num_str = args_list[0][1][-1]
		in_tab = self.tab + '_' + last_num_str
		col_list = self._get_column(in_tab)[1:-1]  # 获取要插入的字段列表
		col_str = ','.join(col_list)  # 获取插入字段字符串
		val_str = self._handle_str(len(col_list))  # 获取 %s, %s... 字符串
		sql = """insert into {tab} ({columns}) VALUES ({val})""".format(tab=in_tab, columns=col_str, val=val_str)
		# 确保入库的时候都在50条以下
		l = len(args_list)
		if l >= 50:
			aux = list(chunked(args_list, math.ceil(l / 2)))
			for a in aux:
				self.cursor.executemany(sql, a)
				self.conn.commit()
		else:
			self.cursor.executemany(sql, args_list)
			self.conn.commit()

	def get_res(self, only_id, querystring, page):
		"""
		通过get请求专利数据，并判断各种个样的错误类型
		:param only_id:
		:param querystring:
		:param page:
		:return:
		"""
		try:
			info = self.session.get(self.api_url, params=querystring, timeout=15).json()
		except:
			print(only_id, '~~timeout error~~', page, datetime.now())
			return
		if not info:
			print(only_id, '~~no info~~', page, datetime.now())
			return
		errorCode = info.get('errorCode')
		context = info.get('context')
		if not errorCode:
			print(only_id, '~~no errorCode~~', page, datetime.now())
			print(info)
			return
		if errorCode == '000016':
			# 查询错误，最多只能返回查询条件前10000条数据
			print(only_id, '~~code:000016 Query error, only return the first 10000~~', page, datetime.now())
			return
		elif errorCode == "表达式语法错误":
			# 存在语法错误，请重新编辑表达式后进行检索
			print(only_id, '~~Syntax error~~', page, datetime.now())
			print(querystring)
			return
		elif errorCode == '000003':
			# 连接数据查询库异常
			print(only_id, '~~code:000003 Connecting data query base exceptions~~', page)
			return
		elif not context and errorCode == '000000':
			print(only_id, '~~no context but 000000~~', page, datetime.now())
			print(info)
			return
		elif not context and errorCode == '9999':
			# 说明接口调用超过限制
			print(only_id, '~~overtimes~~', page, datetime.now())
			print('program over...')
			sys.exit(1)
		elif errorCode == '000000':
			# total = info.get('total')
			records = context.get('records')
			records = self.get_update_dicts(records)
			values = [[record[i] for i in self.key_list] for record in records]
			return values
		else:
			print(only_id, '~~other error~~', page, datetime.now())
			print(info.strip())
			return

	def main(self):
		"""
		主逻辑方法，不断从redis取出公司和游标，并将错误的公司和游标打如另外的key
		:return:
		"""
		while True:
			comp = self.rc.rpop('patent_api_comp')
			if not comp:
				print('no datas...')
				exit(1)
			value_list = comp.split('~')
			origin_id = value_list[0]
			only_id = value_list[1]
			comp_full_name = value_list[2]
			total = value_list[3]
			page = value_list[4]
			# comp_full_name = comp_full_name.replace('(', r'\(').replace(')', r'\)')
			querystring = {
				"client_id": "6050f8adac110002270d833aed28242d",
				"access_token": self.token,
				"scope": "read_cn",
				"express": "申请人=%s" % comp_full_name,
				"page": "%s" % page,
				"page_row": "100"
			}
			values = self.get_res(only_id, querystring, page)
			if not values:
				self.rc.lpush('patent_api_error', comp)
				continue
			add_list = [origin_id, only_id, comp_full_name, total]
			values = self.get_values(values, add_list)
			try:
				self.in_zhuanli(values)
				print(only_id, '~~success~~', 1, datetime.now())
			except err.InterfaceError:
				print(only_id, '~~mysql no connection~', page, datetime.now())
				self.rc.lpush('patent_api_error', comp)
				print('program over...')
				sys.exit(1)
			except Exception as e:
				if '1366, "Incorrect string value' in e.__str__():
					print(only_id, '~~Incorrect string value~~', page, datetime.now())
					self.rc.lpush('patent_api_error', comp)
				elif '(1406, "Data too long' in e.__str__():
					print(only_id, '~~Data too long~~', page, datetime.now())
					self.rc.lpush('patent_api_error', comp)
				else:
					print(only_id, '~~unknow error~~', page, datetime.now())
					print(e)
					self.rc.lpush('patent_api_error', comp)
					print('program over...')
					sys.exit(1)
			time.sleep(0.5)


if __name__ == '__main__':
	patent = PatentApi()
	patent.main()
