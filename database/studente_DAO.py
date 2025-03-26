#Add whatever it is needed to interface with the DB Table studente
from oauthlib.uri_validate import query

from database.DB_connect import get_connection

def cerca_studente(valore):
    cnx=get_connection()
    cursor = cnx.cursor()
    cursor.execute(f"select nome,cognome from studente where matricola=\"{valore}\"" )
    rows = cursor.fetchall()
    cnx.close()
    return rows

def cerca_iscrizioni(matricola):
    cnx=get_connection()
    cursor = cnx.cursor()
    cursor.execute(f"select nome,iscrizione.codins from iscrizione join corso on corso.codins=iscrizione.codins where matricola=\"{matricola}\"" )
    rows = cursor.fetchall()
    cnx.close()
    return rows

def iscrivi_studente(matricola,corso):
    cnx=get_connection()
    cursor = cnx.cursor()
    cursor.execute(f"select * from studente where matricola=\"{matricola}\"")
    rows = cursor.fetchall()
    if len(rows)==0:
        return "Matricola non valida"
    cursor.execute(f"select nome,iscrizione.codins from iscrizione join corso on corso.codins=iscrizione.codins where matricola=\"{matricola}\" AND iscrizione.codins=\"{corso}\"" )
    rows = cursor.fetchall()
    if len(rows)!=0:
        return "Studente già iscritto al corso"
    intmatricola=int(matricola)
    sql = "INSERT INTO iscrizione (matricola, codins) VALUES (%s, %s)"
    cursor.execute(sql, (intmatricola, corso))
    cnx.commit()
    cursor.fetchall()
    cnx.close()
    return "Iscrizione avvenuta con successo"