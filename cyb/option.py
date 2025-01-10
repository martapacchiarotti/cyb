import requests
import json

payload = {'username': 'admin','password':'admin'}

res=requests.options("http://web-10.challs.olicyber.it")

print( res.url)
print( res.headers)
print( res.text)


res=requests.patch("http://web-10.challs.olicyber.it")
print( res.text)
print (res.headers)





