import sqlite3
import os

# Garante que o diretório data existe
if not os.path.exists('data'):
    os.makedirs('data')

db = sqlite3.connect('data/paises.db')
cursor = db.cursor()