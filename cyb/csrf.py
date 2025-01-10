import requests
import json


s=requests.Session()
url = 'http://web-11.challs.olicyber.it/login'
payload2 = {'username': 'admin','password':'admin'}
res2=s.post(url, json=payload2)
csrf_token=res2.json().get("csrf")
print( res2.text)
print (csrf_token)
flag_url='http://web-11.challs.olicyber.it/flag_piece'
flag=''

for i in range(1,4,1) :

    print (i)
    #headers={'csrf': csrf_token}
    print(type(csrf_token))
    param={'index': i,'csrf': csrf_token}
    print (csrf_token)
    #print(headers)
    print(param)
    flag_response=s.get(flag_url,params=param)

    print(flag_response.url)
    print (flag_response.text)

    if flag_response.status_code==200:

        csrf_token=flag_response.json().get("csrf")
        print(csrf_token) 


        flag_piece=flag_response.text
        flag +=flag_piece
    
    else: 
        print(f'Errore allo step: {i}')
        exit()

print("Ce l'ho fatta? ",flag)


