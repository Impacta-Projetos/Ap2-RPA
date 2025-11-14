from models import db, cursor

def insert_pais(pais_data, nome_buscado):
    # Verifica se o país já existe
    cursor.execute('SELECT id FROM paises WHERE nome_comum = ?', (pais_data['nome_comum'],))
    pais_existente = cursor.fetchone()
    
    if pais_existente:
        print(f"⚠ País '{nome_buscado}' já existe no banco de dados!")
        return False  # País já existe, não insere
    
    # Se não existe, insere o país
    cursor.execute('''
        INSERT INTO paises (
            nome_comum, nome_oficial, capital, continente, regiao,
            subregiao, populacao, area, moeda_nome, moeda_simbolo,
            idioma_principal, fuso_horario, bandeira_url)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', (
            pais_data['nome_comum'], pais_data['nome_oficial'], pais_data['capital'],
            pais_data['continente'], pais_data['regiao'], pais_data['subregiao'],
            pais_data['populacao'], pais_data['area'], pais_data['moeda_nome'],
            pais_data['moeda_simbolo'], pais_data['idioma_principal'],
            pais_data['fuso_horario'], pais_data['bandeira_url']
        ))
    db.commit()
    print(f"✓ País '{nome_buscado}' inserido com sucesso!")
    return True  # País inserido com sucesso

def fechar_conexao():
    db.close()