from info import etl, result_etl, online

sql = """select * from patent_nami_chaifen"""
etl_cur = etl.cursor()
etl_cur.execute(sql)
results = etl_cur.fetchall()
etl_cur.close()
