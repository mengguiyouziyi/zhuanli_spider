from info import etl, result_etl, online

sql = """select * from patent_nami_chaifen"""
etl_cur = etl.cursor()
etl_cur.execute(sql)
results = etl_cur.fetchall()
etl_cur.close()
for result in results:
	applicantName = result['applicantName']
	lian_sql = """select first_name, second_name, third_name, fourth_name from company_chain_info WHERE comp_full_name = %s"""
	on_cur = online.cursor()
	on_cur.execute(lian_sql, (applicantName,))
	lian_results = on_cur.fetchall()
	on_cur.close()
	for lian_result in lian_results:
		result.update(lian_result)
		# in_chain_sql = """insert into patent_chain (pubNumber, title, abs, appDate, guanjianzi, applicantName, first_name, second_name, third_name, fourth_name) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
		# etl_cur_2 = etl.cursor()
		# etl_cur_2.execute(in_chain_sql, (
		# 	result['pubNumber'], result['title'], result['abs'], result['appDate'],
		# 	result['guanjianzi'], result['applicantName'], result['first_name'],
		# 	result['second_name'], result['third_name'], result['fourth_name']))
		# etl.commit()
		# etl_cur_2.close()
		# print('chain', result['applicantName'])

		intro_sql = """select intro from comp_intro_result WHERE comp_full_name = %s"""
		etl_cur_1 = result_etl.cursor()
		etl_cur_1.execute(intro_sql, (applicantName,))
		intro_results = etl_cur_1.fetchall()
		etl_cur_1.close()
		for intro_result in intro_results:
			jian_result = result.copy()
			jian_result.update(intro_result)
			in_jian_sql = """insert into patent_chain_intro (pubNumber, title, abs, appDate, guanjianzi, applicantName, first_name, second_name, third_name, fourth_name, intro) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
			in_jian_cur = etl.cursor()
			in_jian_cur.execute(in_jian_sql, (
				jian_result['pubNumber'], jian_result['title'], jian_result['abs'], jian_result['appDate'],
				jian_result['guanjianzi'], jian_result['applicantName'], jian_result['first_name'],
				jian_result['second_name'], jian_result['third_name'], jian_result['fourth_name'],
				jian_result['intro']))
			etl.commit()
			in_jian_cur.close()
			print('intro', jian_result['applicantName'])

		fund_sql = """select invest_date, invest_stage, invest_money_num, comp_full_name from company_financing WHERE invest_name = %s"""
		on_cur_1 = online.cursor()
		on_cur_1.execute(fund_sql, (applicantName,))
		fund_results = on_cur_1.fetchall()
		for fund_result in fund_results:
			result.update(fund_result)
			in_fund_sql = """insert into patent_chain_invest (guanjianzi, applicantName, first_name, second_name, third_name, fourth_name, invest_date, invest_stage, invest_money_num, comp_full_name) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
			in_fund_cur = etl.cursor()
			in_fund_cur.execute(in_fund_sql, (
				result['guanjianzi'], result['applicantName'], result['first_name'], result['second_name'],
				result['third_name'], result['fourth_name'], result['invest_date'], result['invest_stage'],
				result['invest_money_num'], result['comp_full_name']))
			etl.commit()
			in_fund_cur.close()
			print('invest', result['applicantName'])
etl.close()
result_etl.close()
online.close()
