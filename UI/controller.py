import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handle_cerca_iscritti(self, e):
        """Simple function to handle a button-pressed event,
        and consequently print a message on screen"""
        name = self._view.txt_name.value
        if name is None or name == "":
            self._view.create_alert("Inserire il nome")
            return
        self._view.txt_result.controls.append(ft.Text(f"Hello, {name}!"))
        self._view.update_page()

    def get_options(self):
        lista=self._model.corsi()
        options=[]
        for i in lista:
            options.append(ft.dropdown.Option(key=i[0],text=f"{i[2]} ({i[0]})"))
        return options

    def handle_cerca_iscritti(self,e):
        self._view.txt_result.controls.clear()
        self._view.update_page()
        if self._view.ddCorso.value is None:
            self._view.txt_result.controls.append(ft.Text("Selezionare un corso", color="red"))
        else:
            list=self._model.iscritti_corso(self._view.ddCorso.value)
            for i in list:
                self._view.txt_result.controls.append(ft.Text(f"{i[1]} {i[2]} ({i[0]})"))
        self._view.update_page()

    def handle_cerca_studente(self, e):
        self._view.txt_result.controls.clear()
        self._view.txt_nome.value=""
        self._view.txt_cognome.value=""
        self._view.update_page()
        if self._view.txt_matricola.value == "":
            self._view.txt_result.controls.append(ft.Text("Inserire una matricola", color="red"))
        else:
            list=self._model.studente(self._view.txt_matricola.value)
            if len(list) == 0:
                self._view.txt_result.controls.append(ft.Text("Inserire una matricola valida", color="red"))
            else:
                for i in list:
                    self._view.txt_nome.value=i[0]
                    self._view.txt_cognome.value=i[1]
        self._view.update_page()

    def handle_cerca_corso(self, e):
        self._view.txt_result.controls.clear()
        self._view.update_page()
        if self._view.txt_matricola.value == "":
            self._view.txt_result.controls.append(ft.Text("Cercare uno studente", color="red"))
        else:
            list=self._model.studente_iscrizioni(self._view.txt_matricola.value)
            if len(list) == 0:
                self._view.txt_result.controls.append(ft.Text("Matricola non trovata", color="red"))
            else:
              for i in list:
                    self._view.txt_result.controls.append(ft.Text(f"{i[0]} ({i[1]})"))
        self._view.update_page()

    def handle_iscrizione(self,e):
        self._view.txt_result.controls.clear()
        self._view.update_page()
        if self._view.txt_matricola=="" or self._view.ddCorso.value=="":
            self._view.txt_result.controls.append(ft.Text("Inserire tutti i parametri", color="red"))
        else:
            list=self._model.studente(self._view.txt_matricola.value)
            if len(list) == 0:
                self._view.txt_result.controls.append(ft.Text("Studente o corso non esistenti", color="red"))
            else:
                risultato=self._model.iscrizione(self._view.txt_matricola.value,self._view.ddCorso.value)
                self._view.txt_result.controls.append(ft.Text(risultato, color="green"))
        self._view.update_page()