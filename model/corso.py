from dataclasses import dataclass

@dataclass()
class Corso:
    # Attributi del Corso
    codins: str
    crediti: int
    nome: str
    pd: int

    # relazione
    studenti: set = None    # Ho aggiunto manualmente un “contenitore” dentro il corso che serve per:
                            # memorizzare gli studenti iscritti a quel corso

    def __str__(self):
        return f"{self.nome} ({self.codins})"

    def __eq__(self, other):
        return self.codins == other.codins

    def __hash__(self):
        return hash(self.codins)
