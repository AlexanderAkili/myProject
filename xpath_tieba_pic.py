# code UTF-8
#  
# 
import requests
from lxml import etree
import urllib.request


def get_img_url_list(page_url):
	Response = requests.get(page_url)  # 获取响应
	selector = etree.HTML(Response.text)  # 解析网页
	img_url_list = selector.xpath('//div[@class="d_post_content j_d_post_content "]/img/@src')
	return img_url_list


def get_html(url):
	page = urllib.request.urlopen(url)
	html = page.read()
	return html.decode("utf-8")


def page_url_machine(url_origin):
	url_list = []
	for i in range (1,10):
		url_new = url_origin + "?pn=" + str(i)
		url_list.append(url_new)
	return url_list


def get_img(img_list):
	k = 0
	for img_url in img_list:
		str_position = "D:\A_test_pic_tieba"
		urllib.request.urlretrieve(img_url,str_position + '\%d.jpg'%k)
		k += 1
		print("第%d张图片下载完毕"%k)


def main():
	# 提交url
	url_origin = "https://tieba.baidu.com/p/2256306796"
	page_url = page_url_machine(url_origin)
	img_list = []

	for url in page_url:
		img_url = get_img_url_list(url)
		img_list.extend(img_url)

	pic = get_img(img_list)



if __name__ == "__main__":
	main()
 