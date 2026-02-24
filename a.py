  git config --global user.email "felipemichele.divirgilio@studenti.isissgobetti.it"
  git config --global user.name "Felipe Di Virgilio"
def filtra_per_genere(libri: list[dict], genere: str) -> list[dict]:
    filtrati = []
    for libro in libri:
        if libro ["genere"] == genere:
            filtrati.append(libro)
    return filtrati