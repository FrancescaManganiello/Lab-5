from database.DB_connect import get_connection
from model.studente import Studente


def cerca_studente(matricola, mappa_studenti):
    """
        Funzione che data una matricola ricerca nel database lo studente corrispondente (se presente)
        :param matricola: la matricola dello studente da ricercare
        :param mappa_studenti: una mappa di studenti. Le keys sono le matricole, i values sono oggetti Studente
        :return: uno studente, se presente
    """
    cnx = get_connection()
    if cnx is not None:
        cursor = cnx.cursor(dictionary=True)
        cursor.execute("SELECT * FROM studente WHERE matricola = %s", (matricola,))
        row = cursor.fetchone()
        if row is not None:
            mappa_studenti[matricola] = Studente(**row)
        cursor.close()
        cnx.close()
    else:
        print("Could not connect")
