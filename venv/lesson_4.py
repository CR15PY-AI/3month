# таблица - relation, Строки - tuple, столбцы - Attribute

# SQL - Structured Query language 

# DDL - Data Definition Language (CREATE, ALTER, DROP, TRUNCATE) - Определение и изменение структуры
# DML - Data MAnipulation Language (SELECT, INSERT, UPDATE, DELETE, MERGE) - Чтение и изменение данных
# DCL - Data Control Language (GRANT, REVOKE) - Управление правами доступа
# TCL - Transaction Control Language (BEGIN, COMMIT , ROLLBACK, SAVEPOINT) - Управление транзакциями (Группами операций)




# import sqlite3
# conn = sqlite3.connect("database.db")
# cursor = conn.cursor()

# cursor.execute("""
#     CREATE TABLE IF NOT EXISTS users(
#         id INTEGER PRIMARE KEY,
#         name TXT NOT NULL,
#         age INTEGER
#     )
# """)
# conn.commit()

# conn.close()




import sqlite3

def init_db(db_path = "my_database.db"):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER
        )
    """)

    conn.commit()
    conn.close()

def add_user(name, age, db_path = "my_database.db"):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name, age) VALUES (?,?)", (name, age))
    conn.commit()
    conn.close()

def get_all_users(db_path = "my_database.db"):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, age FROM users")
    rows = cursor.fetchall()
    conn.close()
    return rows

if __name__ == "__main__":
    init_db()
    add_user("Jonh", 25)
    add_user("Xander" , 20)

    users = get_all_users()
    for uid, name , age in users:
        print(uid, name, age)