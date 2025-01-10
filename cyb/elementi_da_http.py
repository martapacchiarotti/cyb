
from bs4 import BeautifulSoup, Comment
import requests


url='http://web-13.challs.olicyber.it/'
res=requests.get(url)
content=res.text

soup=BeautifulSoup(content,"html.parser")

highlight=soup.find_all(class_="red")

flag="".join(element.get_text() for element in highlight)

print(flag)



url2='http://web-14.challs.olicyber.it/'
res2=requests.get(url2)
content2=res2.text
print(content2)


soup2=BeautifulSoup(content2,"html.parser")

comment=soup2.find_all(string=lambda text: isinstance(text, Comment))

print(f'classi: ', comment)



url3='http://web-15.challs.olicyber.it'
res3=requests.get(url3)
content3=res3.text
print(content3)

soup3=BeautifulSoup(res3.text,"html.parser")

script=soup3.find_all('script', scr=True)

resources = []

for link in soup3.find_all('link', href=True):
        resources.append(link['href'])
for script in soup3.find_all('img', src=True):
        resources.append(script['src'])

#flag=requests.get(script)

print(resources)

for resurce in resources:
        nuova_url=url3 + resurce
        print(nuova_url)
        response = requests.get(nuova_url)
        
        # Se la richiesta ha successo, cerchiamo la flag nel contenuto
        if response.status_code == 200:
            content = response.text
            if "flag{" in content:
                print(f"Flag trovata in {nuova_url}:")
                # Stampiamo solo la parte del contenuto che include la flag
                flag_index = content.find("flag{")
                end_index = content.find("}", flag_index) + 1
                print(content[flag_index:end_index])
        #requests.get(nuova_url)

#soup2=BeautifulSoup(content2,"html.parser")

#comment=soup2.find_all(string=lambda text: isinstance(text, Comment))

#print(f'classi: ', comment)<script src="/dynamic.js"></script>