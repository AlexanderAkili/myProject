# code UTF-8
#  
# 
import re
import urllib.request

def get_html(url):
	page = urllib.request.urlopen(url)
	html = page.read()
	#print(html)
	return html.decode("utf-8")

def main():
	url = "https://zhuanlan.zhihu.com/p/33951380"
	html = get_html(url)
	r =  r = r"[\u4e00-\u9fa5]+"
	comment_result = re.findall(r,html)
	#print(comment_result)
	print(len(comment_result))

if __name__ == "__main__":
	main()


 
