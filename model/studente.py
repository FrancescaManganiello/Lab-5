from dataclasses import dataclass

@dataclass()
class Studente:
    matricola: int
    cognome: str
    nome: str
    CDS: str

    # relazione
    corsi: set = None           # un set di corsi a cui è iscritto lo studente

    def __str__(self):
        return f"{self.nome}, {self.cognome} ({self.matricola})"

    def __eq__(self, other):
        return self.matricola == other.matricola

    def __hash__(self):
        return hash(self.matricola)