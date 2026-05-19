import flet as ft

# CONTROLLER: dipende dal model

class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

        # il corso selezionato nel menu a tendina
        self.codins_corso_selezionato = None

    # Popolamento dropdown: succede solo 1 volta ed è l'inizializzazione
    def populate_dd_corso(self):
        for codins, corso in self._model.get_corsi().items():
            self._view.dd_corso.options.append(ft.dropdown.Option(key=corso.codins, text=corso.__str__()))
        self._view.update_page()

        # 1. prende i corsi dal MODEL
        # 2. li scorre uno a uno
        # 3. crea le Dropdown.Option
        # 4. le inserisce direttamente nella VIEW
        # 5. aggiorna la pagina

    # Salvo nel controller il corso che l’utente ha selezionato nel menu a tendina
    def leggi_corso(self, e):   # succede OGNI VOLTA che l’utente cambia selezione e registra le sue scelte
        self.codins_corso_selezionato = self._view.dd_corso.value

    def cerca_iscritti(self, e):
        #  Se nessun corso è selezionato, avvisare l’utente con un messaggio di errore:
        if self.codins_corso_selezionato is None:
            self._view.create_alert("Selezionare un corso!")
            return

        iscritti = self._model.get_iscritti_corso(self.codins_corso_selezionato)
        if iscritti is None:
            self._view.create_alert("Problema nella connessione!")
            return
        self._view.txt_result.controls.clear()
        if len(iscritti) == 0:
            self._view.txt_result.controls.append(ft.Text("Non ci sono studenti iscritti al corso"))
        else:
            self._view.txt_result.controls.append(ft.Text(f"Ci sono {len(iscritti)} iscritti al corso:"))
            for iscritto in iscritti:
                self._view.txt_result.controls.append(ft.Text(f"{iscritto}"))
            self._view.update_page()

    def cerca_studente(self, e):
        #  Se la matricola non è presente, visualizzare un messaggio di errore:
        matricola = self._view.txt_matricola.value
        if matricola == "":
            self._view.create_alert("Inserire una matricola!")
            return
        studente = self._model.cerca_studente(matricola)
        if studente is None:
            self._view.create_alert("Matricola non presente nel database")
            return
        else:
            self._view.txt_nome.value = f"{studente.nome}"
            self._view.txt_cognome.value = f"{studente.cognome}"

        self._view.update_page()

    def cerca_corsi(self, e):
        #  Se la matricola non è presente, visualizzare un messaggio di errore:
        matricola = self._view.txt_matricola.value
        if matricola == "":
            self._view.create_alert("Inserire una matricola!")
            return

        corsi = self._model.get_corsi_studente(matricola)
        if corsi is None:
            self._view.create_alert("Non risulta nessuno studente con la matricola indicata")
        elif len(corsi) == 0:
            self._view.create_alert("Non risulta nessun corso per questa matricola")
        else:
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text(f"Risultano {len(corsi)} corsi:"))
            for corso in corsi:
                self._view.txt_result.controls.append(ft.Text(f"{corso}"))
            self._view.update_page()

    def iscrivi(self, e):
        matricola = self._view.txt_matricola.value
        if matricola == "":
            self._view.create_alert("Inserire una matricola")
            return
        studente = self._model.cerca_studente(matricola)
        if studente is None:
            self._view.create_alert("Matricola non presente nel database")
            return
        if self.codins_corso_selezionato is None:
            self._view.create_alert("Selezionare un corso")
            return
        result = self._model.iscrivi_corso(matricola, self.codins_corso_selezionato)
        self._view.txt_result.controls.clear()
        if result:
            self._view.txt_result.controls.append(ft.Text("Iscrizione avvenuta con successo"))
        else:
            self._view.txt_result.controls.append(ft.Text("Iscrizione fallita"))
        self._view.update_page()









