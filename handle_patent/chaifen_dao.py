from info import etl, result_etl, online

sql = """select pubNumber, title, abs, appDate, applicantName from patent where applicantName = '国家纳米科学中心' or applicantName = '纳米新能源(唐山)有限责任公司'  or applicantName = '纳米新能源（唐山）有限责任公司' or  applicantName = '北京纳米能源与系统研究所'"""
etl_cur = etl.cursor()
etl_cur.execute(sql)
results = etl_cur.fetchall()
for result in results:
	result['guanjianzi'] = result['applicantName']
	print(result['guanjianzi'])
	in_sql = """insert into patent_nami_chaifen_sange (pubNumber, title, abs, appDate, applicantName, guanjianzi) VALUES (%s, %s, %s, %s, %s, %s)"""
	etl_cur.execute(in_sql, (
		result['pubNumber'], result['title'], result['abs'], result['appDate'], result['applicantName'],
		result['guanjianzi']))
	etl.commit()
etl.close()
