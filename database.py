import sqlite3


class Database:

    def __init__(self):

        import sqlite3

        try:
            self.sqlite_connection = sqlite3.connect('sqlite_python.db')
            sqlite_create_table_query = '''CREATE TABLE users (
                                        id INTEGER PRIMARY KEY ,
                                        name TEXT NOT NULL,
                                        email text NOT NULL UNIQUE);'''

            self.cursor = self.sqlite_connection.cursor()
            print("База данных подключена к SQLite")
            self.cursor.execute(sqlite_create_table_query)
            self.sqlite_connection.commit()
            print("Таблица SQLite создана")

        except sqlite3.Error as error:
            print("Ошибка при подключении к sqlite", error)
        finally:
            if (self.sqlite_connection):
                print("Соединение с SQLite закрыто")

    def addData(self):
        self.cursor.execute("""INSERT INTO users ('name', 'email') VALUES ('Leha', 'leha@yandex.ru')""")
        self.cursor.execute("""INSERT INTO users ('name', 'email') VALUES ('sany1', 'sany1@yandex.ru')""")
        self.cursor.execute("""INSERT INTO users ('name', 'email') VALUES ('sany2', 'sany2@yandex.ru')""")
        self.sqlite_connection.commit()

    def getData(self):
        self.cursor.execute("""SELECT * FROM users""")
        rows = self.cursor.fetchall()
        print(rows)