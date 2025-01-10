import requests

#richiesta di cookie
url3 = 'http://web-05.challs.olicyber.it/flag'
cookies = {'password': 'admin'}
res3=requests.get(url3,cookies=cookies)
print( res3.cookies)
print(res3.text)


url = 'http://web-06.challs.olicyber.it/token'
s=requests.Session()

cookies = {'password': 'admin'}
res=s.get(url)
print( res.cookies)
res2=s.get('http://web-06.challs.olicyber.it/flag')
print(res2.text)