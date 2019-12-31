import re
from urllib.request import urlopen

def html(url):
	html_code = urlopen(url)
	html_code = html_code.read().decode('gb2312')
	return html_code
	
def re_code(s):
	ret = re.findall('<td class="keyword">.*?">(.*?)</a>.*?<span class="icon-.*?">(\d+)</span>',s,re.S)
	return ret
	
def main():
	url = 'http://top.baidu.com/buzz.php?p=top10'
	url_html = html(url)
	main_code = re_code(url_html)
	num = 1
	for i in main_code:
		print("热点排名第{ranking}：{name}    指数：{index}".format(ranking=num,name=i[0],index=i[1]))
		num +=1
	
main()
