import sqlite3
connect = sqlite3.connect('library.db')
cursor = connect.cursor()


def create_table():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS library (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
        )
    ''')
    #connect.commit()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        author TEXT NOT NULL,
        year INTEGER NOT NULL,
        genre TEXT NOT NULL,
        availability INTEGER NOT NULL,
        library_id INTEGER NOT NULL,
        FOREIGN KEY (library_id) REFERENCES library(id)
        )
    ''')

    connect.commit()

create_table()


def insert_test_db():
    cursor.execute (
        'INSERT INTO library (name) VALUES (?) ',

                  #('Имени Скрябина',),
                   #('Книжный червь',),
                  ('Кожаная обложка',)
    #
     )


    cursor.execute (
        'INSERT INTO books (title, author, year, genre, availability,library_id) VALUES (?,?,?,?,?,?)',
        #('Основы экономики' , 'Юрий.А', 1999, 'наука', 12 ,1)
                    # ('История пирамид', 'Афанасев.З', 2012, 'наука', 18 ,1 ),
                    #('Маленький принц', 'Томас.Ш', 2008, 'сказки', 10 ,2 ),
                     #('Буратино' , 'Тоби.М', 1990, 'сказки', 15 ,2 ),
                    # ('Гарри Потер', 'Роан.Р', 2010, 'фантастика', 18 ,3 ),
                    # ( 'Ведьмак', 'Андрей.С', 2008, 'фантастика', 15 ,3 ),
     )

    connect.commit()
    #print('данные сохранены')
def get_info():
    cursor.execute ('''
    SELECT library.name, books.title, books.author, books.year, books.genre, books.availability
    FROM library INNER JOIN books ON library.id = books.library_id
    ''')
    bb = cursor.fetchall()
    print(bb)

#get_info()

def hi_availability():
    cursor.execute ('''
    SELECT library.name, MAX(books.availability) FROM library INNER JOIN books ON library.id = books.library_id
    ''')
    bb = cursor.fetchall()
    print(bb)
#hi_availability()
