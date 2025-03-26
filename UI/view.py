import flet as ft


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
        self._title = None
        self.ddCorso = None
        self.btn_CI = None
        self.txt_matricola = None
        self.txt_nome = None
        self.txt_cogonome = None
        self.btn_cercaS = None
        self.btn_cercaC = None
        self.btnI = None
        self.txt_result = None
        self.txt_container = None

    def load_interface(self):
        """Function that loads the graphical elements of the view"""
        # title
        self._title = ft.Text("App gestione studenti", color="blue", size=24)
        self._page.controls.append(self._title)

        #ROW1 cerca corsi
        self.ddCorso = ft.Dropdown(
            width=780,
            label="Selezionare un corso",
            options=self._controller.get_options()
        )
        self.btn_CI = ft.ElevatedButton(text="Cerca iscritti", on_click=self._controller.handle_cerca_iscritti)
        row1 = ft.Row([self.ddCorso, self.btn_CI],
                      alignment=ft.MainAxisAlignment.CENTER)

        #Row2 Matricola, nome e cognome
        self.txt_matricola = ft.TextField(label="Matricola")
        self.txt_nome = ft.TextField(label="Nome", read_only=True)
        self.txt_cognome = ft.TextField(label="Cognome", read_only=True)
        row2 = ft.Row([self.txt_matricola, self.txt_nome, self.txt_cognome],
                      alignment=ft.MainAxisAlignment.CENTER)

        #Row3 Buttons
        self.btn_cercaS = ft.ElevatedButton(text="Cerca Studente", on_click=self._controller.handle_cerca_studente)
        self.btn_cercaC = ft.ElevatedButton(text="Cerca Corso", on_click=self._controller.handle_cerca_corso)
        self.btnI = ft.ElevatedButton(text="Iscrivi", on_click=self._controller.handle_iscrizione)
        row3 = ft.Row([self.btn_cercaS, self.btn_cercaC, self.btnI],alignment=ft.MainAxisAlignment.CENTER)

        self._page.add(row1,row2,row3)

        # List View where the reply is printed
        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
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
