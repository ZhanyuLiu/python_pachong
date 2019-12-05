import  requests
url = "http://m.ip138.com/ip.asp?ip="
r = requests.get(url+'202.204.80.112')
print(r.status_code)
print(r.text[-500:])

# ip地址查询得全代码
try:
    r = requests.get(url + '202.204.80.112')
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.encoding)
    print(r.text[-500:])
except:
    print("爬取失败")