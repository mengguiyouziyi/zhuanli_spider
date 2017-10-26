import requests
import time
import pymysql
import math
import json
from getToken import get_token


def get_comp(connect):
	"""
	从数据库获取公司列表
	:return:
	"""
	cur = connect.cursor()
	sql = """select only_id, comp_full_name from zhuanli_shenqing_comp"""
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
	columns_a = _get_column(insert_con, tab)
	col_num = len(columns_a.split(','))
	columns = columns_a
	insert_sql = """insert into {tab} ({columns}) VALUES ({val})""".format(tab=tab, columns=columns,
	                                                                       val=_handle_str(col_num))
	insert_cur = insert_con.cursor()
	# print(insert_sql)
	# print(args_list)
	insert_cur.executemany(insert_sql, args_list)
	insert_con.commit()


def get_res(access_token, proposer, page):
	"""
	返回response api
	:param access_token:
	:param proposer: 申请人
	:param page: 页码
	:return:
	"""
	querystring = {"client_id": "6050f8adac110002270d833aed28242d",
	               "access_token": access_token,
	               # "access_token": "30e0b80a-9d22-4129-8607-46d749d97c53",
	               "scope": "read_cn", "express": "申请人=%s" % proposer, "page": "%s" % page, "page_row": "100"}
	# print(querystring)
	response = requests.request("GET", "http://114.251.8.193/api/patent/search/expression", params=querystring,
	                            timeout=10)
	time.sleep(1)
	return response


def parse_page(token, proposer, page):
	"""
	解析返回的api
	:param token:
	:param proposer: 申请人
	:param page:
	:return:
	"""
	response = get_res(token, proposer, page)
	# 解析response，获得totle
	info = json.loads(response.text)
	errorCode = info.get('errorCode')
	# 如果token过期了，递归调用自身
	if not errorCode:
		print('error  ', proposer, '  ', page)
		token = get_token()
		parse_page(token, proposer, page)
	# 如果没过期，但返回错误
	# 这里要分返回什么错误，如果返回接口调用次数限制，则需要打印出当前的申请人和申请的页数；
	# 或者直接让程序阻塞，向mysql发送心跳
	if errorCode != "000000":
		print('error  ', proposer, '  ', page)
		return None
	# page = info.get('page')
	total = info.get('total')
	records = info.get('context').get('records')

	records = get_update_dicts(records)
	print(records)

	values = [list(record.values()) for record in records]
	return (total, values)


def get_update_dicts(records):
	"""
	获取更新后的字典列表
	:param records:
	:return:
	"""
	# ini_dict = {'IMGTITLE': '', 'lssc': '', 'abso': '', 'tie': '', 'vu': '', 'absc': '', 'tio': '', 'abse': '', 'inc': '', 'pdfexist': '', 'agc': '', 'ape': '', 'age': '', 'apc': '', 'IMGNAME': '', 'ano': '', 'tic': '', 'ans': '', 'apo': '', 'ino': '', 'pns': '', 'pdt': '', 'ine': '', 'pid': '', 'pno': '', 'IMGO': '', 'exo': '', 'pd': '', 'asc': '', 'ipc': '', 'ase': '', 'aso': '', 'ad': '', 'exc': '', 'ago': '', 'sfpns': '', 'pk': ''}
	ini_dict = {"pid": "", "tic": "", "tie": "", "tio": "", "ano": "", "ad": "", "pd": "", "pk": "", "pno": "",
	            "apo": "", "ape": "", "apc": "", "ipc": "", "lc": "", "vu": "", "abso": "", "abse": "", "absc": "",
	            "imgtitle": "", "imgname": "", "lssc": "", "pdt": "", "debec": "", "debeo": "", "debee": "", "imgo": "",
	            "pdfexist": "", "ans": "", "pns": "", "sfpns": "", "inc": "", "ine": "", "ino": "", "agc": "",
	            "age": "", "ago": "", "asc": "", "ase": "", "aso": "", "exc": "", "exe": "", "exo": ""}
	long_records = []
	for record in records:
		temp = ini_dict.copy()
		low = {k.lower(): v for k, v in record.items()}
		temp.update(low)
		long_records.append(temp)
	return long_records


def max_record(records):
	"""
	获取最大的record
	:param records:
	:return:
	"""
	len_list = [len(r) for r in records]
	print(max(len_list))
	max_index = len_list.index(max(len_list))
	print(records[max_index])
	ini_dict = {}.fromkeys(records[max_index].keys(), '')
	print(ini_dict)


def get_values(values, only_id, proposer, total):
	"""
	将元素添加到list行首
	:param values:
	:param only_id:
	:param proposer:
	:param total:
	:return:
	"""
	values = [[only_id, proposer, total] + value for value in values]
	return values


def main():
	# 获取公司列表
	config = {'host': 'etl1.innotree.org',
	          'port': 3308,
	          'user': 'spider',
	          'password': 'spider',
	          'db': 'spider',
	          'charset': 'utf8',
	          'cursorclass': pymysql.cursors.DictCursor}
	connect = pymysql.connect(**config)
	results = get_comp(connect)
	token = get_token()
	# print(token)
	# page=1，获取response
	for result in results:
		only_id = result.get('only_id')
		proposer = result.get('comp_full_name')
		response1 = parse_page(token, proposer, 1)
		# print(response1)
		if not response1:
			continue
		(total1, values1) = response1
		values1 = get_values(values1, only_id, proposer, total1)
		# 通过total确定循环次数
		# 加入9999次，pages=100页
		pages = math.ceil(int(total1) / 100)
		in_zhuanli(connect, 'zhuanli_info_all', values1)
		print(proposer, '  ', 1)
		if pages == 1:
			continue
		for p in range(2, pages + 1):
			response = parse_page(token, proposer, p)
			if not response:
				continue
			(total, values) = response
			values = get_values(values, only_id, proposer, total)
			in_zhuanli(connect, 'zhuanli_info_all', values)
			print(proposer, '  ', p)


if __name__ == '__main__':
	# access_token = get_token()
	# print(access_token)
	# get_api(access_token)
	# get_api('23d4daa7-29f9-4ebb-baa0-5d5d5d0c51ab')
	main()
