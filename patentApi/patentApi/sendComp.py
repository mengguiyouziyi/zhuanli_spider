# coding:utf-8
import os
import sys
from os.path import dirname

father_path = dirname(dirname(os.path.abspath(dirname(__file__))))
base_path = dirname(dirname(os.path.abspath(dirname(__file__))))
path = dirname(os.path.abspath(dirname(__file__)))
sys.path.append(path)
sys.path.append(base_path)
sys.path.append(father_path)

from util.info import startup_nodes, etl
from rediscluster import StrictRedisCluster
from math import ceil


def send_key(key):
	rc = StrictRedisCluster(startup_nodes=startup_nodes, decode_responses=True)
	cursor = etl.cursor()
	sql = """select origin_id, only_id, comp_full_name, total from zhuanli_qian_100"""
	cursor.execute(sql)
	results = cursor.fetchall()
	for result in results:
		origin_id = result['origin_id']
		only_id = result['only_id']
		comp_full_name = result['comp_full_name']
		total = result['total']
		int_total = int(total)
		if int_total < 101:
			continue
		elif int_total > 10000:
			int_total = 10000
		page_num = ceil(int_total / 100)
		for page in range(2, page_num + 1):
			value = str(origin_id) + '~' + str(only_id) + '~' + comp_full_name + '~' + str(total) + '~' + str(page)
			rc.lpush(key, value)


if __name__ == '__main__':
	send_key(key='patent_api_comp')
