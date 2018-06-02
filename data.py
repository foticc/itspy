# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup



url = 'http://www.18183.com/yys/201610/xsfy.html'

response = requests.get(url)

response.encoding = 'utf-8'
text = response.text

data = BeautifulSoup(text,'html.parser')

head = data.select('div.panel-content div.cp')
easy = data.select('div.panel-content div.cp div.tb-w.clx div.tb-cl.tb-l')
hard = data.select('div.panel-content div.cp div.tb-w.clx div.tb-cl.tb-r')


for x in head:
	a = x.find_all('div',class_='tb-hd')
	y = x.find_all("div",class_='tb-cl tb-l')
	z = x.find_all('div',class_='tb-cl tb-r')
	print(a[0].get_text())
	for n in y:
		print(n)
