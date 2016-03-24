#-*- coding : utf-8 -*-

#crawler for BBS top ten

from urllib.request import urlopen
from bs4 import BeautifulSoup
import http.cookiejar

def newsmth_top10():
    agent = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.72 Safari/537.36'}
    content = urlopen('http://www.newsmth.net/nForum/#!mainpage').read()
    soup = BeautifulSoup(content)

    top_ten_str = soup.find(id = 'top10')
    print(top_ten_str)

def test():
    content = urlopen('http://tnt.kuaizhan.com/company/gossip/109', timeout = 5).read()
    soup = BeautifulSoup(content)
    for title in soup.find_all('p', {"class" : "list-title"}):
        print(title.get_text())

test()