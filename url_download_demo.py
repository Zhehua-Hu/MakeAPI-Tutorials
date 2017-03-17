#!/usr/bin/python
# coding=utf-8
"""
Threee Methods to download file from url.

"""


url = 'http://zhehua.info/assets/images/blog/EnchainLogoLittle.png'
savename = "/home/zhehua/EnchainLogoLittle3.png"


## Method 1
import urllib
urllib.urlretrieve(url, savename)

## Method 2
# import urllib2
# f = urllib2.urlopen(url)
# data = f.read()
# with open(savename, "wb") as code:
#     code.write(data)

## Method 3
# import requests
# r = requests.get(url)
# with open(savename, "wb") as code:
# 	code.write(r.content)