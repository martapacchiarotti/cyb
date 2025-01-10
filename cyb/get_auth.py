import requests
url = 'http://web-03.challs.olicyber.it/flag'

headers = {'X-Password': 'admin'}


res=requests.get(url, headers=headers)

print( res.url)
print( res.text)

#chiedere header inxml invece che json
url2 = 'http://web-04.challs.olicyber.it/users'
headers = {'Accept': 'application/xml'}
res2=requests.get(url2, headers=headers)
print( res2.headers)
print(res2.text)



#richiesta di cookie
url3 = 'http://web-05.challs.olicyber.it/flag'
headers = {'Accept': 'application/xml'}
res3=requests.get(url3)
print( res.cookies)
print(res2.text)