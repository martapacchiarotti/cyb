

import requests

payload = {'id': 'flag'}
res=requests.get("http://web-02.challs.olicyber.it/server-records", params=payload)

print( res.url)
print( res.text)