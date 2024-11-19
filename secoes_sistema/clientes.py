from funcionalidades.limpador_tela import limpar_terminal
import msvcrt

clientes = []

def cadastrar_cliente(nome, endereco, cpf):
    limpar_terminal()
    cliente = {
        'nome': nome,
        'endereco': endereco,
        'cpf': cpf
    }
    
    for cliente_existente in clientes:
        if cliente_existente['cpf'].lower() == cpf.lower():
            print(f'O cliente com o cpf "{cpf}" já está cadastrado.')
            msvcrt.getch()
            return
    
    clientes.append(cliente)
    print(f'Cliente {nome} foi cadastrado no sistema!')
    msvcrt.getch()

def editar_cliente(indice, novo_nome, novo_endereco, novo_cpf):
    limpar_terminal()
    if 0 <= indice <= len(clientes):
        clientes[indice]['nome'] = novo_nome
        clientes[indice]['endereco'] = novo_endereco
        clientes[indice]['cpf'] = novo_cpf
        print(f'Cliente na posição {indice} editado com sucesso!')
        msvcrt.getch()
    else:
        print('Índice Inválido!')
        msvcrt.getch()

def excluir_cliente(indice):
    limpar_terminal()
    if 0 <= indice < len(clientes):
        cliente_removido = clientes.pop(indice)
        print(f'Cliente "{cliente_removido["nome"]}" excluído com sucesso!')
        msvcrt.getch()
    else:
        print('Índice Inválido!')
        msvcrt.getch()

def exibir_clientes():
    limpar_terminal()
    if not clientes:
        print('Nenhum cliente cadastrado.')
        msvcrt.getch()
    else:
        print('Clientes cadastrados:')
        for i in range(len(clientes)):
            print(f'{i}. Nome: "{clientes[i]["nome"]}", Endereço: {clientes[i]["endereco"]}, CPF: {clientes[i]["cpf"]}"')
    msvcrt.getch() 

def menu_clientes():
    while True:
        limpar_terminal()
        print('Menu:')
        print('1 - Cadastrar Cliente')
        print('2 - Editar Cliente')
        print('3 - Excluir Cliente')
        print('4 - Exibir Clientes')
        print('5 - Voltar ao menu principal')
        escolha = input('Escolha uma opção (1-5): ')

        if escolha == '1':
            nome = input('Nome do cliente: ')
            endereco = input('Endereço do cliente: ')
            cpf = input('CPF do cliente: ')
            cadastrar_cliente(nome, endereco, cpf)
        elif escolha == '2':
            try:
                indice = int(input('Índice do cliente a editar: '))
                novo_nome = input('Novo nome do cliente: ')
                novo_endereco = input('Novo endereço do cliente: ')
                novo_cpf = input('Novo CPF do cliente: ')
                editar_cliente(indice, novo_nome, novo_endereco, novo_cpf)
            except ValueError:
                print('Por favor, insira um número válido para o índice.')
                msvcrt.getch()
        elif escolha == '3':
            try:
                indice = int(input('Índice do cliente a excluir: '))
                excluir_cliente(indice)
            except ValueError:
                print('Por favor, insira um número válido para o índice.')
                msvcrt.getch()
        elif escolha == '4':
            exibir_clientes()
        elif escolha == '5':
            print('Voltando ao menu principal.')
            break
        else:
            print('Opção inválida! Tente novamente.')