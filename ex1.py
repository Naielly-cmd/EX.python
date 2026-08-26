class Produto:
    def __init__ (self,nome, codigo, qtd, preco_unitario):
       self.nome = nome
       self.codigo = codigo
       self.qtd = qtd
       self.preco_unitario = preco_unitario
       
    def mostrar(self):
        print(f"Nome: {self.nome}")
        print(f"Codigo: {self.codigo}" ) 
        print(f"Quantidade: {self.qtd}")
        print(f"Preço unitário: {self.preco_unitario}")
        
P1 = Produto("smartphone", 50.789065, 1, 7000.00)
P1.mostrar()