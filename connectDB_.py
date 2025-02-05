import sqlite3

def se_connecter():
    conn = sqlite3.connect("PROJET_PYTHON.db")
    cursor=conn.cursor()
    return conn,cursor

