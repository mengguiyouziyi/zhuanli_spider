import requests
from urllib.parse import quote_plus


class CniprRequest(object):
	def __init__(self):
		self.session = requests.session()
		self.id = self.login()

	def login(self):
		headers = {
			# 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
			# 'Accept-Encoding': 'gzip, deflate',
			# 'Accept-Language': 'zh-cn',
			'Connection': 'keep-alive',
			# 'Cookie': 'TailorID=3208de0a93dfd94e069897797de339da92c4',
			'Host': 'm.cnipr.com:8081',
			'Referer': 'http://m.cnipr.com:8081/tailor/http://192.168.201.132:8080/index',
			# 'Upgrade-Insecure-Requests': '1',
			# 'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0_3 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Mobile/15A432'
		}
		login_url = 'http://m.cnipr.com:8081/tailor/http://192.168.201.132:8080/login!goonlogin.action?rd=0.3424056342857026'
		payload = {'username': 'wlglzx', 'password': '!QAZ2wsx'}
		response = self.session.request("POST", login_url, headers=headers, data=payload)
		print(response.text)
		print(response.cookies.items())
		return response.cookies.items()[0][1]

	def get_list_all_other(self):
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

	def get_list_all(self):
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

	def get_list_other(self):
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


	def get_list(self):
		url = 'http://m.cnipr.com:8081/tailor/http://192.168.201.132:8080/search!doOverviewSearch4Index.action?DATA-start=1&limit=30&strWhere=江苏远东电机制造有限公司&yuyijs=&saveFlag=1&keyword2Save=&key2Save=&dbScope=1&type=Valid'
		headers = {
			'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
			'Accept-Encoding': 'gzip, deflate',
			'Accept-Language': 'zh-cn',
			'Connection': 'keep-alive',
			'Cookie': 'TailorID={}'.format(self.id),
			'Host': 'm.cnipr.com:8081',
			'Referer': 'http://m.cnipr.com:8081/tailor/http://192.168.201.132:8080/index',
			'Upgrade-Insecure-Requests': '1',
			'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0_3 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Mobile/15A432',

			# 'User-Agent': 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'
		}
		response = requests.get(url, headers=headers)
		# print(response.text)

		with open('list.html', 'w') as f:
			f.writelines(response.text)

	def get_detail(self):
		comp_name = '江苏远东电机制造有限公司'
		detail_url = 'http://m.cnipr.com:8081/tailor/http://192.168.201.132:8080/search!doDetailSearch.action?Data=strWhere={}&start=4&recordCursor=39&limit=1&option=2&iHitPointType=115&strSortMethod=RELEVANCE&strSources=FMZL%2CSYXX%2CWGZL%2CTWZL%2CHKPATENT%2CUSPATENT%2CJPPATENT%2CEPPATENT%2CWOPATENT%2CGBPATENT%2CDEPATENT%2CFRPATENT%2CCHPATENT%2CKRPATENT%2CRUPATENT%2CAPPATENT%2CATPATENT%2CAUPATENT%2CITPATENT%2CSEPATENT%2CCAPATENT%2CESPATENT%2CGCPATENT%2CASPATENT%2COTHERPATENT%2CTWPATENT&strSynonymous=&yuyijs=&filterChannel=&otherWhere=%5B%7B%22kind%22%3A%22%E4%B8%93%E5%88%A9%E6%9D%83%E7%8A%B6%E6%80%81%22%2C%22showwhere%22%3A%22%E6%9C%89%E6%95%88%22%2C%22where%22%3A%2210%22%7D%5D&title=10.%E4%B8%80%E7%A7%8D%E5%A4%A7%E5%8F%A3%E5%BE%84%E9%AB%98%E6%B8%A9%E8%80%90%E7%A3%A8%E5%B9%B3%E6%9D%BF%E9%97%B8%E9%98%80&keyword=%E4%B8%AD%E7%9F%B3%E5%8C%96'.format(
			comp_name)
		headers = {
			'Host': 'm.cnipr.com:8081',
			'Cookie': 'TailorID=3208de0a93dfd94e069897797de339da92c4',
			'Upgrade-Insecure-Requests': '1',
			'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
			'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0_3 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Mobile/15A432',
			'Referer': 'http://m.cnipr.com:8081/tailor/http://192.168.201.132:8080/search!doOverviewSearch4Index.action?DATA-start=1&limit=10&strWhere=%E4%B8%AD%E7%9F%B3%E5%8C%96&yuyijs=&saveFlag=1&keyword2Save=&key2Save=&dbScope=3&type=Valid',
			'Accept-Language': 'zh-cn'
		}
		response = requests.get(detail_url, headers=headers)
		print(response.text)
		with open('detail.html', 'a') as f:
			f.writelines(response.text)


if __name__ == '__main__':
	cnipr = CniprRequest()
	cnipr.get_list()
# get_list_other()
# get_detail()
