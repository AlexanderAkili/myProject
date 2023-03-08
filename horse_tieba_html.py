# code UTF-8
#  
# Author: PinkScorpian
import requests

'''
url = "http://tieba.baidu.com/f?kw=李毅&ie=utf-8&pn={}"
headers = {
	'User-Agent': "Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36"
	           }
r = requests.get(url, headers = headers)
html = r.content.decode("utf-8")
print(html)
'''

# 爬虫都用面向对象的方式写

class TiebaSpider(object):
	def __init__(self):
		self.headers = {
			'User-Agent': "Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36"
		}
		self.url_start = "http://tieba.baidu.com/f?kw=李毅&ie=utf-8&pn={}"  # https://tieba.baidu.com/f?kw=%E6%9D%8E%E6%AF%85&ie=utf-8&pn=0
		self.tieba_name = "liyi"

	def get_url_list(self, url_start):
		url_list = []
		for i in range(10):
			url_list.append(self.url_start.format(i * 50))
		print(url_list)
		return url_list

	def save_html(self, html, page_num):
		# 保存成 “李毅-第1页.html”
		file_path = "{}_第{}页.html".format(self.tieba_name, page_num)
		with open(".\ " + file_path, "w", encoding="utf-8") as f:
			f.write(html)
		print("第%d页保存完成！" % page_num)

	def run(self):  # 实现主要逻辑
		# 构造url 列表
		url_list = self.get_url_list(self.url_start)
		# 遍历，发送请求，获取响应
		for url in url_list:
			response = requests.get(url, headers=self.headers)
			html = response.content.decode()
			# 保存
			page_num = url_list.index(url) + 1
			self.save_html(html, page_num)


if __name__ == "__main__":
	spider = TiebaSpider()
	spider.run()
