from . import db, cursor

cursor.execute('''
    CREATE TABLE IF NOT EXISTS paises(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
               nome_comum TEXT,
               nome_oficial TEXT,
               capital TEXT,
               continente TEXT,
               regiao TEXT,
               subregiao TEXT,
               populacao INTEGER,
               area REAL,
               moeda_nome TEXT,
               moeda_simbolo TEXT,
               idioma_principal TEXT,
               fuso_horario TEXT,
               bandeira_url TEXT)
''')

db.commit()