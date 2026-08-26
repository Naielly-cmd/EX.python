class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def exibir(self):
        print(f"Nome: {self.nome}")
        print(f"Preço: {self.preco}" ) 
        
#listar produtos
produtos = []

def CadastrarProduto():
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
            print("Valor incorreto, tente novamente.")

def ListarProdutos():
    i = 1
    print("\nPRODUTOS CADASTRADOS")
    if len(produtos) == 0:
        print("Nenhum produto cadastrado.")
        return
    for produto in produtos:
        print(f"Produto: {i}")
        i += 1
        produto.exibir()

def ComprarProduto():
    print("\nCOMPRA DE PRODUTO")
    if len(produtos) == 0:
        print("Não existem produtos cadastrados.")
        return
    ListarProdutos()
    try:
        i = int(input("\nQual o índice do produto que deseja comprar: "))
        if i <= 0 or i > len(produtos):
            print("Produto não encontrado.")
            return
        qtd = int(input("Quantas unidades deseja comprar?: "))
        if qtd <= 0:
            print("A quantidade deve ser maior que zero.")
            return
        produto = produtos[i - 1]
        total = produto.preco * qtd

        print(f"\nDETALHES DA COMPRA\n Produto: {produto.nome} \n Preço unitário: R$ {produto.preco:.2f} \n Quantidade: {qtd} \n Total a pagar: R$ {total:.2f}")

        if total >= 100:
           print("\nParabéns! Sua compra atingiu o valor para desconto.")
        else:
            print("Sem desconto.")
    except ValueError:
        print("\nSua compra não possui desconto.")

def menu():
    while True:
        print("\nSISTEMA DE PRODUTOS")
        print("1 - Cadastrar produto")
        print("2 - Listar produtos")
        print("3 - Comprar produto")
        print("4 - Sair")
        
        try:
            opcao = int(input("Escolha uma opção: "))
            
            if opcao == 1:
                CadastrarProduto()
            elif opcao == 2:
                ListarProdutos()
            elif opcao == 3:
                ComprarProduto()
            elif opcao == 4:
                print("\nPrograma encerrado!")
                break
            else:
                print("Opção inválida. Escolha uma opção de 1 a 4.")
                
        except ValueError:
            print("Opção inválida. Escolha uma opção de 1 a 4.")
menu()
