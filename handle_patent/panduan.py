from hashlib import md5
from info import etl, result_etl, online

cur = etl.cursor()
sql = """select * from patent_nami_chonggao"""
cur.execute(sql)
results = cur.fetchall()
for i, result in enumerate(results):
	pubNumber = result.get('pubNumber', '')
	title = result.get('title', '')
	intro = result.get('intro', '')
	text = title + intro
	word_1, word_2 = "可自发电+纳米".split('+')
	if word_1 in text and word_2 in text:
		print(i, pubNumber)
