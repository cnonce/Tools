import json
from urllib.request import urlopen
import ssl
import re 
ssl._create_default_https_context = ssl._create_unverified_context


for num in range(1,8):
	url = urlopen('https://dncapi.feixiaohao.com/api/exchange/web-exchange?token=&page=%s&pagesize=50&isinnovation=0&type=all&webp=0'%num,ssl_version=ssl.PROTOCOL_TLSv1)
	url = url.read().decode('utf-8')
	dic_url=json.loads(url)
	lists=[]
	name=[]
	for line in range(len(dic_url['data'])):
		lists.append('https://www.feixiaohao.com/exchange/'+dic_url['data'][line]['id']+'/')
		name.append(dic_url['data'][line]['name'])
	for l in range(len(lists)):
		html=urlopen(lists[l])
		html=html.read().decode('utf-8')
		re_url = re.findall('官网地址</span> <span class="val"><a href="(.*?)" target',html,re.S)
		print('%s：%s'% (name[l],re_url[0])) 
		with open('jiaoyisuo.txt','a') as f:
			f.write("%s：%s \n"% (name[l],re_url[0]))