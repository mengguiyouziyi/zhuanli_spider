import pymysql, time, traceback, requests, json


def get_api(access_token):
	"""
	用于测试
		{"error":"invalid_token","error_description":"Invalid access token: 30e0b80a-9d22-4129-8607-46d749d97c53"}
		23d4daa7-29f9-4ebb-baa0-5d5d5d0c51ab
	"""
	connect = pymysql.connect(host='etl2.innotree.org', port=3308, user='spider', password='spider', db='spider',
	                          charset='utf8', cursorclass=pymysql.cursors.DictCursor)
	cursor = connect.cursor()
	sql = """select comp_full_name from zhuanli_shenqing_comp limit 12000"""
	cursor.execute(sql)
	results = cursor.fetchall()
	words = [result.get('comp_full_name', '') for result in results]
	url = "http://114.251.8.193/api/patent/search/expression"
	# words = ['中兴通讯股份有限公司', '三星电子株式会社']

	for j in words:
		for i in range(100):
			querystring = {"client_id": "6050f8adac110002270d833aed28242d",
			               "access_token": access_token,
			               # "access_token": "30e0b80a-9d22-4129-8607-46d749d97c53",
			               "scope": "read_cn", "express": "申请人=%s" % j, "page": "%s" % i, "page_row": "100"}
			try:
				response = requests.request("GET", url, params=querystring, timeout=5)
				info = json.loads(response.text)
				errorCode = info.get('errorCode')
				page = info.get('page')
				print(page)
				total = info.get('total')
				print(total)
				if errorCode == "000000":
					records = info.get('context').get('records')
					print(len(records))
				print(response.text)
				time.sleep(0.5)
			except:
				traceback.print_exc()
				continue


x = {'IMGTITLE': '缩略图',
     'lssc': '2',
     'abso': '本发明属于耐火材料的测量领域。更适用于耐火材料随温度变化时电阻率连续测量的方法与设备。该设备的组成是在炉体内的固定座上卡有涂防氧化涂料的被测试样，并采用机械传导机构根据设计者要求，对试样施加适量压力，在测量时为防止试样氧化应采用保护气体保护加热。本发明测试方法与设备与现有技术相比较具有测量范围宽，测量精度高，可比性强，而且相对省时经济。',
     'tie': 'Method and device for measuring resistivity of carbon-contained refractory material',
     'vu': '39.34000015258789',
     'absc': '本发明属于耐火材料的测量领域。更适用于耐火材料随温度变化时电阻率连续测量的方法与设备。该设备的组成是在炉体内的固定座上卡有涂防氧化涂料的被测试样，并采用机械传导机构根据设计者要求，对试样施加适量压力，在测量时为防止试样氧化应采用保护气体保护加热。本发明测试方法与设备与现有技术相比较具有测量范围宽，测量精度高，可比性强，而且相对省时经济。',
     'tio': '测量含碳耐火材料电阻率的方法及设备',
     'abse': 'The present invention relates to a method suitable for continuously measuring the resistivity of refractory material along with temperature changes, and equipment thereof. The present invention belongs to the field of the measurement of refractory material. The equipment is formed by that a measured test sample coated with oxidation prevention paint is clamped on a fixed seat in a stove body, a proper amount of pressure is applied to the test sample by a machine conducting mechanism according to the requirements of the designer, and heating is protected by protective gas in order to prevent the test sample from oxidizing during measurement. Compared with the prior art, the test method and the equipment of the present invention have the advantages of wide measuring range, high measuring precision, strong comparability, comparative time saving and economy.',
     'inc': '刘开琪;李林;许胜西',
     'pdfexist': '1',
     'agc': '金向荣',
     'ape': 'General Inst. of Iron and Steel, Ministry of Metallurgical Industry',
     'age': 'jin xiangrong',
     'apc': '冶金工业部钢铁研究总院',
     'IMGNAME': 'http://image.zldsj.com/H/PID/CNC0/2003/1119/00000000001128/0FCF0HMLCC017C22/THB/THB.GIF',
     'ano': 'CN99122288.1',
     'tic': '测量含碳耐火材料电阻率的方法及设备',
     'ans': 'CN101999000022288',
     'apo': '冶金工业部钢铁研究总院',
     'ino': '刘开琪;李林;许胜西',
     'pns': 'CN1128355C',
     'pdt': '发明',
     'ine': 'Liu Kaiqi;Li Lin;Xu Shengxi',
     'pid': 'PIDCNC020031119000000000011280FCF0HMLCC017C22',
     'pno': 'CN1128355C',
     'IMGO': 'http://image.zldsj.com/H/PID/CNC0/2003/1119/00000000001128/0FCF0HMLCC017C22/ABS/99122288.GIF',
     'exo': '贺文晶',
     'pd': '2003/11/19 00:00:00',
     'asc': '冶金工业部钢铁研究总院',
     'ipc': 'G01N27/18;G01R27/02',
     'ase': 'General Inst. of Iron and Steel, Ministry of Metallurgical Industry',
     'aso': '冶金工业部钢铁研究总院',
     'ad': '1999/11/10 00:00:00',
     'exc': '贺文晶',
     'ago': '金向荣',
     'sfpns': 'CN1128355C',
     'pk': 'C'}


x = 'id,pid,appNumber,pubNumber,appDate,pubDate,title,ipc,applicantName,inventroName,family,agencyName,agentName,addrProvince,addrCity,addrCounty,address,patType,abs,lprs,draws,dbName,tifDistributePath,pages,proCode,appCoun,gazettePath,gazettePage,gazetteCount,statusCode,familyNo,legalStatus,mainIpc,appResource,cl,patentWords,page'
print(x.split(','))