import requests
from bs4 import BeautifulSoup

# URL di partenza
start_url = "http://web-16.challs.olicyber.it"

response = requests.get(start_url)

#soup = BeautifulSoup(response.text, 'html.parser')
print(response.text)
        