# Add whatever it is needed to interface with the DB Table corso
from database.DB_connect import get_connection

def get_corsi():
    cnx=get_connection()
    cursor = cnx.cursor()
    cursor.execute("select * from corso ")
    rows=cursor.fetchall()
    cnx.close()
    return rows

def get_studenti_iscritti(valore):
    cnx=get_connection()
    cursor = cnx.cursor()
    cursor.execute(f"select iscrizione.matricola,nome,cognome from studente JOIN iscrizione on studente.matricola=iscrizione.matricola where codins=\"{valore}\"")
    rows=cursor.fetchall()
    cnx.close()
    return rows

