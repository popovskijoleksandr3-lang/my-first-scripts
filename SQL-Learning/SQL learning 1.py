import sqlite3
connection = sqlite3.connect('learning sql')
cursor=connection.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS PRODUCT (
name Text,
price integer,
weight Text
)
''')
cursor.execute("Insert into PRODUCT (name, price, weight) values ('Cola', 3,'300 gram')")
connection.commit()
cursor.execute("SELECT * FROM PRODUCT")
print(cursor.fetchall())
connection.close()