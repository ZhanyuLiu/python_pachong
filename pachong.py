import  requests
# r = requests.get("https://item.jd.com/2967929.html")
# print(r.status_code)
# print(r.encoding)
# print(r.text[:1000])
# 1.全代码
# url = "https://item.jd.com/2967929.html"
# try:
#     r = requests.get(url)
#     r.raise_for_status()
#     r.encoding = r.apparent_encoding
#     print(r.text[:1000])
# except:
#     print("爬取失败")


# 2.亚马逊
# r = requests.get("https://www.amazon.cn/gp/product/B01M8L52.html")
# # print(r.status_code)
# r.encoding = r.apparent_encoding
# # print(r.encoding)
# # print(r.text[:1000])

# # 查看我们是使用什么访问网站的
# print(r.request.headers)

# 网站识别此次访问为爬虫，将其屏蔽，使用浏览器访问，就需要更改访问头部
# 更改访问头部
kv = {'User-Agent':'Mozilla/5.0'}
url = "https://www.amazon.cn/gp/product/B01M8L5Z3Y"
r = requests.get(url,headers= kv)
print(r.status_code)
print(r.request.headers)
print(r.text[:1000])


