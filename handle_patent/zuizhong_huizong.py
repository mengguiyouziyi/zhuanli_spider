from hashlib import md5
from info import etl, result_etl, online

words = ["纳米发电机", "纳米发电模组", "纳米传感器", "NEMS", "纳机电系统", "纳米发电薄膜", "纳米风力发电薄膜", "纳米风力发电", "纳米摩擦传感电缆", "纳米摩擦",
         "纳米传感电缆",
         "纳米摩擦电缆", "纳米传感带", "纳米自发电鞋", "纳米发电鞋", "压电传感器", "生理监测传感带", "生理信号采集传感带", "纳米自发电鞋",
         "自发光鞋", "智能计步鞋", "追踪鞋", "智能看护鞋", "足部理疗鞋", "自发电防伪", "高端酒防伪", "化妆品防伪", "物流防伪", "药品防伪", "纳米防伪", "微纳传感器",
         "微型能量收集", "石墨烯微型超级电容器", "石墨烯超级电容器", "石墨烯微型电容器", "石墨烯电容器", "压电传感电缆", "压电传感电缆", "纳米氧化锌", "紫外线传感器",
         "硅基紫外线传感器", "气流传感器", "气动传感(器)", "电子烟传感器", "雾化器传感器", "通用雾化器传感器", "医用雾化器传感器", "气体检测传感器", "智能睡眠传感器",
         "智能枕头传感器", "居家养老监护器", "智能床垫传感器", "智能坐垫传感器"]
comp_names = ['纳米新能源（唐山）有限责任公司', '纳米新能源(唐山)有限责任公司', '国家纳米科学中心', '北京纳米能源与系统研究所']
bu_words = ['摩擦发电', '压力发电', '计步', '电子烟', '医疗', '温度传感器', '石墨烯']
cur = etl.cursor()
sql = """select * from patent_nami_all_invest_zong"""
cur.execute(sql)
results = cur.fetchall()
# sql = """select * from patent_nami_all_chain_sange"""
# cur.execute(sql)
# results1 = cur.fetchall()
# s = set()
# results = results0 + results1
alls = []
for result in results:
	pubNumber = result.get('pubNumber', '')
	pubNumber = pubNumber.replace('（', '(').replace('）', ')') if pubNumber else ''
	title = result.get('title', '')
	title = title.replace('（', '(').replace('）', ')') if title else ''
	abs = result.get('abs', '')
	abs = abs.replace('（', '(').replace('）', ')') if abs else ''
	appDate = result.get('appDate', '')
	appDate = appDate.replace('（', '(').replace('）', ')') if appDate else ''
	# 这里已经有了关键字了
	guanjianzi = result.get('guanjianzi', '')
	guanjianzi = guanjianzi.replace('（', '(').replace('）', ')') if guanjianzi else ''
	applicantName = result.get('applicantName', '')
	applicantName = applicantName.replace('（', '(').replace('）', ')') if applicantName else ''
	# if len(applicantName) < 4:
	# 	continue
	# if '株式会社' in applicantName:
	# 	continue
	# if '英国' in applicantName:
	# 	continue

	first_name = result.get('first_name', '')
	first_name = first_name.replace('（', '(').replace('）', ')') if first_name else ''
	second_name = result.get('second_name', '')
	second_name = second_name.replace('（', '(').replace('）', ')') if second_name else ''
	third_name = result.get('third_name', '')
	third_name = third_name.replace('（', '(').replace('）', ')') if third_name else ''
	fourth_name = result.get('fourth_name', '')
	fourth_name = fourth_name.replace('（', '(').replace('）', ')') if fourth_name else ''
	intro = result.get('intro', '')
	intro = intro.replace('（', '(').replace('）', ')') if intro else ''

	invest_date = result.get('invest_date', '')
	invest_date = invest_date.replace('（', '(').replace('）', ')') if invest_date else ''
	invest_stage = result.get('invest_stage', '')
	invest_stage = invest_stage.replace('（', '(').replace('）', ')') if invest_stage else ''
	invest_money_num = result.get('invest_money_num', '')
	invest_money_num = invest_money_num.replace('（', '(').replace('）', ')') if invest_money_num else ''
	comp_full_name = result.get('comp_full_name', '')
	comp_full_name = comp_full_name.replace('（', '(').replace('）', ')') if comp_full_name else ''
	text = title + abs
	if guanjianzi not in comp_names:
		# 关键字不在words中
		for word in words:
			if word in text:
				guanjianzi = word
				args = (pubNumber, title, abs, appDate, guanjianzi, applicantName, first_name, second_name, third_name,
				        fourth_name, intro, invest_date, invest_stage, invest_money_num, comp_full_name)
				alls.append(args)
			else:
				continue
	else:
		# 关键字在公司列表中
		for word in bu_words:
			# 遍历words列表，如果此次关键字在text中，将word复制给guanjianzi
			if word in text:
				guanjianzi = word
				args = (pubNumber, title, abs, appDate, guanjianzi, applicantName, first_name, second_name, third_name,
				        fourth_name, intro, invest_date, invest_stage, invest_money_num, comp_full_name)
				alls.append(args)
			else:
				# 如果此次没有在，guanjianzi是原来的
				continue
		# 出来了说明没有关键字，还是原来关键字
		if guanjianzi not in bu_words:
			args = (pubNumber, title, abs, appDate, guanjianzi, applicantName, first_name, second_name, third_name,
			        fourth_name, intro, invest_date, invest_stage, invest_money_num, comp_full_name)
			alls.append(args)
	# ss = str(pubNumber) + str(title) + str(abs) + str(appDate) + str(guanjianzi) + str(applicantName) + str(
	# 	first_name) + str(second_name) + str(third_name) + str(fourth_name) + str(intro) + str(invest_date) + str(
	# 	invest_stage) + str(invest_money_num) + str(comp_full_name)
	# md = md5(ss.encode('utf-8'))
	# aa = md.hexdigest()
	# if aa in s:
	# 	continue
	# else:
	# 	s.add(aa)

for a in alls:
	in_sql = """insert into patent_nami_all_invest_zong2 
(pubNumber, title, abs, appDate, guanjianzi, applicantName, first_name, second_name, third_name, fourth_name, intro, invest_date, invest_stage, invest_money_num, comp_full_name) 
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
	cur.execute(in_sql, a)
	etl.commit()
	print(a[5])
