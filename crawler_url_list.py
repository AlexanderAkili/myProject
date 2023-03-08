import urllib.request
import urllib.parse
import time,random
from bs4 import BeautifulSoup


class Crawler(object):
	def __init__(self):
		pass
		
	def crawl(self,url,pages,depth = 2):  # 爬取数据
		header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}	
		timeout = random.choice(range(80,180))  # 设定的一个超时时间，取随机数可以防止被网站认定为爬虫
		
		for page in pages:
			#try:
			request = urllib.request.urlopen(url)  # 获取网站响应内容
			page_content = request.read()  # 读取网站响应文件,用变量page_content存储
			with open ("page_content_downloading.txt","wb") as f:
				f.write(page_content)  # print("-----test----")
			return page_content
			#except Exception as a:
			#	print("----There is a tiny frog----")
			#	break
		'''

		for i in range(depth):
			
				c = urllib.request.Request(url,data,headers = header)
				beau_soup = BeautifulSoup(c.read())
				self.add_2_index(page,beau_soup)
				
			links = soup('a')
			for link in links:
				if ('href' in dic(lin.attrs)):
		'''
					
		
	def get_entry_id(self):  # 辅助函数，用于获取条目id，如果条目不存在就将其加入数据库中
		pass
		
	def add_2_index(self):
		print("indexing %s" % url)

	def isindexed(self,url):
		return False
	
	def add_link_ref(self,url_from,url_to,link_text):
		pass
	
	def get_txt_only(self,page_content):
		pass
		
	def save(self,data,name):
		pass
		

def main():
	# create a tiny spider
	pink_spider = Crawler()
	url = input("请输入要爬取的url：")
	
	
	# let it crawl websites
	pages = ["http://www.tuniu.com"]
	page_content =  pink_spider.crawl(url,pages)
	
	
	
	# get data 
	data = pink_spider.get_txt_only(page_content)
	
	
	# save
	pink_spider.save(data,"demo_dowload")
	
if __name__ == "__main__":
	main()