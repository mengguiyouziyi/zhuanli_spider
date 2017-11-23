import requests


def login():
	login_url = 'http://search.cnipr.com/login!goonlogin.action?rd=0.6589196511445976'
	payloads = 'username=mengguiyouziyi&password=3646287'
	payload = {'username': 'mengguiyouziyi', 'password': '3646287'}
	response = requests.request("POST", login_url, data=payload)
	print(response.cookies.items())
	print(dict(response.cookies.items()))


if __name__ == '__main__':
	login()
