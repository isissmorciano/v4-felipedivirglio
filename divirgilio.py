import json

def salva_biblioteca(libri: list[dict], nome_file: str) -> None:
    try:
        with open(nome_file, "w", encoding="utf-8") as file:
            json.dump(libri, file, indent=4)
        print(f"File '{nome_file}' salvato con successo")
    except IOError as e:
        print(f"Errore durante il salvataggio del file: {e}")

def carica_biblioteca(nome_file: str) -> list[dict]:
    try:
        with open(nome_file, "r", encoding="utf-8") as file:
            libri = json.load(file)
        return libri
    except FileNotFoundError:
        print(f"Errore il file '{nome_file}' non è stato trovato")
        return []
    except json.JSONDecodeError as e:
        print(f"Errore nel persing JSON: {e}")
        return []

def filtra_per_genere(libri: list[dict], genere: str) -> list[dict]:
    filtrati = []
    for libro in libri:
        if libro ["genere"] == genere:
            filtrati.append(libro)
    return filtrati

























def main() -> None:
    libri = [
    {"titolo": "Il piccolo principe", "genere": "Romanzo", "anno": 1943},
    {"titolo": "1984", "genere": "Fantascienza", "anno": 1949},
    {"titolo": "Dune", "genere": "Fantascienza", "anno": 1965},
    {"titolo": "Harry Potter", "genere": "Fantasy", "anno": 1997}
    ]

    nome_file = "biblioteca.json"
    salva_biblioteca(libri, nome_file)
    libri_caricati = carica_biblioteca(nome_file)
    filtra = filtra_per_genere(libri_caricati, genere: str)
    print(f"Libri di {filtra}")
    print(libri('anno'))
    print(libri('titolo'))
    

main()