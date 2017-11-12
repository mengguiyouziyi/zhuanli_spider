from info import etl, result_etl, online

sql = """select * from patent_nami_chaifen"""
etl_cur = etl.cursor()
etl_cur.execute(sql)
results = etl_cur.fetchall()
etl_cur.close()
jieguo_list = []
for result in results:
	# 在当前的result下面
	applicantName = result['applicantName']

	# lian_sql = """select first_name, second_name, third_name, fourth_name from company_chain_info WHERE comp_full_name = %s"""
	# on_cur = online.cursor()
	# on_cur.execute(lian_sql, (applicantName,))
	# lian_results = on_cur.fetchall()
	# on_cur.close()
	# if len(lian_results) == 0:
	# 	jieguo_list.append(result)
	# 	continue
	# for lian_result in lian_results:
	# 	x = result.copy()
	# 	x.update(lian_result)
	# 	jieguo_list.append(x)

	# intro_sql = """select intro from comp_intro_result WHERE comp_full_name = %s"""
	# etl_cur_1 = result_etl.cursor()
	# etl_cur_1.execute(intro_sql, (applicantName,))
	# intro_results = etl_cur_1.fetchall()
	# etl_cur_1.close()
	# if len(intro_results) == 0:
	# 	jieguo_list.append(result)
	# for intro_result in intro_results:
	# 	jian_result = result.copy()
	# 	jian_result.update(intro_result)
	# 	jieguo_list.append(jian_result)
	# print(1)

	fund_sql = """select invest_date, invest_stage, invest_money_num, comp_full_name from company_financing WHERE invest_name = %s"""
	on_cur_1 = online.cursor()
	on_cur_1.execute(fund_sql, (applicantName,))
	fund_results = on_cur_1.fetchall()
	on_cur_1.close()
	if len(fund_results) == 0:
		jieguo_list.append(result)
	for fund_result in fund_results:
		x = result.copy()
		x.update(fund_result)
		jieguo_list.append(x)
	print(1)




for result in jieguo_list:
	in_sql = """insert into patent_nami_all_invest 
(pubNumber, title, abs, appDate, guanjianzi, applicantName, first_name, second_name, 
third_name, fourth_name, intro, invest_date, invest_stage, invest_money_num, comp_full_name) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
	etl_cur_2 = etl.cursor()
	etl_cur_2.execute(in_sql, (
		result.get('pubNumber', ''), result.get('title', ''), result.get('abs', ''),
		result.get('appDate', ''), result.get('guanjianzi', ''), result.get('applicantName', ''),
		result.get('first_name', ''), result.get('second_name', ''), result.get('third_name', ''),
		result.get('fourth_name', ''), result.get('intro', ''), result.get('invest_date', ''),
		result.get('invest_stage', ''), result.get('invest_money_num', ''), result.get('comp_full_name', '')
	))
	etl.commit()
	etl_cur_2.close()
	print(result['applicantName'])

# intro_sql = """select intro from comp_intro_result WHERE comp_full_name = %s"""
# etl_cur_1 = result_etl.cursor()
# etl_cur_1.execute(intro_sql, (applicantName,))
# intro_results = etl_cur_1.fetchall()
# etl_cur_1.close()
# for intro_result in intro_results:
# 	jian_result = result.copy()
# 	jian_result.update(intro_result)
# 	in_jian_sql = """insert into patent_chain_intro (pubNumber, title, abs, appDate, guanjianzi, applicantName, first_name, second_name, third_name, fourth_name, intro) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
# 	in_jian_cur = etl.cursor()
# 	in_jian_cur.execute(in_jian_sql, (
# 		jian_result['pubNumber'], jian_result['title'], jian_result['abs'], jian_result['appDate'],
# 		jian_result['guanjianzi'], jian_result['applicantName'], jian_result['first_name'],
# 		jian_result['second_name'], jian_result['third_name'], jian_result['fourth_name'],
# 		jian_result['intro']))
# 	etl.commit()
# 	in_jian_cur.close()
# 	print('intro', jian_result['applicantName'])
#
# fund_sql = """select invest_date, invest_stage, invest_money_num, comp_full_name from company_financing WHERE invest_name = %s"""
# on_cur_1 = online.cursor()
# on_cur_1.execute(fund_sql, (applicantName,))
# fund_results = on_cur_1.fetchall()
# for fund_result in fund_results:
# 	result.update(fund_result)
# 	in_fund_sql = """insert into patent_chain_invest (guanjianzi, applicantName, first_name, second_name, third_name, fourth_name, invest_date, invest_stage, invest_money_num, comp_full_name) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
# 	in_fund_cur = etl.cursor()
# 	in_fund_cur.execute(in_fund_sql, (
# 		result['guanjianzi'], result['applicantName'], result['first_name'], result['second_name'],
# 		result['third_name'], result['fourth_name'], result['invest_date'], result['invest_stage'],
# 		result['invest_money_num'], result['comp_full_name']))
# 	etl.commit()
# 	in_fund_cur.close()
# 	print('invest', result['applicantName'])
etl.close()
result_etl.close()
online.close()
