import flet as ft

# VIEW: dipende dal controller

class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Lab O5 - segreteria studenti"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None

        # graphical elements
        self.dd_corso = None
        self.btn_cerca_iscritti = None
        self._title = None
        self.txt_matricola = None
        self.txt_nome = None
        self.txt_cognome = None
        self.txt_result = None
        self.btn_cerca_studente = None
        self.btn_cerca_corsi = None

    def load_interface(self):
        """Function that loads the graphical elements of the view"""
        self._title = ft.Text("App Gestione Studenti", color="blue", size=24)
        self._page.controls.append(self._title)

        # ROW with some controls

        # CREO IL DROP DOWN CON I CORSI
        self.dd_corso = ft.Dropdown(
            label = "corso",
            width = 550,
            hint_text = "Selezionare un corso",
            options = [],            # lista con dentro tutti i corsi
            autofocus = True,       # serve a mettere automaticamente il cursore dentro quel controllo appena si apre la finestra.
            on_change = self._controller.leggi_corso
        )

        # PER POPOLARE IL DROPDOWN CON I CORSI
        self._controller.populate_dd_corso()

        # PER IL BUTTON DI Cerca Iscritti
        self.btn_cerca_iscritti = ft.ElevatedButton(
            text = "Cerca Iscritti",
            on_click = self._controller.cerca_iscritti
        )

        row0 = ft.Row([self.dd_corso, self.btn_cerca_iscritti], alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row0)

        # TEXT FIELD PER GLI ALTRI CAMPI

        self.txt_matricola = ft.TextField(
            width = 200,
            hint_text = "matricola"
        )

        self.txt_nome = ft.TextField(
            width=200,
            hint_text="nome",
            read_only = True
        )

        self.txt_cognome = ft.TextField(
            width=200,
            hint_text="cognome",
            read_only=True
        )

        row1 = ft.Row([self.txt_matricola, self.txt_nome, self.txt_cognome],
                      alignment=ft.MainAxisAlignment.CENTER)

        self._page.controls.append(row1)

        # PER IL BUTTON DI Cerca Studente
        self.btn_cerca_studente = ft.ElevatedButton(
            text="Cerca studente",
            on_click=self._controller.cerca_studente,
            tooltip= "Verifica se c'è uno studente con la matricola verificata"
        )

        # PER IL BUTTON DI Cerca corsi
        self.btn_cerca_corsi = ft.ElevatedButton(
            text="Cerca corsi",
            on_click=self._controller.cerca_corsi
        )

        # PER IL BUTTON DI Iscrivi
        self.btn_iscrivi = ft.ElevatedButton(
            text="Iscrivi",
            on_click=self._controller.iscrivi
        )

        row2 = ft.Row([self.btn_cerca_studente, self.btn_cerca_corsi, self.btn_iscrivi],
                      alignment=ft.MainAxisAlignment.CENTER)

        self._page.controls.append(row2)

        # LIST VIEW PER I RISULTATI
        self.txt_result = ft.ListView(
            expand=1,           # dice di occupare tutto lo spazio disponibile
            spacing=10,         # distanza tra un elemento e l’altro della lista.
            padding=20,         # spazio interno ai bordi per non far appiccicare gli elementi ai bordi
            auto_scroll=True    # fa scorrere automaticamente la lista verso il basso quando aggiungi nuovi elementi
        )

        self._page.controls.append(self.txt_result)
        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        """Function that opens a popup alert window, displaying a message
        :param message: the message to be displayed"""
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
