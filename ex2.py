class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def exibir(self):
        print(f"Nome: {self.nome}")
        print(f"Preço: {self.preco}" ) 

produtos = []

def cadastrarProduto():
    print("\nCADASTRO DE PRODUTO")
    while True:
        try:
            nome = input("Digite o nome do produto: ")
            if nome == "":
                print("O nome do produto não pode ficar vazio.")
                continue
            preco = float(input("Digite o preço do produto: R$ "))
            if preco <= 0:
                print("O preço deve ser maior que zero.")
                continue
            produto = Produto(nome, preco)
            produtos.append(produto)
            print("Produto cadastrado")
            return
        except ValueError:
            print("Erro: valor incorreto, tente novamente.")

