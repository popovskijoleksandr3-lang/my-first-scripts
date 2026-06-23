import sqlite3
connection = sqlite3.connect('learning sql 343')
cursor=connection.cursor()
cursor.execute('''
create table if not exists learning
(
name Text,
price Real )
''')
products = [('Cola',3.12),
            ('Fanta',3.76)]
cursor.executemany("insert into learning (name, price) values (?, ?)", products)
connection.commit()
cursor.execute("Select * From learning")
print(cursor.fetchall())
cursor.execute("select * from learning")
print(cursor.fetchall())
connection.close()
