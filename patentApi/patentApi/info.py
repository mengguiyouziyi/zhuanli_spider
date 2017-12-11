import pymysql
from rediscluster import StrictRedisCluster

############################ redis info ############################
startup_nodes = [{"host": "172.29.237.209", "port": "7000"},
                 {"host": "172.29.237.209", "port": "7001"},
                 {"host": "172.29.237.209", "port": "7002"},
                 {"host": "172.29.237.214", "port": "7003"},
                 {"host": "172.29.237.214", "port": "7004"},
                 {"host": "172.29.237.214", "port": "7005"},
                 {"host": "172.29.237.215", "port": "7006"},
                 {"host": "172.29.237.215", "port": "7007"},
                 {"host": "172.29.237.215", "port": "7008"}]
# rc = StrictRedisCluster(startup_nodes=startup_nodes, decode_responses=True)

############################ mysql info ############################
# etl
etl_conf = {'host': '172.31.215.44', 'port': 3306, 'user': 'base', 'password': 'imkloKuLiqNMc6Cn', 'charset': 'utf8mb4',
            'cursorclass': pymysql.cursors.DictCursor}
etl = pymysql.connect(**etl_conf)
etl.select_db('spider')

# online_conf = etl_conf.copy()
# online_conf.update({'host': '172.31.215.33'})
# # online = pymysql.connect(**online_conf)
# # online.select_db('spider')
#
# kaifa_conf = etl_conf.copy()
# kaifa_conf.update({'host': '172.31.215.36'})
# # kaifa = pymysql.connect(**kaifa_conf)
# # kaifa.select_db('innotree_data_assessment')
#
# panshi_conf = etl_conf.copy()
# panshi_conf.update({'host': '172.31.215.37'})
# # panshi = pymysql.connect(**panshi_conf)
# # panshi.select_db('spider')
#
# weisaite_conf = etl_conf.copy()
# weisaite_conf.update({'host': '172.31.215.45'})
# # weisaite = pymysql.connect(**weisaite_conf)
# # weisaite.select_db('spider')

############################ user info ############################
key_list = ['pid', 'tic', 'tie', 'tio', 'ano', 'ad', 'pd', 'pk', 'pno', 'apo', 'ape', 'apc', 'ipc', 'lc',
            'vu', 'abso', 'abse', 'absc', 'imgtitle', 'imgname', 'lssc', 'pdt', 'debec', 'debeo', 'debee',
            'imgo', 'pdfexist', 'ans', 'pns', 'sfpns', 'inc', 'ine', 'ino', 'agc', 'age', 'ago', 'asc',
            'ase', 'aso', 'exc', 'exe', 'exo']
############################ sql info ############################
"""
create table zhuanli_qian_100 
select only_id, comp_full_name, totle from 
(select distinct origin_id, only_id, comp_full_name, totle from zhuanli_info_all UNION all 
select distinct origin_id, only_id, comp_full_name, totle from zhuanli_info_all_0 UNION all
select distinct origin_id, only_id, comp_full_name, totle from zhuanli_info_all_1 UNION all
select distinct origin_id, only_id, comp_full_name, totle from zhuanli_info_all_2 UNION all
select distinct origin_id, only_id, comp_full_name, totle from zhuanli_info_all_3 UNION all
select distinct origin_id, only_id, comp_full_name, totle from zhuanli_info_all_4 UNION all
select distinct origin_id, only_id, comp_full_name, totle from zhuanli_info_all_5 UNION all
select distinct origin_id, only_id, comp_full_name, totle from zhuanli_info_all_6 UNION all
select distinct origin_id, only_id, comp_full_name, totle from zhuanli_info_all_7 UNION all
select distinct origin_id, only_id, comp_full_name, totle from zhuanli_info_all_8 UNION all
select distinct origin_id, only_id, comp_full_name, totle from zhuanli_info_all_9)b;
"""
