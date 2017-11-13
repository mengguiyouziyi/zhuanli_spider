import pymysql

etl_config = {'host': '172.31.215.38',
              'port': 3306,
              'user': 'spider',
              'password': 'spider',
              'db': 'spider',
              'charset': 'utf8',
              'cursorclass': pymysql.cursors.DictCursor}
etl = pymysql.connect(**etl_config)

etl_config = {'host': '172.31.215.38',
              'port': 3306,
              'user': 'spider',
              'password': 'spider',
              'db': 'dimension_result',
              'charset': 'utf8',
              'cursorclass': pymysql.cursors.DictCursor}
result_etl = pymysql.connect(**etl_config)

on_config = {'host': '172.31.215.37',
             'port': 3306,
             'user': 'test',
             'password': '123456',
             'db': 'innotree_data_online',
             'charset': 'utf8',
             'cursorclass': pymysql.cursors.DictCursor}
online = pymysql.connect(**on_config)
