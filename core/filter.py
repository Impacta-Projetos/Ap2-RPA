from api import api

def filtrar_dados(pais):
    dados = api.buscar_pais(pais)
    if dados:
        # Se retornar múltiplos países, tenta encontrar o mais relevante
        pais_info = None
        pais_lower = pais.lower()
        
        # Procura por correspondência exata no nome comum ou oficial
        for p in dados:
            nome_comum = p.get('name', {}).get('common', '').lower()
            nome_oficial = p.get('name', {}).get('official', '').lower()
            
            # Verifica se o nome buscado está contido no nome do país
            # Prioriza correspondências exatas ou que começam com o termo buscado
            if (pais_lower == nome_comum or pais_lower == nome_oficial or
                nome_comum.startswith(pais_lower) or nome_oficial.startswith(pais_lower)):
                pais_info = p
                break
        
        # Se não encontrou uma correspondência perfeita, pega o primeiro
        if not pais_info:
            pais_info = dados[0]
        
        pais_data = {
            'nome_comum': pais_info.get('name', {}).get('common', ''),
            'nome_oficial': pais_info.get('name', {}).get('official', ''),
            'capital': pais_info.get('capital', [''])[0],
            'continente': pais_info.get('continents', [''])[0],
            'regiao': pais_info.get('region', ''),
            'subregiao': pais_info.get('subregion', ''),
            'populacao': pais_info.get('population', 0),
            'area': pais_info.get('area', 0.0),
            'moeda_nome': list(pais_info.get('currencies', {}).values())[0].get('name', '') if pais_info.get('currencies') else '',
            'moeda_simbolo': list(pais_info.get('currencies', {}).values())[0].get('symbol', '') if pais_info.get('currencies') else '',
            'idioma_principal': list(pais_info.get('languages', {}).values())[0] if pais_info.get('languages') else '',
            'fuso_horario': pais_info.get('timezones', [''])[0],
            'bandeira_url': pais_info.get('flags', {}).get('png', '')
        }
        return pais_data
    
    print(f"✗ Não foi possível obter dados para '{pais}'")
    return None