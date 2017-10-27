"""
宏宇要如redis，set
"""
import os
import sys

f = os.path.abspath(os.path.dirname(__file__))
ff = os.path.dirname(f)
fff = os.path.dirname(ff)
sys.path.extend([f, ff, fff])

import pymysql
import traceback
# from use.utility.tools import get_redis_db
from use.utility.info import a024, a027, etl_config, xin_config, online_config

# a024_db = get_redis_db(a024)

etl = pymysql.connect(**etl_config)
etl.select_db('spider')
etl_cur = etl.cursor()

"""create table zhuanli_patent_wai select patent.* from patent_1 LEFT JOIN zhuanli_wai_comp on applicantName LIKE concat('%', comp_full_name, '%')"""

try:
	sql = """select comp_full_name from zhuanli_wai_comp"""
	etl_cur.execute(sql)
	results = etl_cur.fetchall()

	m = 0
	for i in range(1, 12):
		comp_full_name = [result['comp_full_name'] for result in results]
		sql_1 = """select * from patent_{0} WHERE applicantName in ({1})""".format(str(i), str(tuple(comp_full_name)))
		# sql_1 = """select * from patent_{0} WHERE applicantName LIKE '{1}'""".format(str(i), ('%' + result['comp_full_name'] + '%'))
		# print(sql_1)
		etl_cur.execute(sql_1)
		results_1 = etl_cur.fetchall()
		m += len(results_1)
		print(m)
		sql_2 = """insert into zhuanli_patent_wai (pid,appNumber,pubNumber,appDate,pubDate,title,ipc,applicantName,inventroName,family,agencyName,agentName,addrProvince,addrCity,addrCounty,address,patType,abs,lprs,draws,dbName,tifDistributePath,pages,proCode,appCoun,gazettePath,gazettePage,gazetteCount,statusCode,familyNo,legalStatus,mainIpc,appResource,cl,patentWords,page) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
		l = ['pid', 'appNumber', 'pubNumber', 'appDate', 'pubDate', 'title', 'ipc', 'applicantName', 'inventroName',
		     'family', 'agencyName', 'agentName', 'addrProvince', 'addrCity', 'addrCounty', 'address', 'patType',
		     'abs', 'lprs', 'draws', 'dbName', 'tifDistributePath', 'pages', 'proCode', 'appCoun', 'gazettePath',
		     'gazettePage', 'gazetteCount', 'statusCode', 'familyNo', 'legalStatus', 'mainIpc', 'appResource', 'cl',
		     'patentWords', 'page']
		values = [[record[i] for i in l] for record in results_1]
		etl_cur.executemany(sql_2, values)
		etl.commit()
except:
	traceback.print_exc()
finally:
	etl.close()

# try:
# 	sql = """select comp_full_name from zhuanli_wai_comp"""
# 	etl_cur.execute(sql)
# 	results = etl_cur.fetchall()
#
# 	m = 0
# 	for result in results:
# 		for i in range(1, 12):
# 			sql_1 = """select * from patent_{0} WHERE applicantName LIKE '{1}'""".format(str(i), ('%' + result['comp_full_name'] + '%'))
# 			# sql_1 = """select * from patent_{0} WHERE applicantName LIKE '{1}'""".format(str(i), ('%' + result['comp_full_name'] + '%'))
# 			# print(sql_1)
# 			etl_cur.execute(sql_1)
# 			results_1 = etl_cur.fetchall()
# 			m += len(results_1)
# 			print(m)
# 			sql_2 = """insert into zhuanli_patent_wai (pid,appNumber,pubNumber,appDate,pubDate,title,ipc,applicantName,inventroName,family,agencyName,agentName,addrProvince,addrCity,addrCounty,address,patType,abs,lprs,draws,dbName,tifDistributePath,pages,proCode,appCoun,gazettePath,gazettePage,gazetteCount,statusCode,familyNo,legalStatus,mainIpc,appResource,cl,patentWords,page) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
# 			l = ['pid', 'appNumber', 'pubNumber', 'appDate', 'pubDate', 'title', 'ipc', 'applicantName', 'inventroName',
# 			     'family', 'agencyName', 'agentName', 'addrProvince', 'addrCity', 'addrCounty', 'address', 'patType',
# 			     'abs', 'lprs', 'draws', 'dbName', 'tifDistributePath', 'pages', 'proCode', 'appCoun', 'gazettePath',
# 			     'gazettePage', 'gazetteCount', 'statusCode', 'familyNo', 'legalStatus', 'mainIpc', 'appResource', 'cl',
# 			     'patentWords', 'page']
# 			values = [[record[i] for i in l] for record in results_1]
# 			etl_cur.executemany(sql_2, values)
# 			etl.commit()
# except:
# 	traceback.print_exc()
# finally:
# 	etl.close()
