import requests
# kv = {'wd':'Python'}
# r = requests.get("http://www.baidu.com/s",params=kv)
# print(r.status_code)
# print(r.request.url)
# print(len(r.text))


# 百度搜索的全代码
keyword = "Python"
try:
    kv = {'wd':keyword}
    r = requests.get("http://www.baidu.com/s",params=kv)
    print(r.status_code)
    print(r.request.url)
    print(len(r.text))
except:
    print("爬取失败")

# 360搜索的全代码
try:
    kv = {'q':keyword}
    r = requests.get("http://www.so.com/s",params=kv)
    print(r.request.url)
    # print(r.raise_for_status())
    print(r.status_code)
    print(len(r.text))
except:
    print("爬取失败")