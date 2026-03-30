import requests

def buscar_repositorios(topico, limite=5):
    print(f"Buscando repositórios sobre '{topico}' no GitHub...\n")
    
    url = "https://api.github.com/search/repositories"
    
    parametros = {
        'q': topico,
        'per_page': limite
    }
    
    headers = {
        'Accept': 'application/vnd.github.v3+json'
    }
    
    resposta = requests.get(url, params=parametros, headers=headers, timeout=10)
    resposta.raise_for_status()
    dados = resposta.json()
    repositorios = dados.get('items', [])
    
    if not repositorios:
        print("Nenhum repositório encontrado para este tópico.")
        return
        
    print("-" * 50)
    for i, repo in enumerate(repositorios, start=1):
        nome = repo.get('name', 'Nome não disponível')
        url_repo = repo.get('html_url', 'URL não disponível')
        
        print(f"{i}. {nome}")
        print(f"   URL: {url_repo}\n")

# --- Execução do Script ---
if __name__ == "__main__":
    buscar_repositorios("golang")