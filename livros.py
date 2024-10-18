from limpador_tela import limpar_terminal
import msvcrt

livros = []

def cadastrar_livro(titulo,autor):
    limpar_terminal()
    livro = {
        'titulo': titulo,
        'autor' : autor
    }

    for livro_existente in livros:
        if livro_existente['titulo'].lower() == titulo.lower():
            print(f'O livro "{titulo}" já está cadastrado.')
            msvcrt.getch()
            return

    livros.append(livro)
    print(f'Livro "{titulo}" cadastrado com sucesso!')
    msvcrt.getch()

def editar_livro(indice, novo_titulo, novo_autor):
    limpar_terminal()
    if 0 <= indice < len(livros):
        livros[indice]['titulo'] = novo_titulo
        livros[indice]['autor'] = novo_autor
        print(f'Livro na posição {indice} editado com sucesso!')
        msvcrt.getch()
    else:
        print('Índice Inválido!')
        msvcrt.getch()

def excluir_livro(indice):
    limpar_terminal()
    if 0 <= indice < len(livros):
        livro_removido = livros.pop(indice)
        print(f'Livro "{livro_removido["titulo"]}" excluído com sucesso!')
        msvcrt.getch()
    else:
        print('Índice Inválido!')
        msvcrt.getch()

def exibir_livros():
    limpar_terminal()
    if not livros:
        print('Nenhum livro cadastrado.')
        msvcrt.getch()
    else:
        print('Livros cadastrados:')
        for i in range(len(livros)):
            print(f'{i}. Título: "{livros[i]["titulo"]}", Autor: {livros[i]["autor"]}"')
    msvcrt.getch()

def menu_livro():
    while True:
        limpar_terminal()
        print('Menu:')
        print('1 - Cadastrar Livro')
        print('2 - Editar Livro')
        print('3 - Excluir Livro')
        print('4 - Exibir Livros')
        print('5 - Voltar ao menu principal')
        escolha = input('Escolha uma opção (1-5): ')

        if escolha == '1':
            titulo = input('Título do livro: ')
            autor = input('Autor do livro: ')
            cadastrar_livro(titulo, autor)
        elif escolha == '2':
            try:
                indice = int(input('Índice do livro a editar: '))
                novo_titulo = input('Novo título do livro: ')
                novo_autor = input('Novo autor do livro: ')
                editar_livro(indice, novo_titulo, novo_autor)
            except ValueError:
                print('Por favor, insira um número válido para o índice.')
                msvcrt.getch()
        elif escolha == '3':
            try:
                indice = int(input('Índice do livro a excluir: '))
                excluir_livro(indice)
            except ValueError:
                print('Por favor, insira um número válido para o índice.')
                msvcrt.getch()
        elif escolha == '4':
            exibir_livros()
        elif escolha == '5':
            print('Voltando ao menu principal.')
            break
        else:
            print('Opção inválida! Tente novamente.')