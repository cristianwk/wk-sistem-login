import sqlite3

conn = sqlite3.connect('UsersData.db')

c = conn.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS Users(
    Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL,
    Email TEXT NOT NULL UNIQUE,
    User INTEGER NOT NULL,
    Password TEXT NOT NULL          
)
""")

print("Conectado ao Banco de Dados")

#c.execute("""
#INSERT INTO Users (Id, Name, Email
 #         """)