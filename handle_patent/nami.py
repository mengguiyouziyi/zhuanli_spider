import pymysql

config = {'host': '172.31.215.38',
          'port': 3306,
          'user': 'spider',
          'password': 'spider',
          'db': 'spider',
          'charset': 'utf8',
          'cursorclass': pymysql.cursors.DictCursor}
connect = pymysql.connect(**config)
cur = connect.cursor()

sql = """select * from patent_nami"""
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
			in_sql = """insert into patent_nami_chaifen (pubNumber, appDate, title, applicantName, abs, guanjianzi) VALUES (%s, %s, %s, %s, %s, %s)"""
			cur.execute(in_sql, (
				result['pubNumber'], result['appDate'], result['title'], result['applicantName'], result['abs'],
				result['guanjianzi']))
			connect.commit()
			print(result['applicantName'])
