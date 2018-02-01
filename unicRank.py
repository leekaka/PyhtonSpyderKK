# CrawUnivRankingB.py
import requests
from bs4 import BeautifulSoup
import bs4


def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""


def fillUnivList(ulist, html):
    soup = BeautifulSoup(html, "html.parser")
    for tr in soup.find('tbody').children:
        if isinstance(tr, bs4.element.Tag):
            tds = tr('td')
            ulist.append([tds[0].string, tds[1].string,tds[2].string, tds[3].string])


def printUnivList(ulist, num):
    tplt = "{0:^10}\t{1:{4}^10}\t{2:^10}\t{3:^10}"  # #{4},代表用format的第四个变量填充没用完的位置 即chr(12288)
    print(tplt.format("\n排名", "学校名称", "地域","总分", chr(12288)))
    for i in range(num):
        u = ulist[i]
        print(tplt.format(u[0], u[1], u[2], u[3], chr(12288)))
    with open('uniRank.txt','w') as fwiter:
        fwiter.write(tplt.format("排名", "学校名称", "地域","总分\n", chr(12288)))
        for i in range(num):
            u = ulist[i]
            fwiter.write(tplt.format(u[0], u[1], u[2], u[3], chr(12288)) + '\n')



def main():
    n = int(input('please iput a number(全国排名前多少)：'))
    uinfo = []
    url = 'http://www.zuihaodaxue.cn/zuihaodaxuepaiming2016.html'
    html = getHTMLText(url)
    fillUnivList(uinfo, html)
    printUnivList(uinfo, n)  # n univs
    print('\n数据来源于最好大学网，排名根据录取分数')
    input("\n\nPress the enter key to exit.")


if __name__ == '__main__':
    main()
