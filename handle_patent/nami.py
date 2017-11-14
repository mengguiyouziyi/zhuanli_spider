from info import etl, result_etl, online

cur = etl.cursor()

sql = """select * from patent_nami_chonggao"""
cur.execute(sql)
results = cur.fetchall()
s = set()
for result in results:
	ss = result['pubNumber'] + result['applicantName']
	if ss in s:
		continue
	else:
		s.add(ss)
		names = result['applicantName'].split(';')
		for n in names:
			result['applicantName'] = n
			in_sql = """insert into patent_nami_chaifen_chonggao (pubNumber, appDate, title, applicantName, abs, guanjianzi) VALUES (%s, %s, %s, %s, %s, %s)"""
			cur.execute(in_sql, (
				result['pubNumber'], result['appDate'], result['title'], result['applicantName'], result['abs'],
				result['guanjianzi']))
			etl.commit()
			print(result['applicantName'])
