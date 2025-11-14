def obter_paises():
    paises = []
    cont = 1
    while cont <= 3:
        pais = input(f'Digite o nome do {cont}º país: ').lower()
        paises.append(pais)
        cont += 1
    return paises
