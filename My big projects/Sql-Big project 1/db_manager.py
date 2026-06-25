import sqlite3
def init_db():
    connection = sqlite3.connect('my_shop')
    cursor = connection.cursor()
    cursor.execute('''
    Create Table if not exists products (
    id Integer primary key autoincrement,
    name text not null,
    price real not null
    )
    ''')
    connection.commit()
    connection.close()
def add_product(name, price):
    connection = sqlite3.connect('my_shop')
    cursor = connection.cursor()
    cursor.execute("Insert into products (name, price) Values (?, ?)", (name, price))
    connection.commit()
    connection.close()
def get_all_products():
    connection = sqlite3.connect('my_shop')
    cursor=connection.cursor()
    cursor.execute("select * from products")
    products = cursor.fetchall()
    connection.close()
    return products
if __name__ == "__main__":
    init_db()
    add_product("Cola", 3.62)
    add_product("Fanta", 3.54)
    add_product("Pepsi", 3.40)
    add_product("Sprite", 3.35)
    add_product("Water", 1.50)
    print("Дані в базі:", get_all_products())

