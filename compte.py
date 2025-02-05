from connectDB_ import se_connecter


def ajouterApplication(nomApplication,nomSurSite, motPasse, idUtilisateur):
    conn, cursor = se_connecter()

    try:

        cursor.execute('''INSERT INTO compte(Nom_compte, Nom_sur_site, Mot_passe, ID_utilisateur) VALUES(?,?,?,?)''',
                       (nomApplication,nomSurSite, motPasse, idUtilisateur))
        conn.commit()
        print("L'application a été enregistrée avec succès.")

        cursor.execute('''SELECT * FROM compte WHERE ID_utilisateur = ? ORDER BY ID_Compte DESC LIMIT 1''', (idUtilisateur,))
        applicationAjoute = cursor.fetchone()

        return applicationAjoute
    except Exception as e:
        raise Exception(f"Erreur :  {str(e)}")
    finally:
        conn.close()


def lireApplication(id_):
    conn, cursor = se_connecter()

    try:
        cursor.execute('''SELECT * FROM compte WHERE ID_Compte = ?''', (id_,))
        application = cursor.fetchone()
        return application
    except Exception as e:
        raise Exception(f"Erreur : {str(e)}")
    finally:
        conn.close()


def lireApplications(id_):
    conn, cursor = se_connecter()

    try:
        cursor.execute('''SELECT * FROM compte WHERE ID_utilisateur = ? ORDER BY ID_Compte DESC''', (id_,))
        application = cursor.fetchall()
        return application
    except Exception as e:
        raise Exception(f"Erreur : {str(e)}")
    finally:
        conn.close()


def mettreAJourApplication(idApplication, nomApplication, nomSurSite, motPasse, ):
    conn, cursor = se_connecter()

    try:
        cursor.execute('''UPDATE compte SET Nom_Compte = ?, Nom_sur_site = ? ,Mot_passe = ? WHERE ID_Compte = ?''',
                       (nomApplication, nomSurSite, motPasse, idApplication))
        conn.commit()
        print("L'application a été mise à jour avec succès.")

        return True
    except Exception as e:
        raise Exception(f"Erreur : {str(e)}")
    finally:
        conn.close()


def supprimerApplication(idApplication):
    conn, cursor = se_connecter()

    try:
        cursor.execute('''DELETE FROM compte WHERE ID_Compte = ?''', (idApplication,))
        conn.commit()
        print("L'application a été supprimée avec succès.")
        return True
    except Exception as e:
        raise Exception(f"Erreur : {str(e)}")
    finally:
        conn.close()