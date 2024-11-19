from funcionalidades.limpador_tela import limpar_terminal
from sistema_principal.config_db import criar_conexao
import msvcrt

livros = []

def cadastrar_livro(titulo,genero,idioma,data_estreia,id_autor,id_editora):
    limpar_terminal()
    conn = criar_conexao()
    try:
        cursor = conn.cursor()
        query = 'INSERT INTO livro (titulo, genero, idioma, data_estreia, id_autor, id_editora) VALUES (%s, %s, %s, %s, %s, %s);'
        cursor.execute(query, (titulo, genero, idioma, data_estreia, id_autor, id_editora))
        conn.commit()
        print('Livro cadastrado com sucesso!')
    except Exception as e:
        print(f'Erro ao cadastrar o livro: {e}')
    finally:
        cursor.close()
        conn.close()

def verificar_livro(titulo):
    limpar_terminal()
    conn = criar_conexao()
    try:
        cursor = conn.cursor()
        query = 'SELECT * FROM livro WHERE titulo = %s;'
        cursor.execute(query, (titulo))
        conn.commit()
    except Exception as e:
        print(f'Erro ao buscar o livro: {e}')
    finally:
        cursor.close()
        conn.close()


def editar_livro(titulo, novo_titulo):
    limpar_terminal()
    conn = criar_conexao()
    titulo = input('Digite o titulo do livro que deseja editar: ')
    verificar_livro(titulo)
    try:
        cursor = conn.cursor()
        query = 'UPDATE livro SET titulo = %s WHERE titulo = %s;'
        cursor.execute(query, (titulo, novo_titulo))
        conn.commit()
        print('Livro editado com sucesso!')
    except Exception as e:
        print(f'Erro ao editar o livro: {e}')
    finally:
        cursor.close()
        conn.close()
        msvcrt.getch()

def excluir_livro(titulo):
    limpar_terminal()
    conn = criar_conexao()
    titulo = input('Digite o titulo do livro que deseja excluir: ')
    verificar_livro(titulo)
    try:
        cursor = conn.cursor()
        query = 'DELETE FROM livro WHERE titulo = %s;'
        cursor.execute(query, (titulo))
        conn.commit()
        print('Livro excluido com sucesso!')
    except Exception as e:
        print(f'Erro ao excluir o livro: {e}')
    finally:
        cursor.close()
        conn.close()
        msvcrt.getch()

def exibir_livros():
    limpar_terminal()
    conn = criar_conexao()
    try:
        cursor = conn.cursor()
        query = 'SELECT * FROM livro;'
        cursor.execute(query)
        conn.commit()
    except Exception as e:
        print(f'Erro ao exibir os livros: {e}')
    finally:
        cursor.close()
        conn.close()
    msvcrt.getch()

def menu_livro():
    while True:
        print('Menu:')
        print('1 - Cadastrar Livro')
        print('2 - Editar Livro')
        print('3 - Excluir Livro')
        print('4 - Exibir Livros')
        print('5 - Voltar ao menu principal')
        escolha = input('Escolha uma opção (1-5): ')

        if escolha == '1':
            titulo = input('Título do livro: ')
            genero = input('Gênero do livro: ')
            idioma = input('Idioma do livro: ')
            data_estreia = input('Data de Estreia do livro: ')
            id_autor = input('Id do Autor do livro: ')
            id_editora = input('Id da Editora do livro: ')
            cadastrar_livro(titulo,genero,idioma,data_estreia,id_autor,id_editora)
            msvcrt.getch()
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
            msvcrt.getch()
        elif escolha == '5':
            print('Voltando ao menu principal.')
            break
        else:
            print('Opção inválida! Tente novamente.')