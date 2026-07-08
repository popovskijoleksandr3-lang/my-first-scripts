import sqlite3
connection = sqlite3.connect('learning sql 6')
cursor=connection.cursor()
cursor.execute('''
create table if not exists project
(
name Text
price Text''')
products = [('guitar', "199 dollars"),
            ('electric guitar', "760 dollars")]
cursor.executemany('insert into project values (?,?)', products)
connection.commit()
cursor.execute('select * from project')
print(cursor.fetchall())
connection.close()