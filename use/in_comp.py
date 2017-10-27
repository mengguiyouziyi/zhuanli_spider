import xlrd
import hashlib
import pymysql
import traceback


def xml_rows_num(xml_path):
	"""
	返回xml文件行数
	:param xml_path:
	:return:
	"""
	book = xlrd.open_workbook(xml_path)
	sheet = book.sheet_by_index(0)
	rows = sheet.nrows
	return rows


def xml_every_row(xml_path, row_num):
	"""
	通过行数迭代
	:param xml_path:
	:param row_num:
	:return:
	"""
	book = xlrd.open_workbook(xml_path)
	sheet = book.sheet_by_index(0)
	vals = sheet.row_values(row_num)  # list，含有一列的所有信息
	only_id = gen_id(vals[1])
	vals.insert(1, only_id)
	return vals


def read_xml_gen(xml_path):
	"""
	还是要读取
	:return:
	"""
	book = xlrd.open_workbook(xml_path)
	sheet = book.sheet_by_index(0)
	rows = sheet.nrows
	print(rows)
	for row in range(1, rows + 1):
		vals = sheet.row_values(row)  # list，含有一列的所有信息
		# only_id = gen_id(vals[1])
		# vals.insert(1, only_id)
		yield vals


def read_xml(xml_path):
	"""
	读取excel表
	:return:
	"""
	book = xlrd.open_workbook(xml_path)
	sheet = book.sheet_by_index(0)
	rows = sheet.nrows
	val_all = []
	for row in range(1, rows):
		vals = sheet.row_values(row)  # list，含有一列的所有信息
		only_id = gen_id(vals[1])
		vals.insert(1, only_id)
		# vals.append(only_id)
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
	# sql = """insert into zhuanli_wai_comp (only_id, comp_full_name, hangye, zihangye, guoji, diqu, shengqingliang) VALUES (%s, %s, %s, %s, %s, %s, %s)"""
	# vl_list = [val[1:8] for val in vals]
	sql = """insert into zhuanli_wai_comp (comp_full_name) VALUES (%s)"""
	vl_list = [val[0:1] for val in vals]
	cur.executemany(sql, vl_list)
	connect.commit()


def main():
	val_all = read_xml_gen('/Users/menggui/Desktop/project/zhuanli_spider/use/科技金融-国外（来源36kr）.xlsx')
	config = {'host': 'etl2.innotree.org',
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
			if len(x) == 1:
				in_comp(connect, x)
				x.clear()
			else:
				continue
		in_comp(connect, x)
	except:
		traceback.print_exc()
	finally:
		connect.close()


if __name__ == '__main__':
	main()
