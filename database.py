import sqlite3

# Skapa och anslut till database.db
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Skapa tabellen för användare om den inte redan finns
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE
)
""")

# Spara ändringarna och stäng anslutningen
conn.commit()
conn.close()
