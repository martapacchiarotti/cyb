import requests
import json

payload = {'username': 'admin','password':'admin'}
res=requests.post("http://web-08.challs.olicyber.it/login", data=payload)

print( res.url)
print( res.text)



payload2 = {'username': 'admin','password':'admin'}
res2=requests.post("http://web-09.challs.olicyber.it/login",  json=payload2)
print( res2.url)
print( res2.text)
