
'''
just xpath
'''
print __doc__
import requests
from lxml import etree

url = 'https://music.douban.com/top250'
html = requests.get(url).text
s = etree.HTML(html)
title = s.xpath('//*[@id="content"]/div/div[1]/div/table[1]/tr/td[2]/div/a/text()')[0]
score = s.xpath('//*[@id="content"]/div/div[1]/div/table[1]/tr/td[2]/div/div/span[2]/text()')
numbers = s.xpath('//*[@id="content"]/div/div[1]/div/table[1]/tr/td[2]/div/div/span[3]/text()')[0]
music = s.xpath('//*[@id="content"]/div/div[1]/div/table[1]/tr/td[2]/div/a/@href')[0]
img = s.xpath('//*[@id="content"]/div/div[1]/div/table[1]/tr/td[1]/a/img/@src')[0]
print title, numbers, score, music, img




