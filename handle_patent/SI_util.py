# coding:utf-8
import pymysql
import traceback
import os
import sys
import logging
import io
import time

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

path = os.path.abspath(os.path.dirname(__file__))
sys.path.append(path)

logger = logging.getLogger(__name__)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s %(name)s- %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)


def selectFun(columns, tab, start, num, db='spider'):
	"""
	查询并返回结果
	参数：字段，表
	:return:
	"""
	select_sql = """select {columns} from {tab} limit {start}, {num}""".format(
		columns=columns, tab=tab, start=start, num=num)
	print(select_sql)
	select_con, select_cur = _sqlObj(db)
	try:
		select_cur.execute(select_sql)
		results = select_cur.fetchall()
		return results
	except:
		traceback.print_exc()
	finally:
		select_con.close()
	return None


# def insertFun(insert_con, insert_cur, tab, columns, args):
# 	"""
# 	结果插入表
# 	参数：表， 字段， 字段值
# 	"""
# 	insert_sql = """insert into {tab} {columns} VALUES (%s, %s)""".format(tab=tab, columns=columns)
#
# 	insert_cur.execute(insert_sql, args)
# 	insert_con.commit()


def insertManyFun(tab, columns, args_list):
	"""
	结果插入表，批量，不利于
	参数：表， 字段， 字段值
	"""
	col_num = len(columns.split(', '))
	insert_sql = """insert into {tab} {columns} VALUES {val}""".format(tab=tab, columns=columns,
	                                                                   val=_handle_str(col_num))
	print(insert_sql)
	insert_con, insert_cur = _sqlObj('spider')
	try:
		insert_cur.execute(insert_sql, args_list)
		insert_con.commit()
	except:
		traceback.print_exc()
	finally:
		insert_con.close()


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


def _sqlObj(db):
	"""
	etl1.innotree.org
	参数：数据库
	"""
	connect = pymysql.connect(host='172.31.215.38', port=3306, user='spider', password='spider', db=db,
	                          charset='utf8', cursorclass=pymysql.cursors.DictCursor)
	cursor = connect.cursor()
	return connect, cursor

# def _sqlObj1(db):
# 	"""
# 	10.252.0.52
# 	参数：数据库
# 	"""
# 	connect = pymysql.connect(host='10.252.0.52', port=3306, user='etl_tmp', password='UsF4z5HE771KQpra', db=db,
# 	                          charset='utf8', cursorclass=pymysql.cursors.DictCursor)
# 	cursor = connect.cursor()
# 	return connect, cursor


def main(*args):
	words = ["纳米发电机", "纳米发电模组", "纳米传感器", "NEMS", "纳机电系统", "纳米发电薄膜", "纳米风力发电薄膜", "纳米风力发电", "纳米摩擦传感电缆", "纳米摩擦", "纳米传感电缆",
	         "纳米摩擦电缆", "纳米传感带", "纳米自发电鞋", "纳米发电鞋", "压电传感器", "生理监测传感带", "生理信号采集传感带", "纳米自发电鞋",
	         "自发光鞋", "智能计步鞋", "追踪鞋", "智能看护鞋", "足部理疗鞋", "自发电防伪", "高端酒防伪", "化妆品防伪", "物流防伪", "药品防伪", "纳米防伪", "微纳传感器",
	         "微型能量收集", "石墨烯微型超级电容器", "石墨烯超级电容器", "石墨烯微型电容器", "石墨烯电容器", "压电传感电缆", "压电传感电缆", "纳米氧化锌", "紫外线传感器",
	         "硅基紫外线传感器", "气流传感器", "气动传感（器）", "电子烟传感器", "雾化器传感器", "通用雾化器传感器", "医用雾化器传感器", "气体检测传感器", "智能睡眠传感器",
	         "智能枕头传感器", "居家养老监护器", "智能床垫传感器", "智能坐垫传感器"]
	columns_list = args[0].split(',')
	num = len(columns_list)
	start = i = 0
	while True:
		results = selectFun(args[0], args[1], start, 500000, db=args[2])
		if not results:
			# time.sleep(600)
			# continue
			return
		start += len(results)
		# value_list = []
		for result in results:
			i += 1
			# title, abs, pubnumber, appdate, applicantname, appcoun, guanjianzi
			if result['appcoun'] != 'CN' or result['title'].replace(' ', '').isalpha():
				continue
			som = result['title'] + result['abs']
			is_have = False
			for w in words:
				if w not in som:
					continue
				else:
					print(i, result['title'])
					result['appcoun'] = w
					is_have = True
			if '可自发电' in som and '纳米' in som:
				print(i, result['title'])
				result['appcoun'] = '可自发电+纳米'
				is_have = True
			if not is_have:
				continue
			# # 去空
			# n = 0
			# for val in result.values():
			# 	if val == '' or val is None:
			# 		n += 1
			# if n >= num - 1:
			# 	continue
			values = [result[columns_list[i].strip()] for i in range(num)]
			insertManyFun(args[3], args[4], values)

		# 	value_list.append(values)
		# 	if len(value_list) == 5:
		# 		insertManyFun(args[3], args[4], value_list)
		# 		value_list.clear()
		# 	else:
		# 		continue
		# insertManyFun(args[3], args[4], value_list)


if __name__ == '__main__':
	# select_columns = "quan_cheng, logo"
	# select_table = "tyc_jichu_chuisou"
	#
	# insert_table = "comp_logo_tyc"
	# insert_columns = "(comp_full_name, logo_url)"
	# args = [select_columns, select_table, insert_table, insert_columns]
	# main(*args)
	pass
