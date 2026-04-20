import mysql.connector
import json
from models.salle import Salle

class DataSalle:

    def get_connection(self):
        with open("Data/config.json", "r") as f:
            config = json.load(f)
        connexion = mysql.connector.connect(
            host=config["host"],
            user=config["user"],
            password=config["password"],
            database=config["database"]
        )
        return connexion

    def insert_salle(self, salle):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO salle VALUES (%s, %s, %s, %s)",
                       (salle.code, salle.description, salle.categorie, salle.capacite))
        conn.commit()
        conn.close()

    def update_salle(self, salle):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE salle SET description=%s, categorie=%s, capacite=%s WHERE code=%s",
                       (salle.description, salle.categorie, salle.capacite, salle.code))
        conn.commit()
        conn.close()

    def delete_salle(self, code):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM salle WHERE code=%s", (code,))
        conn.commit()
        conn.close()

    def get_salle(self, code):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM salle WHERE code=%s", (code,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return Salle(row[0], row[1], row[2], row[3])
        return None

    def get_salles(self):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM salle")
        rows = cursor.fetchall()
        conn.close()
        salles = []
        for row in rows:
            salles.append(Salle(row[0], row[1], row[2], row[3]))
        return salles