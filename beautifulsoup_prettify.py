import requests
r = requests.get("http://python123.io/ws/demo.html")
# print(r.text)
demo = r.text
from bs4 import BeautifulSoup
soup = BeautifulSoup(demo,"html.parser")
# # 添加换行符
# print(soup.prettify())
# # 查找出所有的a标签
# for link in soup.find_all('a'):
#     print(link.get('href'))
import re
for tag in soup.find_all(re.compile('b')):
    print(tag.name)
print(soup.find_all('p','course'))
print(soup.find_all(id = 'link1'))

# 使用正则表达式
print(soup.find_all(string = "Basic Python"))
print(soup.find_all(string = re.compile("Python")))