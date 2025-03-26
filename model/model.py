import database.corso_DAO
from database import corso_DAO as DBC
from database import studente_DAO as DBS


class Model:
    def __init__(self):
        self.lista_corsi=[]

    def corsi(self):
        lista=DBC.get_corsi()
        return lista

    def iscritti_corso(self,valore):
        list=DBC.get_studenti_iscritti(valore)
        return list

    def studente(self,valore):
        list= DBS.cerca_studente(valore)
        return list

    def studente_iscrizioni(self,matricola):
        list=DBS.cerca_iscrizioni(matricola)
        return list

    def iscrizione(self,matricola,corso):
        stringa=DBS.iscrivi_studente(matricola,corso)
        return stringa


