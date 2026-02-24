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
    genere = str(input("Genere: ")).strip()
    if not genere:
        print("Genere non può essere vuoto.")
        return
    risultati = []
    for i in libri:
        if genere in libri:
            risultati.append(i)
    
    
    print(f"Libri di {genere}")
    for l in libri:
        print(f"-{l["titolo"]}")

def calcola_media_anno(libri: list[dict]) -> float:
    if not libri:
        return 0.0
    somma = sum(libro["anno"] for libro in libri)
    return somma / len(libri)
    












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
    
    if libri_caricati:
        libri = filtra_per_genere(libri_caricati, "libri")
    media = calcola_media_anno(libri_caricati)
    print(f"Media anno di pubblicazione: {media:.1f}")



main()