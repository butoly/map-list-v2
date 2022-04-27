import sqlite3


class Database:

    def __init__(self):

        import sqlite3

        try:
            self.sqlite_connection = sqlite3.connect('sqlite_python.db')
            sqlite_create_table_users = '''CREATE TABLE users (
                                        id INTEGER PRIMARY KEY ,
                                        name TEXT NOT NULL UNIQUE,
                                        email TEXT NOT NULL UNIQUE,
                                        picture TEXT);'''

            sqlite_create_table_place = '''CREATE TABLE place (
                                                    id INTEGER PRIMARY KEY ,
                                                    userid INTEGER NOT NULL,
                                                    description TEXT NOT NULL,
                                                    name NVARCHAR NOT NULL,
                                                    picture text);'''

            self.cursor = self.sqlite_connection.cursor()
            self.cursor.execute(sqlite_create_table_users)
            self.cursor.execute(sqlite_create_table_place)
            self.sqlite_connection.commit()

        except sqlite3.Error as error:
            print("Ошибка при подключении к sqlite", error)
        finally:
            if (self.sqlite_connection):
                print("Соединение с SQLite закрыто")

    def addData(self):
        self.cursor.execute("""INSERT INTO users ('name', 'email') VALUES ('Leha', 'leha@yandex.ru')""")
        self.cursor.execute("""INSERT INTO users ('name', 'email') VALUES ('sany1', 'sany1@yandex.ru')""")
        self.cursor.execute("""INSERT INTO users ('name', 'email') VALUES ('sany2', 'sany2@yandex.ru')""")

        self.cursor.execute("""INSERT INTO place ('userid', 'description', 'name') VALUES ('1', 'Прикольное место, мне понравилось', 'We Cideria')""")
        self.cursor.execute("""INSERT INTO place ('userid', 'description', 'name') VALUES ('1', 'не особо зашло', 'Killfish')""")
        self.cursor.execute("""INSERT INTO place ('userid', 'description', 'name') VALUES ('2', 'кек вейт чебурек', 'Acha-chacha')""")

        self.sqlite_connection.commit()

    def getData(self):
        self.cursor.execute("""SELECT * FROM users""")
        rows = self.cursor.fetchall()
        print(rows)
        self.cursor.execute("""SELECT * FROM place""")
        rows = self.cursor.fetchall()
        print(rows)