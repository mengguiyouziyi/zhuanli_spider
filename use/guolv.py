
from utility.info import etl, kaifa

sql_che = """select comp_id from comp_list_chelianwang"""
cur_che = kaifa.cursor()
cur_che.execute(sql_che)
results_che = cur_che.fetchall()

cur_zhuanli = etl.cursor()
aux = []
zhuanli_dicts = []
for i, r_che in enumerate(results_che):
	print('zhao ', i)
	if len(aux) == 500:
		sql_zhuanli = """select only_id, comp_full_name, shengqingliang from zhuanli_shenqing_comp where only_id in {ids}""".format(
			ids=str(tuple(aux)))
		cur_zhuanli.execute(sql_zhuanli)
		results_zhuanli = cur_zhuanli.fetchall()
		zhuanli_dicts.extend(results_zhuanli)
		aux.clear()
	else:
		aux.append(r_che['comp_id'])
		continue
sql_zhuanli = """select only_id, comp_full_name, shengqingliang from zhuanli_shenqing_comp where comp_id in {ids}""".format(
	ids=str(tuple(aux)))
cur_zhuanli.execute(sql_zhuanli)
results_zhuanli = cur_zhuanli.fetchall()
zhuanli_dicts.extend(results_zhuanli)


aux_che = []
sql_in = """insert into zhuanli_shenqing_che (only_id, comp_full_name, shengqingliang) VALUES (%s, %s, %s)"""
for j, d in enumerate(zhuanli_dicts):
	print('cha ', j)
	if len(aux_che) == 500:
		cur_zhuanli.executemany(sql_in, aux_che)
		etl.commit()
		aux_che.clear()
	else:
		aux_che.append(d)
		continue
cur_zhuanli.executemany(sql_in, aux_che)
etl.commit()

etl.close()
