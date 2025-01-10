import requests
from bs4 import BeautifulSoup, Comment


url='http://just-a-reminder.challs.olicyber.it/default.js'
res=requests.get(url)
content=res.text

print (content)

#soup=BeautifulSoup(content,"html.parser")

#resources = []

#for link in soup.find_all('link', href=True):
#        resources.append(link['href'])
#for script in soup.find_all('img', src=True):
#        resources.append(script['src'])

#print(resources)

#for resurce in resources:
 #       nuova_url=url + resurce
  #      print(nuova_url)
   #     response = requests.get(nuova_url)
        
        # Se la richiesta ha successo, cerchiamo la flag nel contenuto
     #   if response.status_code == 200:
    #        content = response.text
    #        if "flag{" in content:
    #            print(f"Flag trovata in {nuova_url}:")
                # Stampiamo solo la parte del contenuto che include la flag
   #             flag_index = content.find("flag{")
    #            end_index = content.find("}", flag_index) + 1
     #           print(content[flag_index:end_index])



