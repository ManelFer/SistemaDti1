import sqlite3


class DataBase():
    def __init__(self, name = "system.db"):
        self.name = name

    def conecta(self):
        self.connection = sqlite3.connect(self.name)

    def close_connection(self):
        if self.connection:
            try:
                self.connection.close()
            except sqlite3.Error as e:
                print(f"Erro ao fechar a conexão: {e}")

    def create_table(self, create_table_sql):
        try:
            cursor = self.connection.cursor()
            cursor.execute(create_table_sql)
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Erro na conexão: {e}")

    def create_table_users(self):
        create_table_sql = """
            CREATE TABLE IF NOT EXISTS users(
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                user TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL,
                acess TEXT NOT NULL
            );
        """
        self.create_table(create_table_sql)
    
    def create_table_cadastro(self):
        create_table_sql = """
            CREATE TABLE IF NOT EXISTS cadastro(
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                patrimonio TEXT UNIQUE NOT NULL,
                marca TEXT NOT NULL,
                modelo TEXT NOT NULL,
                quantidade TEXT NOT NULL
            );
        """
        self.create_table(create_table_sql)

if __name__ == "__main__":
    db = DataBase()
    db.conecta()
    db.create_table_users()
    db.create_table_cadastro()
    db.close_connection()