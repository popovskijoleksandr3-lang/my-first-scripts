import sqlite3
connection = sqlite3.connect('Learning SQL 2')
cursor=connection.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS learning (
        name TEXT,
        price TEXT
    )
''')
products =[('Cola', '3 dollars'),
          ('Fanta', '3.45 dollars'),
          ('Sprite', '4 dollars')
]
cursor.executemany("Insert into learning (name, price) values (?, ?)", products)
connection.commit()
cursor.execute("SELECT * FROM learning")
print(cursor.fetchall())
connection.close()

