import requests
r = requests.get("http://python123.io/ws/demo.html")
# print(r.text)
demo = r.text
from bs4 import BeautifulSoup
soup = BeautifulSoup(demo,"html.parser")
# BeautifulSoup的两种形式
# soup1 = BeautifulSoup("<html>data</html>","html.parser")
# soup2 = BeautifulSoup(open("D://demo.html"),"html.parser")
print(soup.title)
tag = soup.a
print(tag.attrs)
# 获取class值
print(tag.attrs['class'])
print(tag.attrs['href'])
print(soup.a.name)
print(soup.a.parent.name)
print(soup.a.parent.parent.name)
print(tag)
print(type(tag.attrs))
print(type(tag))
print(soup.a.string)
# print(soup.prettify())

# 当出现注释时，该怎么操作
newsoup = BeautifulSoup("<b><!--This is a comment--></b><p>Thia is a not a comment</p>","html.parser")
# 在通常的分析文本中，判断注释一般使用查看类型的形式
print(newsoup.b.string)
print(type(newsoup.b.string))
print(soup.head)
print(soup.head.contents)
# body中儿子节点的数量
print(len(soup.body.contents))
# 获取第一个节点
print(soup.body.contents[1])

# 父亲节点
print(soup.title.parent)
print(soup.html.parent)













