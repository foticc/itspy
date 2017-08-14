import requests
from bs4 import BeautifulSoup
import time


url = 'http://www.lrcgc.com'
home = '/artist-00.html'

#home'div.artist_category dl.current dd p a'
def spider(url,select):
	response = requests.get(url)
	print dir(response)
	print response.status_code
	soup = BeautifulSoup(response.text,'lxml')
	context = soup.select(select)
	print context
	return context


def get_singer_list(url,select):
	for x in spider(url, select):
		print x.text
		
if __name__ == '__main__':
	get_singer_list(url+home,'.current dd p a')