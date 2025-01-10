import requests

s=requests.Session()

cookies = {'password': 'admin'}
res=s.get(url)
print( res.cookies)
res2=s.get('http://web-06.challs.olicyber.it/flag')
print(res2.text)
