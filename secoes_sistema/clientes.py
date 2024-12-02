from funcionalidades.limpador_tela import limpar_terminal
from sistema_principal.config_db import criar_conexao
import msvcrt

def cadastrar_cliente(nome_cliente, endereco, email, telefone):
    limpar_terminal()
    conn = criar_conexao()
    try:
        cursor = conn.cursor()
        query = 'INSERT INTO cliente (nome_cliente, endereco, email, telefone) VALUES (%s, %s, %s, %s);'
        cursor.execute(query, (nome_cliente, endereco, email, telefone))
        conn.commit()
        print('Cliente cadastrado com sucesso!')
    except Exception as e:
        print(f'Erro ao cadastrar o cliente: {e}')
    finally:
        cursor.close()
        conn.close()

def verificar_cliente(nome_cliente):
    limpar_terminal()
    conn = criar_conexao()
    try:
        cursor = conn.cursor()
        query = 'SELECT * FROM cliente WHERE cliente like %s;'
        cursor.execute(query, (nome_cliente,))
        conn.commit()
    except Exception as e:
        print(f'Erro ao verificar o cliente: {e}')
    finally:
        cursor.close()
        conn.close()

def editar_cliente(nome_cliente, novo_nome):
    limpar_terminal()
    conn = criar_conexao()
    try:
        cursor = conn.cursor()
        query = 'UPDATE cliente SET nome_cliente = %s WHERE nome_cliente = %s;'
        cursor.execute(query, (novo_nome, nome_cliente))
        conn.commit()
        print('Cliente editado com sucesso!')
    except Exception as e:
        print(f'Erro ao editar o dados do cliente: {e}')
    finally:
        cursor.close()
        conn.close()
        msvcrt.getch()

def excluir_cliente(nome_cliente):
    limpar_terminal()
    conn = criar_conexao()
    try:
        cursor = conn.cursor()
        query = 'DELETE FROM cliente WHERE nome_cliente like %s;'
        cursor.execute(query, (nome_cliente,))
        print('Cliente excluido com sucesso!')
        conn.commit()    
    except Exception as e:
        print(f'Erro ao excluir os dados do cliente: {e}')
    finally:
        cursor.close()
        conn.close()
        msvcrt.getch()

def exibir_clientes():
    limpar_terminal()
    conn = criar_conexao()
    try:
        cursor = conn.cursor()
        query = 'SELECT * FROM cliente;'
        cursor.execute(query)
        exibicao_clientes = cursor.fetchall()
        print(exibicao_clientes)
        conn.commit()
    except Exception as e:
        print(f'Erro ao exibir os clientes: {e}')
    finally:
        cursor.close()
        conn.close()
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
            nome_cliente = input('Nome do cliente: ')
            endereco = input('Endereço do cliente: ')
            email = input('E-mail do cliente: ')
            telefone = input('Telefone do cliente: ')
            cadastrar_cliente(nome_cliente, endereco, email, telefone)
        elif escolha == '2':
            nome_cliente = input('Informe o nome do cliente: ')
            novo_nome = input('Informe o novo nome do cliente: ')
            editar_cliente(nome_cliente, novo_nome)
        elif escolha == '3':
            try:
                excluir_nome_cliente = input('Informe o nome do cliente a excluir: ')
                excluir_cliente(excluir_nome_cliente)
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