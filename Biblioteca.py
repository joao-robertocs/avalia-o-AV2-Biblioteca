from limpador_tela import limpar_terminal
from acesso_sistema import acessar_sistema
from livros import menu_livro
from clientes import menu_clientes
from aluguel import menu_aluguel
import msvcrt

acessar_sistema()
while True:
    limpar_terminal()
    print('Menu Principal: ')
    print('1 - Gerenciar Livros')
    print('2 - Gerenciar Clientes')
    print('3 - Gerenciar Aluguel')
    print('4 - Fechar Sistema')

    opcao = int(input('Digite sua opção desejada: '))


    if opcao == 1:
        menu_livro()
    
    elif opcao == 2:
        menu_clientes()
    
    elif opcao == 3:
        menu_aluguel()

    elif opcao == 4:
        limpar_terminal()
        print('Sistema Encerrado, até a próxima!')
        break
    
    else:
        print('Opção Inválida!')
        msvcrt.getch()