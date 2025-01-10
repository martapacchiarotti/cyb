import requests

url=' http://web-12.challs.olicyber.it/'

headers = {'Accept': 'application/html'}
res=requests.get(url,headers=headers)

print(res.text)