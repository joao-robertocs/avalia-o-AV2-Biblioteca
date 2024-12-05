from secoes_sistema.clientes import exibir_clientes
from secoes_sistema.livros import exibir_livros
from funcionalidades.limpador_tela import limpar_terminal
from sistema_principal.config_db import criar_conexao
import msvcrt

livros_alugados = []

def aluguel_livro(data_aluguel, id_livro, id_cliente, data_prevista):
     limpar_terminal()
     conn = criar_conexao()
     try:
        cursor = conn.cursor()
        query = 'INSERT INTO aluguel (data_aluguel, id_livro, id_cliente, data_prevista) VALUES (%s, %s, %s, %s);'
        cursor.execute(query, (data_aluguel, id_livro, id_cliente, data_prevista))
        conn.commit()
        print('Aluguel realizado com sucesso!')
     except Exception as e:
        print(f'Erro ao realizar aluguel: {e}')
     finally:
        cursor.close()
        conn.close()
        

def livro_atrasado(id_livro):
    limpar_terminal()
    conn = criar_conexao()
    try:
        cursor = conn.cursor()
        query = 'UPDATE aluguel SET livro_atrasado = NOT livro_atrasado WHERE id_livro = %s;'
        cursor.execute(query, (id_livro,))
        conn.commit()
        print('O status do livro alugado foi atualizado para "ATRASADO".')
    except Exception as e:
        print(f'Erro ao atualizar o status do livro: {e}')
    finally:
        cursor.close()
        conn.close()
    msvcrt.getch()


def devolucao_livro(id_livro, id_cliente, data_devolucao):
    limpar_terminal()
    conn = criar_conexao()
    try:
        cursor = conn.cursor()
        query = 'INSERT INTO aluguel (id_livro, id_cliente, data_devolucao) VALUES (%s, %s, %s);'
        cursor.execute(query, (id_livro, id_cliente, data_devolucao))
        conn.commit()
        print('A data para devolução do livro foi informada!')
    except Exception as e:
        print(f'Erro ao informar a data para devolução do livro: {e}')
    finally:
        cursor.close()
        conn.close()

def exibir_alugados():
    limpar_terminal()
    conn = criar_conexao()
    try:
        cursor = conn.cursor()
        query = 'SELECT * FROM aluguel;'
        cursor.execute(query)
        exibicao_aluguel = cursor.fetchall()
        print(exibicao_aluguel)
        conn.commit()
    except Exception as e:
        print(f'Erro ao exibir os aluguéis: {e}')
    finally:
        cursor.close()
        conn.close()
    msvcrt.getch()


def menu_aluguel():
    while True:
        limpar_terminal()
        print('Menu Aluguel:')
        print('1 - Realizar Aluguel')
        print('2 - Atualizar Status do Livro Alugado')
        print('3 - Informar Devolução')
        print('4 - Exibir Livros Alugados')
        print('5 - Retornar ao Menu Principal')

        escolha = input('Digite a opção desejada: ')

        if escolha == '1':
            data_aluguel = input('Informe a data do aluguel: ')
            exibir_livros()
            id_livro = int(input('Informe o ID do livro que será alugado: '))
            limpar_terminal()
            exibir_clientes()
            id_cliente = int(input('Informe o ID do cliente que está alugando: '))
            limpar_terminal()
            data_prevista = input('Informe a data prevista para devolução do livro: ')
            aluguel_livro(data_aluguel, id_livro, id_cliente, data_prevista)
        elif escolha == '2':
            try:
                limpar_terminal()
                exibir_alugados()
                id_livro = input('Informe o ID do livro que está atrasado: ')
                livro_atrasado(id_livro)
            except ValueError:
                print('Informe um ID de livro.') 
        
        elif escolha == '3':
            try:
                limpar_terminal()
                exibir_alugados()
                id_livro = int(input('ID do livro que será devolvido: '))
                id_cliente = int(input('ID do cliente que está devolvendo livro: '))
                data_devolucao = input('Data que o cliente está devolvendo o livro: ')
                devolucao_livro(id_livro, id_cliente, data_devolucao)
            except ValueError:
                print('Por favor, insira um número válido para o ID.')
                msvcrt.getch()
        elif escolha == '4':
            exibir_alugados()
        elif escolha == '5':
            print('Voltando ao menu principal.')
            msvcrt.getch()
            break
        else:
            print('Opção inválida! Tente novamente.')
            msvcrt.getch()