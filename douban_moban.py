# coding: utf-8
'''
使用爬虫基本模板
'''

import requests
from lxml import etree

print __doc__

url = 'https://music.douban.com/top250'
try:
    kv = {'User - Agent': 'Mozilla / 5.0'}
    r = requests.get(url, headers=kv)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    html = r.text
except Exception, e:
    print e.message
else:
    print 'no_error'

s = etree.HTML(html)
title = s.xpath('//*[@id="content"]/div/div[1]/div/table[1]/tr/td[2]/div/a/text()')[0]
score = s.xpath('//*[@id="content"]/div/div[1]/div/table[1]/tr/td[2]/div/div/span[2]/text()')
numbers = s.xpath('//*[@id="content"]/div/div[1]/div/table[1]/tr/td[2]/div/div/span[3]/text()')[0]
music = s.xpath('//*[@id="content"]/div/div[1]/div/table[1]/tr/td[2]/div/a/@href')[0]
img = s.xpath('//*[@id="content"]/div/div[1]/div/table[1]/tr/td[1]/a/img/@src')[0]

print title, numbers, score, music, img






