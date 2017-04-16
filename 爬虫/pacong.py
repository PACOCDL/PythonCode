# coding:utf8
import urllib
import re
import time
 # 通过filename设置路径和名字
response=urllib.urlopen('https://www.douyu.com/directory/game/TVgame')
html=response.read()
code=
print html
imglist=re.findall(r'data-original="(.*?\.(jpg|png))"',html)
print imglist
x=0
for imgurl in imglist:
    print ('下载图片 %s'%imgurl[0])
    if imgurl[1]=='gif':
        urllib.urlretrieve(imgurl[0],filename='G:\PythonCode\pic\%d.gif'%x)
    else:
        urllib.urlretrieve(imgurl[0],filename='G:\PythonCode\pic\%d.jpg'%x)
    x+=1
    time.sleep(1)