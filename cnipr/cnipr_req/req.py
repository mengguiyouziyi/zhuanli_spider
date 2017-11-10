import requests

try:
	import cookielib
except:
	import http.cookiejar as cookielib



class Spide(object):
	def __init__(self):
		self.session = requests.session()
		self.session.cookies = cookielib.LWPCookieJar(filename="cookies.txt")
		self.headers = {
			'accept': "application/x-ms-application, image/jpeg, application/xaml+xml, image/gif, image/pjpeg, application/x-ms-xbap, */*",
			'referer': "http://search.cnipr.com/pages!advSearch.action",
			'accept-language': "zh-CN",
			'user-agent': "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; Shuame; Core/1.53.2050.400 QQBrowser/9.5.10218.400)",
			'content-type': "application/x-www-form-urlencoded",
			'accept-encoding': "gzip, deflate",
			'host': "search.cnipr.com",
			'content-length': "633",
			'connection': "Keep-Alive",
			'pragma': "no-cache",
			# 'cookie': "JSESSIONID=DD010C40BA7D53DD6B2FC549A5A128A8; cniprAutoLogin=mengguiyouziyi%7C3646287; _gscu_719616686=10214968ywmgyx45; _gscs_719616686=10214968mpdsb345|pv:4; _gscbrs_719616686=1; _trs_uv=j9s6zzl4_1186_6w0j; _trs_ua_s_1=j9s6zzl4_1186_btmz",
			'cache-control': "no-cache",
			'postman-token': "bcd5016f-97f4-6ea4-65ee-a42288c96ec5"
		}

	def denglu(self):
		url = "http://search.cnipr.com/login.action"
		querystring = {"rd": "0.4289715556717164"}
		payload = {'username': 'mengguiyouziyi', 'password': '3646287'}
		response = self.session.request("POST", url, headers=self.headers, params=querystring, data=payload)
		self.session.cookies.save()
		print(self.session.cookies)
		print(response.text)

	def check_login(self):
		url = "http://search.cnipr.com/login%21checkLogin.action"
		querystring = {"randomNum": "0.9040123157999989"}
		headers = {
			'accept': "*/*",
			'origin': "http://search.cnipr.com",
			'x-devtools-emulate-network-conditions-client-id': "3453ed57-0010-4d33-b890-5baa0b0e0088",
			'x-requested-with': "XMLHttpRequest",
			'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36",
			'content-type': "text/plain;charset=UTF-8",
			'referer': "http://search.cnipr.com/pages!advSearch.action",
			'accept-encoding': "gzip, deflate",
			'accept-language': "zh-CN,zh;q=0.8",
			# 'cookie': "yunsuo_session_verify=450304a51a18108086355b1d67d81ee2; _ubm_ref.jEVZOqlU=%5B%22%22%2C%22%22%2C1510214249%2C%22http%3A%2F%2Fsearch.cnipr.com%2Fpages!advSearch.action%22%5D; _ubm_id.jEVZOqlU=5dbeb122d94854a8; checkedwords=0%2C1%2C2%2C3%2C4; advchannel=FMZL%2CSYXX%2CWGZL%2CFMSQ%2CTWZL%2CHKPATENT%2CUSPATENT%2CEPPATENT%2CJPPATENT%2CWOPATENT%2CGBPATENT%2CCHPATENT%2CDEPATENT%2CKRPATENT%2CFRPATENT%2CRUPATENT%2CASPATENT%2CATPATENT%2CGCPATENT%2CITPATENT%2CAUPATENT%2CAPPATENT%2CCAPATENT%2CSEPATENT%2CESPATENT%2COTHERPATENT; searchcol=%u7533%u8BF7%uFF08%u4E13%u5229%u6743%uFF09%u4EBA; _gscu_719616686=0950182114s1dh12; _gscs_719616686=t10195927cruhrz13|pv:12; _gscbrs_719616686=1; yunsuo_session_verify=450304a51a18108086355b1d67d81ee2; _trs_uv=j9geerzw_1186_brj5; _ubm_ref.jEVZOqlU=%5B%22%22%2C%22%22%2C1510214249%2C%22http%3A%2F%2Fsearch.cnipr.com%2Fpages!advSearch.action%22%5D; _ubm_id.jEVZOqlU=5dbeb122d94854a8; _ubm_ses.jEVZOqlU=*; JSESSIONID=F832061F766977F0C1831090469574E9; _gscu_719616686=0950182114s1dh12; _gscs_719616686=t10195927cruhrz13|pv:14; _gscbrs_719616686=1; _trs_uv=j9geerzw_1186_brj5; _trs_ua_s_1=j9rvnveo_1186_b9tl",
			'cache-control': "no-cache",
			'postman-token': "3372d6a6-8785-8f16-1298-366cc1ad0775"
		}
		response = self.session.request("POST", url, headers=headers, params=querystring)
		print(response.text)

	def get_list(self):
		try:
			self.session.cookies.load(ignore_discard=True)
		except:
			print("cookie未能加载")
		url = "http://search.cnipr.com/search!doOverviewSearch.action"
		# f = 'strWhere=%E7%94%B3%E8%AF%B7%EF%BC%88%E4%B8%93%E5%88%A9%E6%9D%83%EF%BC%89%E4%BA%BA%3D%28%E4%B8%AD%E5%9B%BD%E7%9F%B3%E6%B2%B9%E5%8C%96%E5%B7%A5%E8%82%A1%E4%BB%BD%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8%29&yuyijs=&start=1&saveFlag=1&limit=10&strSynonymous=&crossLanguage=&islogicsearch=false&saveExp=&showhint=&mpage=null&channelId=FMZL&channelId=SYXX&channelId=WGZL&channelId=FMSQ&channelId=TWZL&channelId=HKPATENT&channelId=USPATENT&channelId=EPPATENT&channelId=JPPATENT&channelId=WOPATENT&channelId=GBPATENT&channelId=CHPATENT&channelId=DEPATENT&channelId=KRPATENT&channelId=FRPATENT&channelId=RUPATENT&channelId=ASPATENT&channelId=ATPATENT&channelId=GCPATENT&channelId=ITPATENT&channelId=AUPATENT&channelId=APPATENT&channelId=CAPATENT&channelId=SEPATENT&channelId=ESPATENT&channelId=OTHERPATENT&trsq=1&dan=1&txt_A=&txt_B=&txt_C=&txt_D=&txt_E=&txt_F=&txt_Q=&txt_R=&txt_I=%E4%B8%AD%E5%9B%BD%E7%9F%B3%E6%B2%B9%E5%8C%96%E5%B7%A5%E8%82%A1%E4%BB%BD%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8&txt_J=&txt_G=&txt_H=&txt_L=&txt_O=&text=&txt_K=&txt_M=&txt_N=&txt_U=&txt_T=&txt_V=&txt_X=&mpage=advsch'
		# f = 'wgViewmodle=&strWhere=%28%28%28%E7%94%B3%E8%AF%B7%EF%BC%88%E4%B8%93%E5%88%A9%E6%9D%83%EF%BC%89%E4%BA%BA%3D%28%E4%B8%AD%E5%9B%BD%E7%9F%B3%E6%B2%B9%E5%8C%96%E5%B7%A5%E8%82%A1%E4%BB%BD%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8%29%29++and+%E7%94%B3%E8%AF%B7%EF%BC%88%E4%B8%93%E5%88%A9%E6%9D%83%EF%BC%89%E4%BA%BA%3D%28%E4%B8%AD%E5%9B%BD%E7%9F%B3%E6%B2%B9%E5%8C%96%E5%B7%A5%E8%82%A1%E4%BB%BD%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8%29%29++and+%E7%94%B3%E8%AF%B7%EF%BC%88%E4%B8%93%E5%88%A9%E6%9D%83%EF%BC%89%E4%BA%BA%3D%28%E4%B8%AD%E5%9B%BD%E7%9F%B3%E6%B2%B9%E5%8C%96%E5%B7%A5%E8%82%A1%E4%BB%BD%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8%29%29++and+%E7%94%B3%E8%AF%B7%EF%BC%88%E4%B8%93%E5%88%A9%E6%9D%83%EF%BC%89%E4%BA%BA%3D%28%E4%B8%AD%E5%9B%BD%E7%9F%B3%E6%B2%B9%E5%8C%96%E5%B7%A5%E8%82%A1%E4%BB%BD%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8%29&start=1&limit=10&option=2&iHitPointType=115&strSortMethod=RELEVANCE&strSources=FMZL%2CSYXX%2CWGZL%2CFMSQ%2CTWZL%2CHKPATENT%2CUSPATENT%2CEPPATENT%2CJPPATENT%2CWOPATENT%2CGBPATENT%2CCHPATENT%2CDEPATENT%2CKRPATENT%2CFRPATENT%2CRUPATENT%2CASPATENT%2CATPATENT%2CGCPATENT%2CITPATENT%2CAUPATENT%2CAPPATENT%2CCAPATENT%2CSEPATENT%2CESPATENT%2COTHERPATENT&strSynonymous=&yuyijs=&filterChannel=&keyword2Save=%E4%B8%AD%E5%9B%BD%E7%9F%B3%E6%B2%B9%E5%8C%96%E5%B7%A5%E8%82%A1%E4%BB%BD%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8&key2Save=%E7%94%B3%E8%AF%B7%EF%BC%88%E4%B8%93%E5%88%A9%E6%9D%83%EF%BC%89%E4%BA%BA&forward=&otherWhere=&username=&password='
		f = 'strWhere=%E7%94%B3%E8%AF%B7%EF%BC%88%E4%B8%93%E5%88%A9%E6%9D%83%EF%BC%89%E4%BA%BA%3D%28%E4%B8%AD%E5%9B%BD%E7%9F%B3%E6%B2%B9%E5%8C%96%E5%B7%A5%E8%82%A1%E4%BB%BD%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8%29&yuyijs=&start=1&saveFlag=1&limit=10&strSynonymous=&crossLanguage=&islogicsearch=false&saveExp=&showhint=&mpage=null&channelId=FMZL&channelId=SYXX&trsq=1&dan=1&txt_A=&txt_B=&txt_C=&txt_D=&txt_E=&txt_F=&txt_Q=&txt_R=&txt_I=%E4%B8%AD%E5%9B%BD%E7%9F%B3%E6%B2%B9%E5%8C%96%E5%B7%A5%E8%82%A1%E4%BB%BD%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8&txt_J=&txt_G=&txt_H=&txt_L=&txt_O=&text=&txt_K=&txt_M=&txt_N=&txt_U=&txt_T=&txt_V=&txt_X=&=&mpage=advsch'
		payload = dict([m.split('=') for m in f.split('&')])
		response = self.session.request("POST", url, data=payload, headers=self.headers)
		print(response.text)


if __name__ == '__main__':
	s = Spide()
	s.denglu()
	# s.check_login()
	s.get_list()
