import requests
from bs4 import BeautifulSoup
import bs4

# 获取网页内容
def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

# 获取合适的数据
def fillUnivList(ulist,html):
    soup = BeautifulSoup(html,"html.parser")
    for tr in soup.find('tbody').children:
        if isinstance(tr,bs4.element.Tag):
            tds = tr('td')
            ulist.append([tds[0].string,tds[1].string,tds[2].string])
    # pass

# 展示输出
def printUnivList(ulist,num):
    # {3}表示在填充的时候使用format的第三个参数来填充，也就是中文，默认是英文填充
    tplt = "{0:^10}\t{1:{3}^10}\t{2:^10}"
    # chr(12288)添加中文空格
    print(tplt.format("排名","学校名称","总分",chr(12288)))
    for i in range(num):
        u = ulist[i]
        print(tplt.format(u[0],u[1],u[2],chr(12288)))

def main():
    uinfo = []
    url = 'http://www.zuihaodaxue.com/zuihaodaxuepaiming2019.html'
    html = getHTMLText(url)
    fillUnivList(uinfo,html)
    printUnivList(uinfo,350)

main()
















