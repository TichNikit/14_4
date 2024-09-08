import sqlite3

def initiate_db():
    connection = sqlite3.connect('db.db')
    cursor = connection.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT, 
    price INTEGER NOT NULL
    )
    ''')

    cursor.execute('INSERT INTO Products (title, description, price) VALUES (?, ?, ?)', ('Витамин А', 'Витамин А необходим для '
                                                                                                'нормального зрения, '
                                            'функционирования иммунной системы и эмбрионального развития, для роста и '
                                            'целостности кожи, формирования костей', '100'))

    cursor.execute('INSERT INTO Products (title, description, price) VALUES (?, ?, ?)', ('Витамин B', 'Витамин B участвует в '
                                                                                                'обмене веществ и '
                                            'производстве энергии', '200'))

    cursor.execute('INSERT INTO Products (title, description, price) VALUES (?, ?, ?)', ('Витамин C', 'Витамин С участвует в '
                                                                                                'кроветворении, регулирует '
                                                                                                'свертываемость крови и '
                                                                                                'проницаемость капилляров',
                                                                                   '300'))

    cursor.execute('INSERT INTO Products (title, description, price) VALUES (?, ?, ?)', ('Витамин D', 'Витамин D помогает '
                                                                                                'организму усваивать кальций '
                                       'и фосфор, которые необходимы для роста костей', '400'))

    connection.commit()
    connection.close()



def get_all_products():
    connection = sqlite3.connect('db.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Products')
    all = cursor.fetchall()
    return all



