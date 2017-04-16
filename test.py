# coding:utf-8
import urllib

from urllib import request


page = 1
url = 'http://www.qiushibaike.com/hot/page/' + str(page)
try:
    a = urllib.request.Request(url)
    response = urllib.request.urlopen(a)
    print(response.read())
except urllib.request.URLError as e:
    if hasattr(e, "code"):
        print(e.code)
    if hasattr(e, "reason"):
        print(e.reason)
