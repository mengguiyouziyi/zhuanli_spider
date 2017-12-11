import pymysql

etl_conf = {'host': '172.31.215.44',
            'port': 3306,
            'user': 'spider',
            'password': 'spider',
            'charset': 'utf8mb4',
            'cursorclass': pymysql.cursors.DictCursor}
etl = pymysql.connect(**etl_conf)
etl.select_db('spider')

sql = """insert into patent_cnipr_all_copy (origin_id) VALUES (%s)"""
cursor = etl.cursor()
cursor.execute(sql, (1,))
etl.commit()
