# code UTF-8
#  
# Author: PinkScorpian
import re
import urllib.request

def get_html(url):
	page = urllib.request.urlopen(url)
	html = page.read()
	#print("")
	return html

def get_img(html):
	reg = r'src="(.*?\.jpg)"\s*width'
	img_re = re.compile(reg)  # 对正则匹配进行编译
	html = html.decode("utf-8")
	#print(html)
	#py2和py3 有区别，py3一定要有这句"decode"
	img_list = re.findall(img_re,html)
	k = 0
	for img_url in img_list:
		urllib.request.urlretrieve(img_url,'%d.jpg'%k)
		k += 1
		print("第%d张图片下载完毕"%k)

def main():
	url_origin = "https://tieba.baidu.com/p/2256306796"
	html = get_html(url_origin)
	pictures =  get_img(html)

if __name__ == "__main__":
	main()