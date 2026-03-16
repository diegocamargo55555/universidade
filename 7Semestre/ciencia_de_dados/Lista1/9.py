class Produto:
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque
    
    def vender(self):
        self.estoque = self.estoque - 1
        
    def repor(self, novos_itens):
        self.estoque = self.estoque + novos_itens
    
    def exibir(self):
        print("nome",self.nome)
        print("preco",self.preco)
        print("estoque",self.estoque)
        

agua = Produto("agua", 1.99, 99)
agua.vender()
agua.repor(5)
agua.exibir()