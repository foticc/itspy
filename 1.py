#encoding:utf-8
import requests
from bs4 import BeautifulSoup
import json
import sys
import re
import jieba
reload(sys)
sys.setdefaultencoding("utf8")

#url = 'https://github.com/timeline.json'
url = 'http://www.lrcgc.com/lyric-210-301333.html'
response = requests.get(url)
soup = BeautifulSoup(response.text,"lxml")
lrc = soup.find_all(id="J_lyric")
lrc = lrc[0].get_text()
lrc = re.sub('\[\d*\:\d*\.\d*\]', ' ', lrc, count=0, flags=0)
seg_list = jieba.cut(lrc)
print ",".join(seg_list)