from pytesseract import image_to_string
from PIL import Image
from PIL import ImageEnhance
import re


def randomCodeOcr(filename):
	image = Image.open(filename)
	# 使用ImageEnhance可以增强图片的识别率
	# enhancer = ImageEnhance.Contrast(image)
	# enhancer = enhancer.enhance(4)
	image = image.convert('L')
	ltext = image_to_string(image)
	# 去掉非法字符，只保留字母数字
	ltext = re.sub("\W", "", ltext)
	print('[%s]识别到验证码:[%s]!!!' % (filename, ltext))
	image.save(filename)
	return ltext


if __name__ == '__main__':
	# ltext = randomCodeOcr('xiazai.jpg')
	try:
		import Image
	except ImportError:
		from PIL import Image
	import pytesseract

	# pytesseract.pytesseract.tesseract_cmd = '<full_path_to_your_tesseract_executable>'
	# Include the above line, if you don't have tesseract executable in your PATH
	# Example tesseract_cmd: 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract'

	print(pytesseract.image_to_string(Image.open('xiazai.jpg')))
	# print(pytesseract.image_to_string(Image.open('test-european.jpg'), lang='fra'))
