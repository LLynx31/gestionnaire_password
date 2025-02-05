from connectDB_ import se_connecter


def ajouterCarteBancaire(numeroCarte, dateExpiatoire, titulaireCarte, cvc2Cvv2, idUtilisateur):
    conn, cursor = se_connecter()

    try:
        cursor.execute('''SELECT * FROM "CarteBancaire" WHERE "Numero_carte" = ?''', (numeroCarte,))
        result = cursor.fetchone()

        if result:
            raise Exception("Le numéro de carte existe déjà. Impossible d'ajouter le numéro de carte.")

        cursor.execute('''INSERT INTO "CarteBancaire" ("Numero_carte", "Date_expiatoire", "Titulaire_carte", "CVC2/CVV2", "ID_utilisateur") 
                          VALUES(?,?,?,?,?)''',
                       (numeroCarte, dateExpiatoire, titulaireCarte, cvc2Cvv2, idUtilisateur))
        conn.commit()
        print("La carte bancaire a été enregistrée avec succès.")

        cursor.execute('''SELECT * FROM "CarteBancaire" WHERE "ID_utilisateur" = ? ORDER BY "ID_carte" DESC LIMIT 1''',
                       (idUtilisateur,))
        cbAjoute = cursor.fetchone()
        return cbAjoute
    except Exception as e:
        raise Exception(f"Erreur : {str(e)}")
    finally:
        conn.close()


def lireCarteBancaire(id_):
    conn, cursor = se_connecter()

    try:
        cursor.execute('''SELECT * FROM "CarteBancaire" WHERE ID_carte = ? ORDER BY ID_carte DESC''', (id_,))
        carte = cursor.fetchone()
        return carte
    except Exception as e:
        raise Exception(f"Erreur : {str(e)}")
    finally:
        conn.close()

def lireCarteBancaires(id_):
    conn, cursor = se_connecter()
    
    try:
        cursor.execute('''SELECT * FROM "CarteBancaire" WHERE ID_utilisateur = ? ORDER BY ID_Carte DESC''', (id_,))
        carte = cursor.fetchall()
        return carte
    except Exception as e:
        raise Exception(f"Erreur : {str(e)}")
    finally:
        conn.close()

def mettreAJourCarteBancaire(idCarte, dateExpiatoire, titulaireCarte, cvc2Cvv2,):
    conn, cursor = se_connecter()
    
    try:
        cursor.execute('''UPDATE "CarteBancaire" SET "Date_expiatoire" = ?, "Titulaire_carte" = ?, "CVC2/CVV2" = ? WHERE ID_carte = ?''',
                       (dateExpiatoire, titulaireCarte, cvc2Cvv2,  idCarte))
        conn.commit()
        print("La carte bancaire a été mise à jour avec succès.")
        return True
    except Exception as e:
        raise Exception(f"Erreur : {str(e)}")
    finally:
        conn.close()

def supprimerCarteBancaire(idCarte):
    conn, cursor = se_connecter()
    
    try:
        cursor.execute('''DELETE FROM "CarteBancaire" WHERE ID_carte = ?''', (idCarte,))
        conn.commit()
        print("La carte bancaire a été supprimée avec succès.")
        return True
    except Exception as e:
        raise Exception(f"Une erreur est survenue : {str(e)}")
    finally:
        conn.close()