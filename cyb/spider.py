import requests
from bs4 import BeautifulSoup

# URL di partenza
start_url = "http://web-16.challs.olicyber.it"

# Insieme delle pagine già visitate
visited_urls = set()

def find_flag(url):
    # Se la pagina è già stata visitata, non la analizziamo di nuovo
    if url in visited_urls:
        return False
    

    # Aggiungiamo la pagina all'insieme delle pagine visitate
    visited_urls.add(url)
    
    try:
        # Effettuiamo la richiesta alla pagina
        response = requests.get(url)
        
        # Verifichiamo che la richiesta sia andata a buon fine
        if response.status_code != 200:
            print(f"Errore nella richiesta a {url}")
            return False

        # Creiamo un oggetto BeautifulSoup per analizzare il contenuto della pagina
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Cerchiamo la flag nel tag <h1>
        h1_tag = soup.find('h1')
        if h1_tag and "flag{" in h1_tag.text:
            print("Flag trovata:", h1_tag.text)
            return True

        # Troviamo tutti i link (<a>) per continuare l'esplorazione
        links = soup.find_all('a', href=True)
        
        # Analizziamo ciascun link
        for link in links:
            next_url = link['href']
            
            # Se il link è relativo, lo rendiamo assoluto
            if not next_url.startswith("http"):
                next_url = start_url + next_url
            
            # Chiamata ricorsiva per esplorare la pagina successiva
            if find_flag(next_url):
                return True
    
    except Exception as e:
        print(f"Errore durante l'accesso a {url}: {e}")

    return False

find_flag(start_url)