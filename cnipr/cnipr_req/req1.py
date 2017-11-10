import requests

url = 'http://search.cnipr.com/search!doOverviewSearch.action'
headers = {
	'Accept-Encoding': 'gzip, deflate',
	'Accept-Language': 'zh-CN,zh;q=0.8',
	'Cache-Control': 'max-age=0',
	'Connection': 'keep-alive',
	'Content-Length': '1078',
	'Content-Type': 'application/x-www-form-urlencoded',
	'Cookie': 'checkedwords=0%2C1%2C2%2C3%2C4; advchannel=FMZL%2CSYXX%2CWGZL%2CFMSQ%2CTWZL%2CHKPATENT%2CUSPATENT%2CEPPATENT%2CJPPATENT%2CWOPATENT%2CGBPATENT%2CCHPATENT%2CDEPATENT%2CKRPATENT%2CFRPATENT%2CRUPATENT%2CASPATENT%2CATPATENT%2CGCPATENT%2CITPATENT%2CAUPATENT%2CAPPATENT%2CCAPATENT%2CSEPATENT%2CESPATENT%2COTHERPATENT; searchcol=%u7533%u8BF7%uFF08%u4E13%u5229%u6743%uFF09%u4EBA; _gscu_719616686=0950182114s1dh12; _gscbrs_719616686=1; yunsuo_session_verify=450304a51a18108086355b1d67d81ee2; _trs_uv=j9geerzw_1186_brj5; _ubm_ref.jEVZOqlU=%5B%22%22%2C%22%22%2C1510214249%2C%22http%3A%2F%2Fsearch.cnipr.com%2Fpages!advSearch.action%22%5D; _ubm_id.jEVZOqlU=5dbeb122d94854a8; cniprAutoLogin=mengguiyouziyi%7C3646287; _gscu_719616686=10214968ywmgyx45; _gscs_719616686=10214968mpdsb345|pv:4; _gscbrs_719616686=1; _trs_uv=j9s6zzl4_1186_6w0j; _trs_ua_s_1=j9s6zzl4_1186_btmz; JSESSIONID=8AEBB8E67BB2F530142B899E6CBD21D7',
	'Host': 'search.cnipr.com',
	'Origin': 'http://search.cnipr.com',
	'Referer': 'http://search.cnipr.com/pages!advSearch.action',
	'Upgrade-Insecure-Requests': '1',
	'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
}
f = 'strWhere=%E7%94%B3%E8%AF%B7%EF%BC%88%E4%B8%93%E5%88%A9%E6%9D%83%EF%BC%89%E4%BA%BA%3D%28%E4%B8%AD%E5%9B%BD%E7%9F%B3%E6%B2%B9%E5%8C%96%E5%B7%A5%E8%82%A1%E4%BB%BD%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8%29&yuyijs=&start=1&saveFlag=1&limit=10&strSynonymous=&crossLanguage=&islogicsearch=false&saveExp=&showhint=&mpage=null&channelId=FMZL&channelId=SYXX&channelId=WGZL&channelId=FMSQ&channelId=TWZL&channelId=HKPATENT&channelId=USPATENT&channelId=EPPATENT&channelId=JPPATENT&channelId=WOPATENT&channelId=GBPATENT&channelId=CHPATENT&channelId=DEPATENT&channelId=KRPATENT&channelId=FRPATENT&channelId=RUPATENT&channelId=ASPATENT&channelId=ATPATENT&channelId=GCPATENT&channelId=ITPATENT&channelId=AUPATENT&channelId=APPATENT&channelId=CAPATENT&channelId=SEPATENT&channelId=ESPATENT&channelId=OTHERPATENT&trsq=1&dan=1&txt_A=&txt_B=&txt_C=&txt_D=&txt_E=&txt_F=&txt_Q=&txt_R=&txt_I=%E4%B8%AD%E5%9B%BD%E7%9F%B3%E6%B2%B9%E5%8C%96%E5%B7%A5%E8%82%A1%E4%BB%BD%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8&txt_J=&txt_G=&txt_H=&txt_L=&txt_O=&text=&txt_K=&txt_M=&txt_N=&txt_U=&txt_T=&txt_V=&txt_X=&mpage=advsch'
payload = dict([m.split('=') for m in f.split('&')])
response = requests.post(url, headers=headers, data=payload)
print(response.text)
