import requests
import time
import traceback
import pymysql
import math
import json
from getToken import get_token


def get_api(access_token):
	"""
	用于测试
		{"error":"invalid_token","error_description":"Invalid access token: 30e0b80a-9d22-4129-8607-46d749d97c53"}
		23d4daa7-29f9-4ebb-baa0-5d5d5d0c51ab
	"""
	connect = pymysql.connect(host='etl2.innotree.org', port=3308, user='spider', password='spider', db='spider',
	                          charset='utf8', cursorclass=pymysql.cursors.DictCursor)
	cursor = connect.cursor()
	sql = """select comp_full_name from zhuanli_shenqing_comp limit 12000"""
	cursor.execute(sql)
	results = cursor.fetchall()
	words = [result.get('comp_full_name', '') for result in results]
	url = "http://114.251.8.193/api/patent/search/expression"
	# words = ['中兴通讯股份有限公司', '三星电子株式会社']

	for j in words:
		for i in range(100):
			querystring = {"client_id": "6050f8adac110002270d833aed28242d",
			               "access_token": access_token,
			               # "access_token": "30e0b80a-9d22-4129-8607-46d749d97c53",
			               "scope": "read_cn", "express": "申请人=%s" % j, "page": "%s" % i, "page_row": "100"}
			try:
				response = requests.request("GET", url, params=querystring, timeout=5)
				info = json.loads(response.text)
				errorCode = info.get('errorCode')
				page = info.get('page')
				print(page)
				total = info.get('total')
				print(total)
				if errorCode == "000000":
					records = info.get('context').get('records')
					print(len(records))
				print(response.text)
				time.sleep(0.5)
			except:
				traceback.print_exc()
				continue


def get_comp(connect):
	"""
	从数据库获取公司列表
	:return:
	"""
	cur = connect.cursor()
	sql = """select only_id, comp_full_name from zhuanli_shenqing_comp limit 100000"""
	cur.execute(sql)
	results = cur.fetchall()
	return results


def _handle_str(num):
	"""
	根据插入字段数量来构造sql语句
	:param num: 插入字段数量
	:return: sql的value字符串
	"""
	x = "(%s"
	y = ", %s"
	for i in range(num - 1):
		x += y
	return x + ')'


def _get_column(con, table_in):
	sql = """select group_concat(column_name) from information_schema.columns WHERE table_name = '{a}' and table_schema = '{b}'""".format(
		a=table_in, b='spider_dim')
	cur = con.cursor()
	cur.execute(sql)
	results = cur.fetchall()
	columns = results[0]['group_concat(column_name)'][3:-10]
	return columns


def in_zhuanli(insert_con, tab, args_list):
	columns_a = _get_column(insert_con, tab)
	col_num = len(columns_a.split(','))
	columns = '(' + columns_a + ')'
	insert_sql = """insert into {tab} {columns} VALUES {val}""".format(tab=tab, columns=columns,
	                                                                   val=_handle_str(col_num))
	insert_cur = insert_con.cursor()

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
	response = requests.request("GET", "http://114.251.8.193/api/patent/search/expression", params=querystring,
	                            timeout=5)
	return response


def parse_page(token, proposer, page):
	response = get_res(token, proposer, page)
	# 解析response，获得totle
	info = json.loads(response.text)
	errorCode = info.get('errorCode')
	# 如果token过期了，递归调用自身
	if not errorCode:
		token = get_token()
		parse_page(token, proposer, page)
	# 如果没过期，但返回错误
	if errorCode != "000000":
		return None
	# page = info.get('page')
	total = info.get('total')
	records = info.get('context').get('records')
	values = [record.values() for record in records]
	return (total, values)


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
	print(token)
	# page=1，获取response
	for result in results:
		proposer = result.get('comp_full_name')
		response1 = parse_page(token, proposer, 1)
		if not response1:
			continue
		(total1, values1) = response1
		# 通过total确定循环次数
		# 加入9999次，pages=100页
		pages = math.ceil(int(total1) / 100)
		if pages == 1:
			# 直接入库  doing
			in_zhuanli(connect, 'zhuanli_info', values1)
			continue
		for p in range(2, pages + 1):
			response = parse_page(token, proposer, p)
			if not response:
				continue
			(total, values) = response
			in_zhuanli(connect, 'zhuanli_info', values)


if __name__ == '__main__':
	# access_token = get_token()
	# print(access_token)
	# get_api(access_token)
	# get_api('23d4daa7-29f9-4ebb-baa0-5d5d5d0c51ab')
	main()