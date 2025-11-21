import sqlite3

connect = sqlite3.connect('shop.db')
cursor = connect.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS shop(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    price INTEGER NOT NULL,
    category TEXT NOT NULL,
    in_stock INTEGER NOT NULL
    )
''')

connect.commit()

def create_user(name, price, category, in_stock):
    cursor.execute(
        'INSERT INTO shop(name, price, category, in_stock) VALUES (?, ?, ?, ?)',
        (name, price, category, in_stock)
    )
    connect.commit()
    print("товар добавлен")

#create_user('laptop', 32000, 'electronics', 50)
#create_user('mi phone', 15000, 'electronics', 100)
#create_user('watch', 8000, 'electronics', 75)
def read_user():
    cursor.execute('SELECT * FROM shop ')
    shop = cursor.fetchall()
    print(shop)
read_user()


def update_user(name,rowid):
    cursor.execute(
        'UPDATE shop SET name=? WHERE rowid=?',
        (name, rowid)
    )
    connect.commit()
    print(f"пользователь с id {rowid} обновлен")

#update_user("headphon", 3)

def delete_user(rowid):
    cursor.execute('DELETE FROM shop WHERE rowid=?', (rowid,) )
    connect.commit()
    print(f"пользователь с  id {rowid} удален")

#delete_user(3)
