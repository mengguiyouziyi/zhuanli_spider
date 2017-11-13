import requests
from urllib.parse import quote_plus


class Soopat(object):
	def __init__(self):
		self.session = requests.session()

	def get_detail(self):
		detail_url = 'http://www.soopat.com/Patent/201611125149'
		headers = {
			'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
			'accept-encoding': "gzip, deflate",
			'accept-language': "zh-CN,zh;q=0.8",
			'cache-control': "no-cache",
			'connection': "keep-alive",
			'cookie': "ASP.NET_SessionId=oemmzdfxtkpzskopirey5xg2; patentids=; __utmc=135424883; __utmz=135424883.1510553816.2.2.utmccn=(referral)|utmcsr=soopat.com|utmcct=/Home/Result|utmcmd=referral; __utmb=135424883; __utma=135424883.1261609669.1510543897.1510543897.1510553816.2",
			'host': "www.soopat.com",
			'referer': "http://www.soopat.com/Home/Result?SearchWord=%E5%9B%BD%E5%AE%B6%E7%BA%B3%E7%B1%B3%E7%A7%91%E5%AD%A6%E4%B8%AD%E5%BF%83&FMZL=Y&SYXX=Y&WGZL=Y&FMSQ=Y",
			'upgrade-insecure-requests': "1",
			'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36",
			'postman-token': "6f1a91a7-7faa-c63b-b711-e8b72e52f8c7"
		}
		response = self.session.get(detail_url, headers=headers)
		print(response.text)

	def get_list(self):
		url = 'http://www.soopat.com/Home/Result?SearchWord=%E7%BA%B3%E7%B1%B3%E6%96%B0%E8%83%BD%E6%BA%90%28%E5%94%90%E5%B1%B1%29%E6%9C%89%E9%99%90%E8%B4%A3%E4%BB%BB%E5%85%AC%E5%8F%B8&FMZL=Y&SYXX=Y&WGZL=Y&FMSQ=Y'
		url = 'http://www.soopat.com/Home/Result?SearchWord=%E5%9B%BD%E5%AE%B6%E7%BA%B3%E7%B1%B3%E7%A7%91%E5%AD%A6%E4%B8%AD%E5%BF%83&FMZL=Y&SYXX=Y&WGZL=Y&FMSQ=Y&PatentIndex=12'
		headers = {
			'Accept-Encoding:gzip, deflate',
			'Accept-Language:zh-CN,zh;q=0.8',
			'Connection:keep-alive',
			'Cookie:ASP.NET_SessionId=oemmzdfxtkpzskopirey5xg2; __utma=135424883.1261609669.1510543897.1510543897.1510543897.1; __utmc=135424883; __utmz=135424883.1510543897.1.1.utmccn=(direct)|utmcsr=(direct)|utmcmd=(none); patentids=',
			'Host:www.soopat.com',
			'Referer:http://www.soopat.com/',
			'Upgrade-Insecure-Requests:1',
			'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
		}
		response = requests.get(url, headers=headers)

	def get_captcha(self):
		words = '国家纳米科学中心'
		qu_words = quote_plus(words)
		headers = {
			'accept': "image/webp,image/apng,image/*,*/*;q=0.8",
			'accept-encoding': "gzip, deflate",
			'accept-language': "zh-CN,zh;q=0.8",
			'connection': "keep-alive",
			'cookie': "ASP.NET_SessionId=oemmzdfxtkpzskopirey5xg2; __utma=135424883.1261609669.1510543897.1510543897.1510543897.1; __utmc=135424883; __utmz=135424883.1510543897.1.1.utmccn=(direct)|utmcsr=(direct)|utmcmd=(none); patentids=",
			'host': "www.soopat.com",
			'referer': "http://www.soopat.com/Home/Result?SearchWord={}&FMZL=Y&SYXX=Y&WGZL=Y&FMSQ=Y".format(qu_words),
			'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36",
			'cache-control': "no-cache",
			'postman-token': "c1ba811f-fed0-8f9d-78ef-cf5287f1a1eb"
		}
		captcha_url = 'http://www.soopat.com/Account/ValidateImage'
		t = self.session.get(captcha_url, headers=headers)
		with open("captcha.jpg", "wb") as f:
			f.write(t.content)
		from PIL import Image
		try:
			im = Image.open("captcha.jpg")
			im.show()
			im.close()
		except:
			pass
		captcha = input("输入验证码\n>")
		url = "http://www.soopat.com/Home/RandomCdPost"
		querystring = {
			"Url": "http://www.soopat.com/Home/Result?SearchWord={}&FMZL=Y&SYXX=Y&WGZL=Y&FMSQ=Y".format(qu_words),
			"Cd": captcha}
		c_headers = {
			'x-devtools-emulate-network-conditions-client-id': "a35c92ef-5d0a-497d-a779-1403ec6f9eab",
			'upgrade-insecure-requests': "1",
			'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36",
			'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
			'referer': "http://www.soopat.com/Home/Result?SearchWord={}&FMZL=Y&SYXX=Y&WGZL=Y&FMSQ=Y".format(qu_words),
			'accept-encoding': "gzip, deflate",
			'accept-language': "zh-CN,zh;q=0.8",
			'cookie': "ASP.NET_SessionId=oemmzdfxtkpzskopirey5xg2; __utma=135424883.1261609669.1510543897.1510543897.1510543897.1; __utmc=135424883; __utmz=135424883.1510543897.1.1.utmccn=(direct)|utmcsr=(direct)|utmcmd=(none); patentids=",
			'cache-control': "no-cache",
			'postman-token': "902408a7-e378-4c21-3764-d527cf6287c1"
		}
		response = self.session.request("GET", url, headers=c_headers, params=querystring)
		print(response.text)

	def get_next(self):
		next_url = 'http://www.soopat.com/Home/Result?SearchWord=%E7%BA%B3%E7%B1%B3%E5%8F%91%E7%94%B5%E6%9C%BA&FMZL=Y&SYXX=Y&WGZL=Y&FMSQ=Y&PatentIndex=80'


if __name__ == '__main__':
	soopat = Soopat()
	# soopat.get_captcha()
	# soopat.get_captcha()
	soopat.get_detail()
