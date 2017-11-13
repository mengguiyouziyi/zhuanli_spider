import requests
import time

try:
	import cookielib
except:
	import http.cookiejar as cookielib


class GetCode():
	def __init__(self):
		self.session = requests.session()
		self.session.cookies = cookielib.LWPCookieJar(filename="cookies.txt")

	def get_a(self):
		pass


	def save_session(self):

		url = "http://114.251.8.193/oauth/authorize"

		querystring = {"client_id": "6050f8adac110002270d833aed28242d", "redirect_uri": "http://www.baidu.com/",
		               "response_type": "code", "scope": "read_cn"}

		headers = {
			'upgrade-insecure-requests': "1",
			'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36",
			'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
			'referer': "http://114.251.8.193/open/oauth_login.jsp",
			'accept-encoding': "gzip, deflate",
			'accept-language': "zh-CN,zh;q=0.8",
			'cookie': "SSOTOKEN=beacon!48F3AB13AFA673C90A54DF7C54F839640C1E18AEF1ABEB196F657D7702CC6C9DBAE44693B06FD91109EA1338ADCE8CE83276257A3168E40B1EA823792CCCE131; JSESSIONID=CFF8F6FDDA05D81A66BE0381BE7B042E",
			'cache-control': "no-cache",
			'postman-token': "8bda0ec1-1218-5103-0205-fe893d55e53d"
		}

		response = self.session.request("GET", url, headers=headers, params=querystring)
		self.session.cookies.save()

	def get_code(self):

		try:
			self.session.cookies.load(ignore_discard=True)
		except:
			print("cookie未能加载")

		url_baidu = "http://114.251.8.193/oauth/authorize"
		payload = ""
		headers_baidu = {
			'origin': "http://114.251.8.193",
			'upgrade-insecure-requests': "1",
			'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36",
			'content-type': "application/x-www-form-urlencoded",
			'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
			'referer': "http://114.251.8.193/oauth/authorize?client_id=6050f8adac110002270d833aed28242d&redirect_uri=http://www.baidu.com/&response_type=code&scope=read_cn",
			'accept-encoding': "gzip, deflate",
			'accept-language': "zh-CN,zh;q=0.8",
			# 'cookie': "SSOTOKEN=beacon!48F3AB13AFA673C90A54DF7C54F839640C1E18AEF1ABEB196F657D7702CC6C9DBAE44693B06FD91109EA1338ADCE8CE83276257A3168E40B1EA823792CCCE131; JSESSIONID=CFF8F6FDDA05D81A66BE0381BE7B042E",
			'cache-control': "no-cache",
			'postman-token': "792e061e-4e8b-6aa9-9021-70afef4fffa6"
		}

		response_baidu = self.session.request("POST", url_baidu, data=payload, headers=headers_baidu)

		print(response_baidu.text)


def main():
	g = GetCode()
	g.save_session()
	time.sleep(0.5)
	g.get_code()


if __name__ == '__main__':
	main()
