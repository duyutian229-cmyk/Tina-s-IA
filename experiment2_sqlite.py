import sqlite3

connection = sqlite3.connect("experiment2.db")
cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS test_orders (
        id INTEGER PRIMARY KEY,
        drink TEXT,
        nickname TEXT
    )
""")

cursor.execute(
    "INSERT INTO test_orders (drink, nickname) VALUES (?, ?)",
    ("latte", "Tina"),
)
connection.commit()


cursor.execute(
    "SELECT id, drink, nickname FROM test_orders WHERE id = ?",
    (cursor.lastrowid,),
)
print(cursor.fetchone())

connection.close()
