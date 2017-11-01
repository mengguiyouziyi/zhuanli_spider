import time
import re
from selenium import webdriver
from scrapy import Selector


# def get_token(path='/data1/spider/java_spider/phantomjs-2.1.1-linux-x86_64/bin/phantomjs1'):
def get_token(path='/root/.pyenv/versions/3.5.4/bin/phantomjs'):
	"""
	path='/root/.pyenv/versions/3.5.4/bin/phantomjs'
	获取access_token
	:return:
	"""
	browser = webdriver.PhantomJS(executable_path=path)
	# browser = webdriver.PhantomJS()
	# browser = webdriver.Chrome(executable_path='/Users/menggui/.pyenv/versions/Anaconda3-4.3.0/bin/chromedriver')
	denglu = 'http://114.251.8.193/login.jsp'
	browser.get(denglu)
	time.sleep(0.5)
	browser.find_element_by_id('username').send_keys('yinguoshu')
	browser.find_element_by_id('password1').send_keys('yinguoshu')
	browser.find_element_by_id('submitButton').click()

	browser.get('http://114.251.8.193/web/api/oauth/authorization.jsp')
	time.sleep(0.5)
	browser.maximize_window()
	# browser.set_window_position(20, 40)
	# browser.set_window_size(3000, 3000)
	browser.execute_script("window.scrollTo(document.body.scrollWidth, document.body.scrollHeight)")
	time.sleep(0.5)
	# with open('x.html', 'a') as f:
	# 	f.write(browser.page_source)
	print(browser.get_window_size())
	browser.find_element_by_class_name('expandResource').click()
	time.sleep(0.5)
	browser.execute_script("window.scrollTo(document.body.scrollWidth, document.body.scrollHeight)")
	time.sleep(0.5)
	browser.find_element_by_name('client_id').send_keys('6050f8adac110002270d833aed28242d')
	browser.find_element_by_name('redirect_uri').send_keys('http://www.baidu.com/')
	browser.find_element_by_name('response_type').send_keys('code')
	browser.find_element_by_name('scope').send_keys('read_cn')
	browser.find_element_by_id('mysubmit').click()
	time.sleep(0.5)

	######
	handles = browser.window_handles
	browser.switch_to.window(handles[1])
	#######

	browser.find_element_by_name('j_username').send_keys('yinguoshu')
	browser.find_element_by_name('j_password').send_keys('yinguoshu')
	browser.find_element_by_class_name('bottong').click()
	time.sleep(0.5)
	browser.find_element_by_name('authorize').click()
	time.sleep(0.5)
	code = re.search(r'code\=(.*?)$', browser.current_url).groups()[0]
	browser.close()
	############
	browser.switch_to.window(handles[0])
	###########

	browser.maximize_window()
	browser.execute_script("window.scrollTo(document.body.scrollWidth, document.body.scrollHeight)")
	time.sleep(0.5)
	browser.find_element_by_id('resource_获取token').find_element_by_class_name('expandResource').click()
	time.sleep(0.5)
	browser.execute_script("window.scrollTo(document.body.scrollWidth, document.body.scrollHeight)")
	time.sleep(0.5)
	browser.find_element_by_id('resource_获取token').find_element_by_name('client_id').send_keys(
		'6050f8adac110002270d833aed28242d')
	browser.find_element_by_id('resource_获取token').find_element_by_name('code').send_keys(code)
	browser.find_element_by_id('resource_获取token').find_element_by_name('client_secret').send_keys(
		'6050f8adac110002270d833a4641d8cf')
	browser.find_element_by_id('resource_获取token').find_element_by_name('grant_type').send_keys('authorization_code')
	browser.find_element_by_id('resource_获取token').find_element_by_name('redirect_uri').send_keys(
		'http://www.baidu.com/')
	browser.find_element_by_id('resource_获取token').find_element_by_class_name('submit').click()
	time.sleep(1)
	select = Selector(text=browser.page_source)
	tags = select.xpath('//pre[@class="json"]/code/span[@class="hljs-string"]/text()').extract()
	# print(tags)
	access_token = tags[0].replace('"', '')
	# refresh_token = tags[2].replace('"', '')
	browser.quit()

	return access_token


if __name__ == '__main__':
	# phan_path = '/Users/menggui/.pyenv/versions/Anaconda3-4.3.0/bin/phantomjs'
	# phan_path = '/home/spider/.pyenv/versions/3.5.3/bin/phantomjs'
	token = get_token()
	print(token)
