import sqlite3


class Database:

    def __init__(self):
        try:
            self.sqlite_connection = sqlite3.connect('maplist')
            self.cursor = self.sqlite_connection.cursor()
        except sqlite3.Error as error:
            print("Ошибка при подключении к sqlite", error)

    def getUsers(self):
        self.cursor.execute("""SELECT * FROM users""")
        users = self.cursor.fetchall()
        return users

    def getPlaces(self):
        self.cursor.execute("""SELECT * FROM places""")
        places = self.cursor.fetchall()
        return places

    def getPlacesByUserId(self, id):
        self.cursor.execute("""SELECT * 
                                FROM places 
                                WHERE owner_id = ?""", id)
        places = self.cursor.fetchall()
        return places
