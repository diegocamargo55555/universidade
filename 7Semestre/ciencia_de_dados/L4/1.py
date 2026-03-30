import re
from collections import Counter

def contar_top_palavras(caminho_arquivo, top_n=10):
    with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
        texto = arquivo.read()
        
    texto = texto.lower()
    palavras = re.findall(r'\b[a-zà-ÿ]+\b', texto)
    contagem = Counter(palavras)
    return contagem.most_common(top_n)

txt = "a.txt" 

with open(txt, 'w', encoding='utf-8') as f:
    f.write("teste.")
    
top_10 = contar_top_palavras(txt)

print("As 10 palavras mais frequentes são:\n")
print(f"{'Palavra':<15} | {'Frequência'}")
print("-" * 30)
for palavra, frequencia in top_10:
    print(f"{palavra:<15} | {frequencia}")