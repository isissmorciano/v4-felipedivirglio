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
    except FileNotFoundError


























def main() -> None:
    libri = [
    {"titolo": "Il piccolo principe", "genere": "Romanzo", "anno": 1943},
    {"titolo": "1984", "genere": "Fantascienza", "anno": 1949},
    {"titolo": "Dune", "genere": "Fantascienza", "anno": 1965},
    {"titolo": "Harry Potter", "genere": "Fantasy", "anno": 1997}
    ]