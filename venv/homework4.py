import sqlite3

class UserDB:
    def __init__(self, db_path = "users.db"):
        self.connect = sqlite3.connect(db_path)
        self.cursor = self.connect.cursor()
        self.create_table()
    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS users(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER,
                email TEXT UNIQUE)
                """)
    def add_book(self, user):
        self.cursor.execute("INSERT INTO users (name, age, email) VALUES (?,?,?)", (user.name, user.age, user.email))
        self.connection.commit()

    def get_all_users(self):
        self.cursor.execute("SELECT * FROM users")
        x = self.cursor.fetchall()
        print(x)