'''
Dev: Kenier G.
Script description: Configure SQLite3 data base
'''

import sqlite3

con = sqlite3.connect('school.db')

cur = con.cursor()

    

#Create users table
array_querys = [
    '''
    CREATE TABLE IF NOT EXISTS countries (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        abrev TEXT NOT NULL,
        descrip TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT (datetime('now','localtime')),
        updated_at TIMESTAMP NULL,
        deleted_at TIMESTAMP NULL
    );
    ''',
    '''
    CREATE TABLE IF NOT EXISTS departaments (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        abrev TEXT NOT NULL,
        descrip TEXT NOT NULL,
        id_country INTEGER NOT NULL,
        created_at TIMESTAMP DEFAULT (datetime('now','localtime')),
        updated_at TIMESTAMP NULL,
        deleted_at TIMESTAMP NULL,
        FOREIGN KEY (id_country) REFERENCES countries(id)
    );
    ''',
    '''
    CREATE TABLE IF NOT EXISTS cities (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        abrev TEXT NOT NULL,
        descrip TEXT NOT NULL,
        id_dep INTEGER NOT NULL,
        created_at TIMESTAMP DEFAULT (datetime('now','localtime')),
        updated_at TIMESTAMP NULL,
        deleted_at TIMESTAMP NULL,
        FOREIGN KEY (id_dep) REFERENCES departaments(id)
    );
    ''',
    '''
    CREATE TABLE IF NOT EXISTS identification_types (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        abrev TEXT NOT NULL,
        descrip TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT (datetime('now','localtime')),
        updated_at TIMESTAMP NULL,
        deleted_at TIMESTAMP NULL
    );
    ''',
    '''
    CREATE TABLE IF NOT EXISTS persons (
        id INTEGER PRIMARY KEY,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        id_ident_type INTEGER NOT NULL,
        ident_number TEXT NOT NULL,
        id_exp_city INTEGER NOT NULL,
        address TEXT NOT NULL,
        mobile TEXT NOT NULL,
        id_user INTEGER NOT NULL,
        created_at TIMESTAMP DEFAULT (datetime('now','localtime')),
        updated_at TIMESTAMP NULL,
        deleted_at TIMESTAMP NULL,
        FOREIGN KEY (id_ident_type) REFERENCES identification_types(id)
    );
    ''',
    '''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        code TEXT NOT NULL,
        id_person TEXT NOT NULL,
        status BOOLEAN NULL,
        created_at TIMESTAMP DEFAULT (datetime('now','localtime')),
        updated_at TIMESTAMP NULL,
        deleted_at TIMESTAMP NULL,
        FOREIGN KEY (id_person) REFERENCES persons(id)

    );
    ''',
    '''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        email TEXT NOT NULL,
        password TEXT NOT NULL,
        status BOOLEAN NULL,
        created_at TIMESTAMP DEFAULT (datetime('now','localtime')),
        updated_at TIMESTAMP NULL,
        deleted_at TIMESTAMP NULL,
        FOREIGN KEY (id) REFERENCES persons(id)
    );
    ''',
]

#Execute SQL (Query)
for query in array_querys :
    cur.execute(query)
con.commit()

#Save changes in database => Push to database

#print("::: Database market has been created :::")

#Close connection
#con.close()