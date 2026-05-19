from database import corso_DAO, studente_DAO
from model.corso import Corso

# MODEL: dipende dal DAO e usa le sue funzioni

class Model:
    def __init__(self):
        self._mappa_corsi = None
        self._mappa_studenti = dict()       # dizionario che salva gli studenti già caricati dal database

    # Caricare i corsi e popolare il Dropdown: punto in cui entrano insieme Model + DAO + Controller
    # STEP 1 — MODEL: prendere i corsi inseriti nel corso_DAO
    def get_corsi(self):
        if self._mappa_corsi is None:               # se non ho ancora caricato i corsi dal database
            self._mappa_corsi = {}
            # Adesso devo aggiungere i corsi del database (DAO)
            corso_DAO.fill_mappa_corsi(self._mappa_corsi)
        return self._mappa_corsi

    # Se non ho i corsi, li prendo dal database e li salvo in memoria; poi li restituisco al controller.

    # Dammi gli studenti iscritti a quel corso
    def get_iscritti_corso(self, codins):
        if self._mappa_corsi[codins].studenti is None:  # non sono ancora stati caricati studenti in quel corso
            self._mappa_corsi[codins].studenti = corso_DAO.get_iscritti_corso(codins)
        return self._mappa_corsi[codins].studenti

    # Dammi lo studente con questa matricola
    def cerca_studente(self, matricola):
        if self._mappa_studenti.get(matricola) is None:
            studente_DAO.cerca_studente(matricola, self._mappa_studenti)
        return self._mappa_studenti.get(matricola)

    def get_corsi_studente(self, matricola):
        studente = self.cerca_studente(matricola)
        if studente is None:
            return None
        else:
            if studente.corsi is None:      # non sono ancora stati caricati corsi per quello studente
                studente.corsi = set()      # creo un insieme vuoto di corsi
                corso_DAO.get_corsi_studente(matricola, studente)
            return studente.corsi

    # Iscrivi uno studente ad un corso
    def iscrivi_corso(self, matricola, codins):
        if self._mappa_studenti[matricola].corsi is None:
            self._mappa_studenti[matricola].corsi = set()       # lo inizializzo come set
        self._mappa_studenti[matricola].corsi.add(self._mappa_corsi[codins])
        return corso_DAO.iscrivi_corso(matricola, codins)