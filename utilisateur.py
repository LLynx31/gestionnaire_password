from connectDB_ import se_connecter
import bcrypt

def ajouter_utilisateur(nom, prenom, email, mot_passe, numero_tel):
    conn, cursor = se_connecter()

    try:
        cursor.execute('''SELECT * FROM utilisateur WHERE Adresse_mail = ? OR Numero_tel = ?''', (email, numero_tel))
        result = cursor.fetchone()

        if result:
            raise Exception("L'adresse email ou le numéro de téléphone existe déjà.")

        mot_passe_hash = bcrypt.hashpw(mot_passe.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

        cursor.execute(
            '''INSERT INTO utilisateur(Nom_utilisateur, Prenom_utilisateur, Adresse_mail, Mot_passe, Numero_tel) VALUES(?,?,?,?,?)''',
            (nom, prenom, email, mot_passe_hash, numero_tel))
        conn.commit()

        cursor.execute('''SELECT * FROM utilisateur WHERE Adresse_mail = ?''', (email,))
        utilisateur_ajoute = cursor.fetchone()

        print("L'utilisateur a été enregistré avec succès.")
        return utilisateur_ajoute
    except Exception as e:
        raise Exception(f"Erreur : {str(e)}")
    finally:
        conn.close()


def lire_utilisateur(id_utilisateur):
    conn, cursor = se_connecter()

    try:
        cursor.execute('''SELECT * FROM utilisateur WHERE ID_utilisateur = ?''', (id_utilisateur,))
        utilisateur = cursor.fetchone()
        return utilisateur
    except Exception as e:
        raise Exception(f"Erreur : {str(e)}")
    finally:
        conn.close()

def mettre_a_jour_utilisateur(id_utilisateur, nom, prenom, mot_passe, newPassword=None):
    conn, cursor = se_connecter()

    try:
        cursor.execute('''SELECT Mot_passe FROM utilisateur WHERE ID_utilisateur = ?''', (id_utilisateur,))
        utilisateur = cursor.fetchone()

        if not utilisateur:
            raise Exception("Utilisateur non trouvé.")

        mot_passe_actuel = utilisateur[0]


        if not bcrypt.checkpw(mot_passe.encode('utf-8'), mot_passe_actuel.encode('utf-8')):
            raise Exception("Mot de passe incorrect.")

        if newPassword:
            newPassword_hash = bcrypt.hashpw(newPassword.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        else:
            newPassword_hash = mot_passe_actuel

        cursor.execute(
            '''UPDATE utilisateur SET Nom_utilisateur = ?, Prenom_utilisateur = ?, Mot_passe = ? WHERE ID_utilisateur = ?''',
            (nom, prenom, newPassword_hash, id_utilisateur))
        conn.commit()

        print("L'utilisateur a été mis à jour avec succès.")
        return True
    except Exception as e:
        raise Exception(f"Erreur : {str(e)}")
    finally:
        conn.close()


def supprimer_utilisateur(id_utilisateur):
    conn, cursor = se_connecter()

    try:
        cursor.execute('''DELETE FROM utilisateur WHERE ID_utlisateur = ?''', (id_utilisateur,))
        conn.commit()
        print("L'utilisateur a été supprimé avec succès.")
        return True
    except Exception as e:
        raise Exception(f"Une erreur est survenue : {str(e)}")
    finally:
        conn.close()


def seConnecter(eMail, motPasse):
    conn, cursor = se_connecter()

    try:
        cursor.execute('''SELECT * FROM utilisateur WHERE Adresse_mail = ?''', (eMail,))
        utilisateur = cursor.fetchone()

        if utilisateur:
            mot_passe_hash = utilisateur[4]

            if bcrypt.checkpw(motPasse.encode('utf-8'), mot_passe_hash.encode('utf-8')):
                print("Connexion réussie.")
                return utilisateur
            else:
                raise Exception("Nom d'utilisateur ou mot de passe incorrect.")
        else:
            raise Exception("Nom d'utilisateur ou mot de passe incorrect.")
    except Exception as e:
        raise Exception(f"Erreur : {str(e)}")
    finally:
        conn.close()


#seConnecter("christian.sagoe119@gmail.com","12345678")