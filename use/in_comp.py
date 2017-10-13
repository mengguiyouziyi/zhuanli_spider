import xlrd
import hashlib
import pymysql
import traceback


def read_xml(xml_path):
	"""
	读取excel表
	:return:
	"""
	book = xlrd.open_workbook(xml_path)
	sheet = book.sheet_by_index(0)
	rows = sheet.nrows
	val_all = []
	for row in range(1, rows + 1):
		vals = sheet.row_values(row)  # list，含有一列的所有信息
		only_id = gen_id(vals[1])
		vals.append(only_id)
		val_all.append(vals)
	return val_all


def gen_id(comp_name):
	"""
	生成唯一id
	:return:
	"""
	m = hashlib.md5()
	m.update(comp_name.encode('utf-8'))
	comp_md5 = m.hexdigest()
	only_id_full = int(comp_md5, 16)
	return str(only_id_full)


def in_comp(connect, vals):
	"""
	向数据库写入公司
	:return:
	"""
	cur = connect.cursor()
	sql = """insert into zhuanli_shenqing_comp (comp_full_name, only_id'IMGTITLE', 'lssc', 'abso', 'tie', 'vu', 'absc', 'tio', 'abse', 'inc', 'pdfexist', 'agc', 'ape', 'apc', 'IMGNAME', 'ano', 'tic', 'ans', 'apo', 'ino', 'pns', 'pdt', 'ine', 'pid', 'pno', 'IMGO', 'pd', 'ipc', 'ad', 'ago', 'sfpns', 'pk']) VALUES (%s, %s, %s, %s, %s, %s, %s)"""
	vl_list = [val[1:8] for val in vals]
	cur.executemany(sql, vl_list)
	connect.commit()


if __name__ == '__main__':
	val_all = read_xml('申请人名单大全.xlsx')
	config = {'host': 'etl1.innotree.org',
	          'port': 3308,
	          'user': 'spider',
	          'password': 'spider',
	          'db': 'spider',
	          'charset': 'utf8',
	          'cursorclass': pymysql.cursors.DictCursor}
	connect = pymysql.connect(**config)
	try:
		x = []
		for i, v in enumerate(val_all):
			print(i)
			x.append(v)
			if len(x) == 100000:
				in_comp(connect, x)
				x.clear()
			else:
				continue
		in_comp(connect, x)
	except:
		traceback.print_exc()
	finally:
		connect.close()
