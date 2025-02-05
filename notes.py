from connectDB_ import se_connecter

def ajouterNote(texte, idUtilisateur):
    conn, cursor = se_connecter()
    
    try:
        cursor.execute('''INSERT INTO "Notes" ("Texte", "ID_utilisateur") 
                          VALUES(?,?)''',
                       (texte,idUtilisateur))
        conn.commit()
        print("La note a été enregistrée avec succès.")

        cursor.execute('''SELECT * FROM Notes WHERE ID_utilisateur = ? ORDER BY ID_note DESC LIMIT 1''',
                       (idUtilisateur,))
        noteAjoute = cursor.fetchone()
        return noteAjoute
    except Exception as e:
        raise Exception(f"Erreur : {e}")
    finally:
        conn.close()

def lireNotes(id_):
    conn, cursor = se_connecter()
    
    try:
        cursor.execute('''SELECT * FROM "Notes" WHERE ID_utilisateur = ? ORDER BY ID_note DESC''', (id_,))
        note = cursor.fetchall()
        return note
    except Exception as e:
        raise Exception(f"Erreur : {str(e)}")
    finally:
        conn.close()


def lireNote(id_):
    conn, cursor = se_connecter()

    try:
        cursor.execute('''SELECT * FROM "Notes" WHERE ID_note = ? ''', (id_,))
        note = cursor.fetchone()
        return note
    except Exception as e:
        raise Exception(f"Erreur : {str(e)}")
    finally:
        conn.close()

def mettreAJourNote(idNote, texte):
    conn, cursor = se_connecter()
    
    try:
        cursor.execute('''UPDATE "Notes" SET "Texte" = ? WHERE ID_note = ?''',
                       ( texte, idNote))
        conn.commit()
        print("La note a été mise à jour avec succès.")
        return True
    except Exception as e:
        raise Exception(f"Erreur : {str(e)}")
    finally:
        conn.close()

def supprimerNote(idNote):
    conn, cursor = se_connecter()
    
    try:
        cursor.execute('''DELETE FROM "Notes" WHERE ID_note = ?''', (idNote,))
        conn.commit()
        print("La note a été supprimée avec succès.")
        return True
    except Exception as e:
        raise Exception(f"Erreur : {str(e)}")
    finally:
        conn.close()