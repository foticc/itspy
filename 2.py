import requests
from bs4 import BeautifulSoup


url = 'http://www.lrcgc.com/artist-11.html'
response = requests.get(url)
soup = BeautifulSoup(response.text,'lxml')
name = soup.select('div[class="namelist"] ul li a')
for x in name:
	print x.get_text().strip(),x['href']#strip lose the space
	# r = requests.get('http://www.lrcgc.com/'+x['href'])
	# con = BeautifulSoup(r.text,'lxml')
	# song = con.select('div.thread_posts_list table tbody tr td a')
	# for y in song:
	# 	print y.get_text()