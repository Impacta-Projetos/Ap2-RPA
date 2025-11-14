import requests

url = "https://restcountries.com/v3.1/name/{pais}"

def buscar_pais(pais):
    response = requests.get(url.format(pais=pais))
    if response.status_code == 200:
        return response.json()
    return None
