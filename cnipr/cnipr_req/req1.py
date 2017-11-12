import requests
from urllib.parse import quote_plus


def get_list_all_other():
	url = 'http://m.cnipr.com:8081/tailor/http://192.168.201.132:8080/search!doOverviewSearch4Index.AJAX-action?DATA-start=1&limit=10&strWhere=%E6%97%A0%E9%94%A1%E5%8D%93%E4%BF%A1%E4%BF%A1%E6%81%AF%E7%A7%91%E6%8A%80%E8%82%A1%E4%BB%BD%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8&yuyijs=&saveFlag=1&keyword2Save=&key2Save=&dbScope=3&type=AtTrial'
	url = 'http://m.cnipr.com:8081/tailor/http://192.168.201.132:8080/search!doOverviewSearch4Index.AJAX-action?DATA-start=1&limit=10&strWhere=%E6%97%A0%E9%94%A1%E5%8D%93%E4%BF%A1%E4%BF%A1%E6%81%AF%E7%A7%91%E6%8A%80%E8%82%A1%E4%BB%BD%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8&yuyijs=&saveFlag=1&keyword2Save=&key2Save=&dbScope=3&type=inValid'
	headers = {
		'Host': 'm.cnipr.com:8081',
		'Accept': '*/*',
		'Cookie': 'TailorID=3208de0a93dfd94e069897797de339da92c4',
		'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0_3 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Mobile/15A432',
		'Accept-Language': 'zh-cn',
		'Referer': 'http://m.cnipr.com:8081/tailor/http://192.168.201.132:8080/search!doOverviewSearch4Index.action?DATA-start=1&limit=10&strWhere=%E6%97%A0%E9%94%A1%E5%8D%93%E4%BF%A1%E4%BF%A1%E6%81%AF%E7%A7%91%E6%8A%80%E8%82%A1%E4%BB%BD%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8&yuyijs=&saveFlag=1&keyword2Save=&key2Save=&dbScope=3&type=Valid'
	}


def get_list_all():
	url = 'http://m.cnipr.com:8081/tailor/http://192.168.201.132:8080/search!doOverviewSearch4Index.action?DATA-start=1&limit=10&strWhere=%E6%97%A0%E9%94%A1%E5%8D%93%E4%BF%A1%E4%BF%A1%E6%81%AF%E7%A7%91%E6%8A%80%E8%82%A1%E4%BB%BD%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8&yuyijs=&saveFlag=1&keyword2Save=&key2Save=&dbScope=3&type=Valid'
	headers = {
		'Host': 'm.cnipr.com:8081',
		'Cookie': 'TailorID=3208de0a93dfd94e069897797de339da92c4',
		'Upgrade-Insecure-Requests': '1',
		'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
		'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0_3 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Mobile/15A432',
		'Referer': 'http://m.cnipr.com:8081/tailor/http://192.168.201.132:8080/index',
		'Accept-Language': 'zh-cn'
	}


def get_list_other():
	url = 'http://m.cnipr.com:8081/tailor/http://192.168.201.132:8080/search!doOverviewSearch4Index.AJAX-action?DATA-start=2&limit=30&strWhere=荷兰应用科学研究会(TNO)&yuyijs=&saveFlag=1&keyword2Save=&key2Save=&dbScope=3&type=AtTrial'
	# url = 'http://m.cnipr.com:8081/tailor/http://192.168.201.132:8080/search!doOverviewSearch4Index.AJAX-action?DATA-start=1&limit=10&strWhere=%E5%9B%9B%E5%B7%9D%E7%9C%81%E5%86%9C%E4%B8%9A%E6%9C%BA%E6%A2%B0%E7%A0%94%E7%A9%B6%E8%AE%BE%E8%AE%A1%E9%99%A2&yuyijs=&saveFlag=1&keyword2Save=&key2Save=&dbScope=1&type=inValid'
	headers = {
		# 'Host': 'm.cnipr.com:8081',
		# 'Accept': '*/*',
		'Cookie': 'TailorID=3208de0a93dfd94e069897797de339da92c4',
		'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0_3 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Mobile/15A432',
		# 'Accept-Language': 'zh-cn',
		# 'Referer': 'http://m.cnipr.com:8081/tailor/http://192.168.201.132:8080/search!doOverviewSearch4Index.action?DATA-start=1&limit=10&strWhere=%E5%9B%9B%E5%B7%9D%E7%9C%81%E5%86%9C%E4%B8%9A%E6%9C%BA%E6%A2%B0%E7%A0%94%E7%A9%B6%E8%AE%BE%E8%AE%A1%E9%99%A2&yuyijs=&saveFlag=1&keyword2Save=&key2Save=&dbScope=1&type=Valid'
	}
	response = requests.get(url, headers=headers).json()
	print(response['html'])


# with open('list3.html', 'a') as f:
# 	f.writelines(response.text)


def get_list():
	# url = 'http://m.cnipr.com:8081/tailor/http://192.168.201.132:8080/search!doOverviewSearch4Index.action?DATA-start=1&limit=10&strWhere=%E4%B8%AD%E5%9B%BD%E7%9F%B3%E6%B2%B9&yuyijs=&saveFlag=1&keyword2Save=&key2Save=&dbScope=1&type=Valid'
	url = 'http://m.cnipr.com:8081/tailor/http://192.168.201.132:8080/search!doOverviewSearch4Index.action?DATA-start=1&limit=30&strWhere={}&yuyijs=&saveFlag=1&keyword2Save=&key2Save=&dbScope=1&type=Valid'.format(
		quote_plus('湖南省怀化市鸿华电子科技有限公司'))
	# url = 'http://m.cnipr.com:8081/tailor/http://192.168.201.132:8080/search!doOverviewSearch4Index.action?DATA-start=1&limit=10&strWhere=%E5%9B%9B%E5%B7%9D%E7%9C%81%E5%86%9C%E4%B8%9A%E6%9C%BA%E6%A2%B0%E7%A0%94%E7%A9%B6%E8%AE%BE%E8%AE%A1%E9%99%A2&yuyijs=&saveFlag=1&keyword2Save=&key2Save=&dbScope=1&type=Valid'
	# url = 'http://m.cnipr.com:8081/tailor/http://192.168.201.132:8080/search!doOverviewSearch4Index.AJAX-action?DATA-start=1&limit=10&strWhere=%E5%9B%9B%E5%B7%9D%E7%9C%81%E5%86%9C%E4%B8%9A%E6%9C%BA%E6%A2%B0%E7%A0%94%E7%A9%B6%E8%AE%BE%E8%AE%A1%E9%99%A2&yuyijs=&saveFlag=1&keyword2Save=&key2Save=&dbScope=1&type=AtTrial'
	# url = 'http://m.cnipr.com:8081/tailor/http://192.168.201.132:8080/search!doOverviewSearch4Index.AJAX-action?DATA-start=1&limit=10&strWhere=%E5%9B%9B%E5%B7%9D%E7%9C%81%E5%86%9C%E4%B8%9A%E6%9C%BA%E6%A2%B0%E7%A0%94%E7%A9%B6%E8%AE%BE%E8%AE%A1%E9%99%A2&yuyijs=&saveFlag=1&keyword2Save=&key2Save=&dbScope=1&type=inValid'
	headers = {
		# 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
		# 'Accept-Encoding': 'gzip, deflate',
		# 'Accept-Language': 'zh-cn',
		'Connection': 'keep-alive',
		'Cookie': 'TailorID=3208de0a93dfd94e069897797de339da92c4',
		# 'Host': 'm.cnipr.com:8081',
		'Referer': 'http://m.cnipr.com:8081/tailor/http://192.168.201.132:8080/index',
		# 'Upgrade-Insecure-Requests': '1',
		'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0_3 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Mobile/15A432'
	}
	# f = 'strWhere=%E7%94%B3%E8%AF%B7%EF%BC%88%E4%B8%93%E5%88%A9%E6%9D%83%EF%BC%89%E4%BA%BA%3D%28%E4%B8%AD%E5%9B%BD%E7%9F%B3%E6%B2%B9%E5%8C%96%E5%B7%A5%E8%82%A1%E4%BB%BD%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8%29&yuyijs=&start=1&saveFlag=1&limit=10&strSynonymous=&crossLanguage=&islogicsearch=false&saveExp=&showhint=&mpage=null&channelId=FMZL&channelId=SYXX&channelId=WGZL&channelId=FMSQ&channelId=TWZL&channelId=HKPATENT&channelId=USPATENT&channelId=EPPATENT&channelId=JPPATENT&channelId=WOPATENT&channelId=GBPATENT&channelId=CHPATENT&channelId=DEPATENT&channelId=KRPATENT&channelId=FRPATENT&channelId=RUPATENT&channelId=ASPATENT&channelId=ATPATENT&channelId=GCPATENT&channelId=ITPATENT&channelId=AUPATENT&channelId=APPATENT&channelId=CAPATENT&channelId=SEPATENT&channelId=ESPATENT&channelId=OTHERPATENT&trsq=1&dan=1&txt_A=&txt_B=&txt_C=&txt_D=&txt_E=&txt_F=&txt_Q=&txt_R=&txt_I=%E4%B8%AD%E5%9B%BD%E7%9F%B3%E6%B2%B9%E5%8C%96%E5%B7%A5%E8%82%A1%E4%BB%BD%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8&txt_J=&txt_G=&txt_H=&txt_L=&txt_O=&text=&txt_K=&txt_M=&txt_N=&txt_U=&txt_T=&txt_V=&txt_X=&mpage=advsch'
	# payload = dict([m.split('=') for m in f.split('&')])
	response = requests.get(url, headers=headers)
	print(response.text)
	# with open('list3.html', 'w') as f:
	# 	f.writelines(response.text)


def get_detail():
	url = 'http://m.cnipr.com:8081/tailor/http://192.168.201.132:8080/search!doDetailSearch.action?Data=strWhere=%E5%90%8D%E7%A7%B0%2C%E7%94%B3%E8%AF%B7%EF%BC%88%E4%B8%93%E5%88%A9%E6%9D%83%EF%BC%89%E4%BA%BA%2C%E5%8F%91%E6%98%8E%EF%BC%88%E8%AE%BE%E8%AE%A1%EF%BC%89%E4%BA%BA%2C%E4%BC%98%E5%85%88%E6%9D%83%E5%8F%B7%2C%E4%B8%93%E5%88%A9%E4%BB%A3%E7%90%86%E6%9C%BA%E6%9E%84%2C%E4%BB%A3%E7%90%86%E4%BA%BA%2C%E5%9C%B0%E5%9D%80%2C%E7%94%B3%E8%AF%B7%E5%9B%BD%E4%BB%A3%E7%A0%81%2C%E5%9B%BD%E7%9C%81%E4%BB%A3%E7%A0%81%2C%E6%91%98%E8%A6%81%2C%E4%B8%BB%E6%9D%83%E9%A1%B9%20%2B%3D(%27%E4%B8%AD%E7%9F%B3%E5%8C%96%25%27)%20&start=4&recordCursor=39&limit=1&option=2&iHitPointType=115&strSortMethod=RELEVANCE&strSources=FMZL%2CSYXX%2CWGZL%2CTWZL%2CHKPATENT%2CUSPATENT%2CJPPATENT%2CEPPATENT%2CWOPATENT%2CGBPATENT%2CDEPATENT%2CFRPATENT%2CCHPATENT%2CKRPATENT%2CRUPATENT%2CAPPATENT%2CATPATENT%2CAUPATENT%2CITPATENT%2CSEPATENT%2CCAPATENT%2CESPATENT%2CGCPATENT%2CASPATENT%2COTHERPATENT%2CTWPATENT&strSynonymous=&yuyijs=&filterChannel=&otherWhere=%5B%7B%22kind%22%3A%22%E4%B8%93%E5%88%A9%E6%9D%83%E7%8A%B6%E6%80%81%22%2C%22showwhere%22%3A%22%E6%9C%89%E6%95%88%22%2C%22where%22%3A%2210%22%7D%5D&title=10.%E4%B8%80%E7%A7%8D%E5%A4%A7%E5%8F%A3%E5%BE%84%E9%AB%98%E6%B8%A9%E8%80%90%E7%A3%A8%E5%B9%B3%E6%9D%BF%E9%97%B8%E9%98%80&keyword=%E4%B8%AD%E7%9F%B3%E5%8C%96'
	headers = {
		# 'Host': 'm.cnipr.com:8081',
		'Cookie': 'TailorID=3208de0a93dfd94e069897797de339da92c4',
		# 'Upgrade-Insecure-Requests': '1',
		# 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
		'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0_3 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Mobile/15A432',
		# 'Referer': 'http://m.cnipr.com:8081/tailor/http://192.168.201.132:8080/search!doOverviewSearch4Index.action?DATA-start=1&limit=10&strWhere=%E4%B8%AD%E7%9F%B3%E5%8C%96&yuyijs=&saveFlag=1&keyword2Save=&key2Save=&dbScope=3&type=Valid',
		# 'Accept-Language': 'zh-cn'
	}
	response = requests.get(url, headers=headers)
	print(response.text)


# with open('detail.html', 'a') as f:
# 	f.writelines(response.text)


if __name__ == '__main__':
	get_list()
	# get_list_other()
	# get_detail()
