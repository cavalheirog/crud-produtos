# CRUD de Produtos
# Autor: Gabriel Cavalheiro
# Descrição: Sistema simples de cadastro de produtos via terminal


produtos = [] 

def listarProdutos():
    if(len(produtos) == 0):
        print('Não tem produtos cadastrados')
    for p in produtos:
        print(f'{p['nome']} ... R$ {p['preco']:.2f}')
        
        
def adicionarProduto(produto):
    produtos.append(produto)
    return True


def buscarProduto(produtoNome):
    for i in range(len(produtos)):
        if produtos[i]['nome'] == produtoNome:
            return i
    return None


def atualizarProduto(indice, produto):
    produtos[indice] = produto
    return True


def removerProduto(indice):
    produtos.pop(indice)
    return True



opcao = None
while(opcao != '0'):
    print()
    print('========================================')
    print('               MENU')
    print('========================================')
    print('1 - Listar Produtos')
    print('2 - Adicionar Produto')
    print('3 - Buscar Produto')
    print('4 - Atualizar Produto')
    print('5 - Remover Produto')
    print('0 - Sair')
    print('========================================')
    
    if(opcao == '1'): 
        print()
        print('LISTA DE PRODUTOS ======================')
        listarProdutos()
    
    elif(opcao == '2'): 
        print()
        print('ADICIONAR DE PRODUTOS ==================')
        nome = input('Nome: ')
        preco = float(input('Preço: '))
        adicionarProduto({'nome': nome, 'preco': preco})
        print()
        print('LISTA DE PRODUTOS ======================')
        listarProdutos()
    
    elif(opcao == '3'): 
         print('BUSCAR PRODUTO =========================')
         nome = input('Nome do produto que deseja buscar:')
         indice = buscarProduto(nome)

         if indice != None:
            p = produtos[indice]
            print(f"{p['nome']} ... R$ {p['preco']:.2f}")                               
         else:
            print('Produto não encontrado')
                
    elif(opcao == '4'): 
         print('ATUALIZAR PRODUTO ======================')
         nome = input('Nome do produto que deseja atualizar:')
         indice = buscarProduto(nome)

         if indice != None:
             nome_atualizado = input('Novo nome: ')
             preco_atualizado = float(input('Novo preço: '))

             atualizarProduto(indice, {'nome': nome_atualizado, 'preco': preco_atualizado})
             print('Produto atualizado com sucesso')
         else:
            print('Produto não encontrado')
    
    elif(opcao == '5'): 
         print('REMOVER PRODUTO ========================')
         nome = input('Nome do produto que deseja remover: ')
         indice = buscarProduto(nome)

         if indice != None:
            removerProduto(indice)
            print('Produto removido com sucesso')
         else: 
            print('produto não encontrado')

         
    
    elif(opcao != None): 
        print('Opção não existe')    
    
    print()
    opcao = input('Opção desejada:')