import requests

def buscar_pais(pais):
    # Tenta primeiro pelo endpoint de tradução
    url_translation = f"https://restcountries.com/v3.1/translation/{pais}"
    response = requests.get(url_translation)
    
    if response.status_code == 200:
        return response.json()
    
    # Se falhar, tenta pelo endpoint de nome em inglês
    url_name = f"https://restcountries.com/v3.1/name/{pais}"
    response = requests.get(url_name)
    
    if response.status_code == 200:
        return response.json()
    
    return None
