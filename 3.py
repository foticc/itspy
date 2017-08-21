import requests
from bs4 import BeautifulSoup
import xlwt
import time

path = 'C:\\Users\\rs\\Desktop\\text.xls'
urlstr = 'http://www.lrcgc.com'
home = '/artist-00.html'
wb = xlwt.Workbook()
sheet = wb.add_sheet('sheet-list',cell_overwrite_ok=True)


def spider(url,select):
	response = requests.get(url)
	soup = BeautifulSoup(response.text,'lxml')
	context = soup.select(select)
	return context

# 'div.artist_category dl.current dd p a' length=9
def get_singer_list(l,select):
	hcontext = spider(l,select)
	i=0
	print len(hcontext),
	for x in hcontext:
		i+=1
		sheet.write(i,0,x.text)
		sheet.write(i,1,x['href'])
		try:
			if x['href']:
				get_singer('http://www.lrcgc.com/'+x['href'],'div.p5 div.namelist ul.cc li a',i)
		except Exception as e:
			continue
		

#'div.p5 div.namelist ul.cc li a'
def get_singer(l,select,i):
	for x in spider(l,select):
		sheet.write(i,3,x.text)
		sheet.write(i,4,x['href'])
		if x['href']:
			get_main_sing_list('http://www.lrcgc.com/'+x['href'],'div.thread_posts_list table tbody tr td a')



#'div.thread_posts_list table tbody tr td a'
def get_main_sing_list(l,select):
	for x in spider(l,select):
		print x.text,x['href']
			
		
get_singer_list(urlstr+home,'div.artist_category dl.current dd p a')
wb.save(path)