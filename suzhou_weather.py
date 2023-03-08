#utf-8
import time
import urllib.request
import random
from bs4 import BeautifulSoup
import csv

def get_page_content(url):
	data = None
	header = {
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
	}
	timeout = random.choice(range(80,180))  # 设定的一个超时时间，取随机数可以防止被网站认定为爬虫
	
	while True:
		try:
			ret = urllib.request.Request(url,data,headers = header)
			# 调试用 print("----Debug! YOYO! YO!----")
			res_ponse = urllib.request.urlopen(ret,timeout = timeout)
			html1 = res_ponse.read().decode("utf-8",errors = 'ignore')
			res_ponse.close()
			return html1
		except Exception as a:
			print("----There is a tiny frog----")
			break

def get_data(html_txt):
	final = []
	b_soup = BeautifulSoup(html_txt,"html.parser")  # 创建BeautifulSoup对象
	body = b_soup.body  # 获取body部分
	data = body.find('div',{'id':'7d'})  # 找到id 为7d的div
	ul = data.find("ul")  # 获取ul部分
	li = ul.find_all("li")  # 获取所有li 
	
	
	# 对每一个li中对象进行遍历
	for day in li:
		temp = []
		date = day.find("h1").string  # 找到日期
		temp.append(date)  # 添加到temp中
		weather = day.find_all('p')  # 找到li中所有p标签
		temp.append(weather[0].string,)  # 第一个p标签中的天气情况加到temp中
		if weather[1].find('span') is None:
			temperature_highest = None # 可能没有当天的最高气温
		else:
			temperature_highest = weather[1].find('span').string  # 找到最高温
			temperature_lowest = weather[1].find('i').string  #找到最低温
			temp.append(temperature_highest)
			temp.append(temperature_lowest)
			final.append(temp)
			
	return final

	
def writ_page_content(data,name):
	file_name = name
	with open (file_name,'a',errors = "ignore",newline ='') as f:
		f_csv = csv.writer(f)
		f_csv.writerows(data)


def main():	
	# 模拟浏览器访问网页，获取html源代码
	url = "http://www.weather.com.cn/weather/101190401.shtml"
	page_content_html = get_page_content(url)
	# 通过正则匹配（beautifulsoup 可以不写正则），获取指定标签中内容
	result = get_data(page_content_html)
	# 将获取的内容写到文件中
	writ_page_content(result,"weather.csv")
if __name__ == "__main__":
	main()