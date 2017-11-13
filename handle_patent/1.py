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
		try:
			self.session.cookies.load(ignore_discard=True)
		except:
			print("cookie未能加载")

	def get_1(self):
		url = "http://114.251.8.193/j_spring_security_check"

		payload = {'j_password': 'yinguoshu', 'j_username': 'yinguoshu'}
		headers = {
			'origin': "http://114.251.8.193",
			'upgrade-insecure-requests': "1",
			'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36",
			'content-type': "application/x-www-form-urlencoded",
			'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
			'referer': "http://114.251.8.193/open/oauth_login.jsp",
			'accept-encoding': "gzip, deflate",
			'accept-language': "zh-CN,zh;q=0.8",
			# 'cookie': "SSOTOKEN=beacon!48F3AB13AFA673C90A54DF7C54F839640C1E18AEF1ABEB196F657D7702CC6C9DBAE44693B06FD91109EA1338ADCE8CE83276257A3168E40B1EA823792CCCE131; JSESSIONID=95AA341A7C1AF9689DC5ED25F9BD2385",
			'cache-control': "no-cache",
			'postman-token': "dac2a7bd-c400-4001-6fc7-d76f644fd3b4"
		}

		response = self.session.request("POST", url, data=payload, headers=headers)
		print(response.cookies)
		print(self.session.cookies)
		self.session.cookies.save()

		# print(response.text)

	def get_2(self):

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
			# 'cookie': "SSOTOKEN=beacon!48F3AB13AFA673C90A54DF7C54F839640C1E18AEF1ABEB196F657D7702CC6C9DBAE44693B06FD91109EA1338ADCE8CE83276257A3168E40B1EA823792CCCE131; JSESSIONID=51E304AE3552CE3288F60C3161E6A542",
			'cache-control': "no-cache",
			'postman-token': "deb707b3-a003-7a2a-dabb-8ba950ae3edd"
		}

		response = requests.request("GET", url, headers=headers, params=querystring)

		print(response.text)

	def get_3(self):
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
			'cookie': "SSOTOKEN=beacon!48F3AB13AFA673C90A54DF7C54F839640C1E18AEF1ABEB196F657D7702CC6C9DBAE44693B06FD91109EA1338ADCE8CE83276257A3168E40B1EA823792CCCE131; JSESSIONID=51E304AE3552CE3288F60C3161E6A542; SSOTOKEN=beacon!48F3AB13AFA673C90A54DF7C54F839640C1E18AEF1ABEB196F657D7702CC6C9DBAE44693B06FD91109EA1338ADCE8CE83276257A3168E40B1EA823792CCCE131; JSESSIONID=94FC1C3FF8DDFC7B398F77AE787DB848",
			'cache-control': "no-cache",
			'postman-token': "50f6b9d6-2f14-2b4c-8b73-088bf9ffa89b"
		}

		response = self.session.request("GET", url, headers=headers, params=querystring)

		# print(response.text)
		self.session.cookies.save()

	def get_4(self):
		# try:
		# 	self.session.cookies.load(ignore_discard=True)
		# except:
		# 	print("cookie未能加载")
		url = "http://114.251.8.193/oauth/authorize"

		payload = {'j_username': 'yinguoshu', 'j_password': 'yinguoshu'}
		headers = {
			'origin': "http://114.251.8.193",
			'upgrade-insecure-requests': "1",
			'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36",
			'content-type': "application/x-www-form-urlencoded",
			'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
			'referer': "http://114.251.8.193/oauth/authorize?client_id=6050f8adac110002270d833aed28242d&redirect_uri=http://www.baidu.com/&response_type=code&scope=read_cn",
			'accept-encoding': "gzip, deflate",
			'accept-language': "zh-CN,zh;q=0.8",
			# 'cookie': "SSOTOKEN=beacon!48F3AB13AFA673C90A54DF7C54F839640C1E18AEF1ABEB196F657D7702CC6C9DBAE44693B06FD91109EA1338ADCE8CE83276257A3168E40B1EA823792CCCE131; JSESSIONID=51E304AE3552CE3288F60C3161E6A542; SSOTOKEN=beacon!48F3AB13AFA673C90A54DF7C54F839640C1E18AEF1ABEB196F657D7702CC6C9DBAE44693B06FD91109EA1338ADCE8CE83276257A3168E40B1EA823792CCCE131; JSESSIONID=94FC1C3FF8DDFC7B398F77AE787DB848",
			'cache-control': "no-cache",
			'postman-token': "426ee756-2f76-4882-cb5c-76382b62069c"
		}

		response = self.session.request("POST", url, data=payload, headers=headers)

		print(response.text)

	def get_5(self):
		url = "http://www.baidu.com/"

		querystring = {"code": "6iG0A8"}

		headers = {
			'upgrade-insecure-requests': "1",
			'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36",
			'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
			'referer': "http://114.251.8.193/oauth/authorize?client_id=6050f8adac110002270d833aed28242d&redirect_uri=http://www.baidu.com/&response_type=code&scope=read_cn",
			'accept-encoding': "gzip, deflate",
			'accept-language': "zh-CN,zh;q=0.8",
			'cookie': "BAIDUID=6C0404301BD166DAB45DC92B2B2A210D:FG=1; BIDUPSID=6C0404301BD166DAB45DC92B2B2A210D; PSTM=1496909224; __cfduid=d1e6ea12239199573b7942e741185bb251497505093; BDUSS=NKZTNrcWFTcjZhRjI3WkI0YVh3YWVSV0V5anZwM1RVUkNjRXhiV3BGSWpRYUZaSVFBQUFBJCQAAAAAAAAAAAEAAADQbm4Gc3VuMDEyMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACO0eVkjtHlZTz; MCITY=-%3A; ispeed_lsm=2; BAIDUID=6C0404301BD166DAB45DC92B2B2A210D:FG=1; BIDUPSID=6C0404301BD166DAB45DC92B2B2A210D; PSTM=1496909224; BDUSS=NKZTNrcWFTcjZhRjI3WkI0YVh3YWVSV0V5anZwM1RVUkNjRXhiV3BGSWpRYUZaSVFBQUFBJCQAAAAAAAAAAAEAAADQbm4Gc3VuMDEyMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACO0eVkjtHlZTz; MCITY=-%3A; ispeed_lsm=2; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BD_HOME=1; BD_CK_SAM=1; PSINO=1; H_PS_PSSID=24457_1462_13548_21094_17001_24328_20928; BD_UPN=123253; sug=3; sugstore=0; ORIGIN=0; bdime=0; BDSVRTM=0",
			'cache-control': "no-cache",
			'postman-token': "f7d33160-7f7a-5df4-4316-3c9029f14916"
		}

		response = self.session.request("GET", url, headers=headers, params=querystring)

		print(response.text)

	def get_6(self):
		url = "https://www.baidu.com/"

		querystring = {"code": "6iG0A8"}

		headers = {
			'upgrade-insecure-requests': "1",
			'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36",
			'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
			'referer': "http://114.251.8.193/oauth/authorize?client_id=6050f8adac110002270d833aed28242d&redirect_uri=http://www.baidu.com/&response_type=code&scope=read_cn",
			'accept-encoding': "gzip, deflate, br",
			'accept-language': "zh-CN,zh;q=0.8",
			'cookie': "BAIDUID=6C0404301BD166DAB45DC92B2B2A210D:FG=1; BIDUPSID=6C0404301BD166DAB45DC92B2B2A210D; PSTM=1496909224; __cfduid=d1e6ea12239199573b7942e741185bb251497505093; BDUSS=NKZTNrcWFTcjZhRjI3WkI0YVh3YWVSV0V5anZwM1RVUkNjRXhiV3BGSWpRYUZaSVFBQUFBJCQAAAAAAAAAAAEAAADQbm4Gc3VuMDEyMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACO0eVkjtHlZTz; MCITY=-%3A; ispeed_lsm=2; BAIDUID=6C0404301BD166DAB45DC92B2B2A210D:FG=1; BIDUPSID=6C0404301BD166DAB45DC92B2B2A210D; PSTM=1496909224; BDUSS=NKZTNrcWFTcjZhRjI3WkI0YVh3YWVSV0V5anZwM1RVUkNjRXhiV3BGSWpRYUZaSVFBQUFBJCQAAAAAAAAAAAEAAADQbm4Gc3VuMDEyMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACO0eVkjtHlZTz; MCITY=-%3A; ispeed_lsm=2; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BD_HOME=1; BD_CK_SAM=1; PSINO=1; H_PS_PSSID=24457_1462_13548_21094_17001_24328_20928; BD_UPN=123253; sug=3; sugstore=0; ORIGIN=0; bdime=0; BDSVRTM=0; BD_LAST_QID=15010089557607663973",
			'cache-control': "no-cache",
			'postman-token': "605bd334-f5df-2eb1-3b5a-bc7dc805d69a"
		}

		response = self.session.request("GET", url, headers=headers, params=querystring)

		print(response.text)

	def get_7(self):
		import requests

		url = "http://114.251.8.193/oauth/authorize"

		querystring = {"client_id": "6050f8adac110002270d833aed28242d", "redirect_uri": "http://www.baidu.com/",
		               "response_type": "code", "scope": "read_cn"}

		headers = {
			'cache-control': "no-cache",
			'postman-token': "ce2be491-618c-75b4-3854-0b11d74a615e"
		}

		response = requests.request("GET", url, headers=headers, params=querystring)

		print(response.text)


def main():
	g = GetCode()
	g.get_1()
	# g.get_2()


# g.get_5()
# g.get_6()


if __name__ == '__main__':
	main()
