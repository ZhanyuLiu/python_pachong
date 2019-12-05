import requests
path = "G:/研1803/01课程/爬虫/abc.jpg"
url = "http://image.nationalgeographic.com.cn/2017/0211/20170211061910157.jpg"
r = requests.get(url)
print(r.status_code)

# 保存图片
with open(path,'wb') as f:
    f.write(r.content)
f.close()


# 图片爬取全部代码
import os
url = "http://image.nationalgeographic.com.cn/2017/0211/20170211061910157.jpg"
root = "G:/研1803/01课程/爬虫//pics//"
# 保存网站中图片本生得名字，截取最后一个反斜杠后得名字
path = root + url.split('/')[-1]
try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r = requests.get(url)
        with open(path,'wb') as f:
            f.write(r.content)
            f.close()
            print("文件保存成功")
    else:
        print("文件已存在")
except:
    print("爬取失败")