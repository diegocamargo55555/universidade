import requests
from bs4 import BeautifulSoup


url = "https://valete.org.br/"
#url = "https://daseintropical.substack.com/p/bronze-age-mindset-traducao"
print(f"Iniciando: {url}\n")

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

resposta = requests.get(url, headers=headers, timeout=15)
resposta.raise_for_status() 

soup = BeautifulSoup(resposta.text, 'html.parser')
tags_h2 = soup.find_all('h2')

if not tags_h2:
    print("Nenhuma tag <h2> foi encontrada nesta página.")

print("Títulos <h2> encontrados:")
print("-" * 40)

for indice, tag in enumerate(tags_h2, start=1):
    texto = tag.get_text(strip=True)
    
    if texto:
        print(f"{indice}. {texto}")
            

