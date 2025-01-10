import os

def read_file(file_name):
    # Il percorso della directory di base dove dovrebbero essere letti i file
    base_directory = "documents/"

    # Genera il percorso completo del file
    file_path = os.path.join(base_directory, file_name)

    try:
        # Legge e restituisce il contenuto del file
        with open(file_path, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        return "File non trovato."
    except Exception as e:
        return f"Errore: {str(e)}"

# Esempio di utilizzo
print(read_file("note.txt"))  # File valido
print(read_file("../../etc/passwd"))  # Tentativo di path traversal
