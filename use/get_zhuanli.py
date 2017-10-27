import requests
import time
import pymysql
import math
import json
# import logging
# from urllib.parse import quote_plus
from traceback import print_exc
from more_itertools import chunked
from collections import OrderedDict
from getToken import get_token


# # 创建一个logger
# logger = logging.getLogger('RegistAddr_Log')
# logger.setLevel(logging.DEBUG)
#
# # 创建一个handler，用于写入日志文件
# fh = logging.FileHandler('./lib/RegistAddr.log')
# # fh.setLevel(logging.DEBUG)
#
# # 定义handler的输出格式
# formatter = logging.Formatter('%(asctime)s - %(process)d - %(levelname)s - %(message)s')
# fh.setFormatter(formatter)
# logger.addHandler(fh)
# # ---------↑↑↑↑↑↑↑定义日志↑↑↑↑↑↑↑↑-----------


def get_comp(connect):
	"""
	从数据库获取公司列表
	:return:
	"""
	cur = connect.cursor()
	sql = """select id, only_id, comp_full_name from zhuanli_shenqing_comp"""
	cur.execute(sql)
	results = cur.fetchall()
	return results


def _handle_str(num):
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


def _get_column(con, table_in):
	"""
	获取mysql表 字段字符串
	:param con:
	:param table_in:
	:return:
	"""
	sql = """select group_concat(column_name) from information_schema.columns WHERE table_name = '{a}' and table_schema = '{b}'""".format(
		a=table_in, b='spider')
	cur = con.cursor()
	cur.execute(sql)
	results = cur.fetchall()
	columns = results[0]['group_concat(column_name)'][3:-10]
	return columns


def in_zhuanli(insert_con, tab, args_list):
	"""
	专利信息入库
	:param insert_con:
	:param tab:
	:param args_list:
	:return:
	"""
	l_num_str = args_list[0][1][-1]
	columns_a = _get_column(insert_con, tab + '_' + l_num_str)
	col_num = len(columns_a.split(','))
	columns = columns_a
	insert_sql = """insert into {tab} ({columns}) VALUES ({val})""".format(tab=tab + '_' + l_num_str, columns=columns,
	                                                                       val=_handle_str(col_num))
	insert_cur = insert_con.cursor()
	# 确保入库的时候都在50条以下
	l = len(args_list)
	if l >= 50:
		aux = list(chunked(args_list, math.ceil(l / 2)))
		for a in aux:
			insert_cur.executemany(insert_sql, a)
			insert_con.commit()
	else:
		insert_cur.executemany(insert_sql, args_list)
		insert_con.commit()


def get_res(token, result, page):
	"""
	返回response api
	:param access_token:
	:param proposer: 申请人
	:param page: 页码
	:return:
	"""
	id = result.get('id')
	proposer = result.get('comp_full_name', '')
	proposer = proposer.replace('(', r'\(').replace(')', r'\)')
	querystring = {"client_id": "6050f8adac110002270d833aed28242d",
	               "access_token": token,
	               "scope": "read_cn", "express": "申请人=%s" % proposer,
	               "page": "%s" % page, "page_row": "100"}
	api_url = "http://114.251.8.193/api/patent/search/expression"
	try:
		info = requests.request("GET", api_url, params=querystring, timeout=15).json()
		time.sleep(1)
	except:
		print(id, '~~timeout error~~', page)
		return
	if not info:
		print(id, '~~no info~~', page)
		return
	# info = json.loads(response.text)
	errorCode = info.get('errorCode')
	context = info.get('context')
	if not errorCode:
		print(id, '~~no errorCode~~', page)
		print(info.strip())
		return -1
	if errorCode == '000016':
		# 查询错误，最多只能返回查询条件前10000条数据
		print(id, '~~code:000016 Query error, only return the first 10000~~', page)
		return
	elif errorCode == "表达式语法错误":
		# 存在语法错误，请重新编辑表达式后进行检索
		print(id, '~~Syntax error~~', page)
		print(querystring)
		return
	elif errorCode == '000003':
		# 连接数据查询库异常
		print(id, '~~code:000003 Connecting data query base exceptions~~', page)
		return
	elif not context:
		print(id, '~~no context~~', page)
		return
	elif errorCode == '000000' and context:
		total = info.get('total')
		records = context.get('records')
		records = get_update_dicts(records)
		key_list = ['pid', 'tic', 'tie', 'tio', 'ano', 'ad', 'pd', 'pk', 'pno', 'apo', 'ape', 'apc', 'ipc', 'lc', 'vu',
		            'abso', 'abse', 'absc', 'imgtitle', 'imgname', 'lssc', 'pdt', 'debec', 'debeo', 'debee', 'imgo',
		            'pdfexist', 'ans', 'pns', 'sfpns', 'inc', 'ine', 'ino', 'agc', 'age', 'ago', 'asc', 'ase', 'aso',
		            'exc', 'exe', 'exo']
		values = [[record[i] for i in key_list] for record in records]
		return (total, values)
	else:
		print(id, '~~other error~~', page)
		print(info.strip())
		return


def get_update_dicts(records):
	"""
	获取更新后的字典列表
	:param records:
	:return:
	"""
	ini_dict = {"pid": "", "tic": "", "tie": "", "tio": "", "ano": "", "ad": "", "pd": "", "pk": "", "pno": "",
	            "apo": "", "ape": "", "apc": "", "ipc": "", "lc": "", "vu": "", "abso": "", "abse": "", "absc": "",
	            "imgtitle": "", "imgname": "", "lssc": "", "pdt": "", "debec": "", "debeo": "", "debee": "", "imgo": "",
	            "pdfexist": "", "ans": "", "pns": "", "sfpns": "", "inc": "", "ine": "", "ino": "", "agc": "",
	            "age": "", "ago": "", "asc": "", "ase": "", "aso": "", "exc": "", "exe": "", "exo": ""}
	long_records = []
	for record in records:
		temp = ini_dict.copy()
		low = {k.lower(): v for k, v in OrderedDict(record).items()}
		temp.update(low)
		long_records.append(temp)
	return long_records


def get_values(values, add_list):
	"""
	将元素添加到list行首
	:param values:
	:param only_id:
	:param proposer:
	:param total:
	:return:
	"""
	values = [add_list + value for value in values]
	return values


def main():
	config = {'host': 'etl1.innotree.org',
	          'port': 3308,
	          'user': 'spider',
	          'password': 'spider',
	          'db': 'spider',
	          'charset': 'utf8',
	          'cursorclass': pymysql.cursors.DictCursor}
	connect = pymysql.connect(**config)
	results = get_comp(connect)
	# 第一次给予token
	token = get_token()
	for result in results:
		id = result.get('id')
		only_id = result.get('only_id')
		proposer = result.get('comp_full_name')
		if id <= 934 and id not in [604, 783]:
			continue
		# 使用token获取结果, 注意使用的是循环外的token
		try:
			response = get_res(token, result, 1)
			if response == -1:
				# 如果token失效，重新获取token，下次循环的时候token也是这个新token
				token = get_token()
				response = get_res(token, result, 1)
			if not response:
				continue
			(total, values) = response
			add_list = [id, only_id, proposer, total]
			values = get_values(values, add_list)
			in_zhuanli(connect, 'zhuanli_info_all', values)
			print(id, '~~success~~', 1)
		except:
			print(id, '~~unknow error~~', 1)
			print_exc()
			continue


# def main():
# 	# 获取公司列表
# 	config = {'host': 'etl1.innotree.org',
# 	          'port': 3308,
# 	          'user': 'spider',
# 	          'password': 'spider',
# 	          'db': 'spider',
# 	          'charset': 'utf8',
# 	          'cursorclass': pymysql.cursors.DictCursor}
# 	connect = pymysql.connect(**config)
# 	results = get_comp(connect)
# 	token = get_token()
# 	# print(token)
# 	# page=1，获取response
# 	for result in results:
# 		only_id = result.get('only_id')
# 		proposer = result.get('comp_full_name')
# 		if proposer == '国家电网公司':
# 			(total1, values1) = parse_page(token, proposer, 101)
# 			if not (total1, values1):
# 				continue
# 			values1 = get_values(values1, only_id, proposer, total1)
# 			# 通过total确定循环次数
# 			# 加入9999次，pages=100页
# 			pages = math.ceil(int(total1) / 100)
# 			in_zhuanli(connect, 'zhuanli_info_all', values1)
# 			print(proposer, '  ', 101)
# 			if pages == 1:
# 				continue
# 			for p in range(102, pages + 1):
# 				(total, values) = parse_page(token, proposer, p)
# 				if not (total, values):
# 					continue
# 				values = get_values(values, only_id, proposer, total)
# 				in_zhuanli(connect, 'zhuanli_info_all', values)
# 				print(proposer, '  ', p)
# 			continue
#
# 		response1 = parse_page(token, proposer, 1)
# 		if not response1:
# 			continue
# 		(total1, values1) = response1
# 		values1 = get_values(values1, only_id, proposer, total1)
# 		# 通过total确定循环次数
# 		# 加入9999次，pages=100页
# 		pages = math.ceil(int(total1) / 100)
# 		in_zhuanli(connect, 'zhuanli_info_all', values1)
# 		print(proposer, '  ', 1)
# 		if pages == 1:
# 			continue
# 		for p in range(2, pages + 1):
# 			response = parse_page(token, proposer, p)
# 			if not response:
# 				continue
# 			(total, values) = response
# 			values = get_values(values, only_id, proposer, total)
# 			in_zhuanli(connect, 'zhuanli_info_all', values)
# 			print(proposer, '  ', p)



if __name__ == '__main__':
	# access_token = get_token()
	# print(access_token)
	# get_api(access_token)
	# get_api('23d4daa7-29f9-4ebb-baa0-5d5d5d0c51ab')
	main()

"""各种错误
{^M
338 "errorCode" : "000016",^M
339 "errorDesc" : "错误代码[000016] ==> 查询错误，最多只能返回查询条件前10000条数据",^M
340 "page_row" : "",^M
341 "page" : "",^M
342 "total" : "",^M
343 "sort_column" : "",^M
344 "context" : ""^M
345 }

{^M
 436 "errorCode" : "表达式语法错误",^M
 437 "errorDesc" : "错误代码[表达式语法错误] ==> 当前表达式：null。存在语法错误，请重新编辑表达式后进行检索。",^M
 438 "page_row" : "",^M
 439 "page" : "",^M
 440 "total" : "",^M
 441 "sort_column" : "",^M
 442 "context" : ""^M
 443 }

{^M
266 "errorCode" : "000003",^M
267 "errorDesc" : "错误代码[000003] ==> 连接数据查询库异常",^M
268 "page_row" : "100",^M
269 "page" : "1",^M
270 "total" : "",^M
271 "sort_column" : "",^M
272 "context" : ""^M
273 }^M
"""


# def max_record(records):
# 	"""
# 	获取最大的record
# 	:param records:
# 	:return:
# 	"""
# 	len_list = [len(r) for r in records]
# 	print(max(len_list))
# 	max_index = len_list.index(max(len_list))
# 	print(records[max_index])
# 	ini_dict = {}.fromkeys(records[max_index].keys(), '')
# 	print(ini_dict)
