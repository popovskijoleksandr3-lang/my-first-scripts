import sqlite3
connection = sqlite3.connect('learning sql 5')
cursor=connection.cursor()
cursor.execute('''
create table if not exists project
(
name Text,
service Text,
price integer )
''')
workers = [('Andrew','Window washing', 6.20),
           ('Alexei','Equipment maintenance', 4.20)]
cursor.executemany("insert into project values (?, ?, ?)", workers)
connection.commit()
cursor.execute('select * from project')
print(cursor.fetchall())
connection.close()