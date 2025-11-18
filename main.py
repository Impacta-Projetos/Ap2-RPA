from models import paises
from core import input, insert, filter

def main():
    paises_lista = input.obter_paises()
    
    for pais in paises_lista:
        pais_data = filter.filtrar_dados(pais)
        if pais_data:
            insert.insert_pais(pais_data, pais)
    
    insert.fechar_conexao()

if __name__ == '__main__':
    main()