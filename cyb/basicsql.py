import requests
from bs4 import BeautifulSoup, Comment

url='http://click-me.challs.olicyber.it'
cookies = {'cookies': '10000000'}

res=requests.get(url,cookies=cookies)
print=res.cookies

print (res.text)