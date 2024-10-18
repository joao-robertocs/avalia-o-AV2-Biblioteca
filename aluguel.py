from clientes import clientes
from clientes import exibir_clientes
from livros import livros
from livros import exibir_livros
from limpador_tela import limpar_terminal
import msvcrt

livros_alugados = []

def aluguel_livro(indice_livro, indice_cliente):
    limpar_terminal()
    if 0 <= indice_livro < len(livros) and 0 <= indice_cliente < len(clientes):
        if livros [indice_livro]['disponivel']:
            livros[indice_livro]['disponivel'] = False
            livro_alugado = {
                'livro': livros[indice_livro],
                'cliente': clientes[indice_cliente]
            }
            livros_alugados.append(livro_alugado)
            print(f'Livro "{livros[indice_livro]['titulo']}" alugado para {clientes[indice_cliente]['nome']} com sucesso!')
        else:
            print(f'O livro "{livros[indice_livro]['titulo']}" já foi alugado.')
    else: 
        print('Índice Inválido!')
    msvcrt.getch()

def devolucao_livro(indice):
    limpar_terminal()
    if 0 <= indice <= len(livros_alugados):
        livro_devolvido = livros_alugados.pop(indice)
        for livro in livros:
            if livro['titulo'] == livro_devolvido['livro']['titulo']:
                livro['disponivel'] = True
                break
        print(f'Livro "{livro_devolvido['livro']['titulo']}" devolvido por {livro_devolvido['cliente']['nome']} com sucesso!')
    else:
        print('Índice Inválido!')
    msvcrt.getch()

def exibir_alugados():
    limpar_terminal()
    if not livros_alugados:
        print('Nenhum livro alugado no momento.')
        msvcrt.getch()
    else: 
        print('Livros Alugados:')
        for i in range(len(livros_alugados)):
            livro = livros_alugados[i]
            print(f'{i}. Título: "{livro['livro']['titulo']}\nAutor: {livro['livro']['autor']}\nAlugado por: {livro['cliente']['nome']}')
        msvcrt.getch()
def menu_aluguel():
    while True:
        limpar_terminal()
        print('Menu Aluguel:')
        print('1 - Realizar Aluguel')
        print('2 - Realizar Devolução')
        print('3 - Exibir Livros Alugados')
        print('4 - Retornar ao Menu Principal')

        escolha = input('Digite a opção desejada: ')

        if escolha == '1':
            exibir_livros()
            indice_livro = int(input('Índice do livro a alugar: '))
            limpar_terminal()
            exibir_clientes()
            indice_cliente = int(input('Índice do cliente: '))
            limpar_terminal()
            aluguel_livro(indice_livro, indice_cliente)
        elif escolha == '2':
            limpar_terminal()
            exibir_alugados()
            indice = int(input('Índice do livro a devolver: '))
            devolucao_livro(indice)
        elif escolha == '3':
            exibir_alugados()
        elif escolha == '4':
            print('Voltando ao menu principal.')
            msvcrt.getch()
            break
        else:
            print('Opção inválida! Tente novamente.')
            msvcrt.getch()