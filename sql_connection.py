import sqlite3

class SQLiteConnection:

    def __init__(self):
        self.conn = sqlite3.connect('recipes.db')
    
    def cursor(self):
        c = self.conn.cursor()
        return c

    def commit(self):
        c = self.conn.commit()

    def close(self):
        self.conn.close()