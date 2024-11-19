from sistema_principal.config_db import criar_conexao
from funcionalidades.limpador_tela import limpar_terminal
from sistema_principal.acesso_sistema import acessar_sistema
from secoes_sistema.livros import menu_livro
from secoes_sistema.clientes import menu_clientes
from secoes_sistema.aluguel import menu_aluguel
import msvcrt

conn = criar_conexao()

if conn:
    conn.close()

acessar_sistema()
while True:
    limpar_terminal()
    print("""Menu Principal:
    1 - Gerenciar Livros
    2 - Gerenciar Clientes
    3 - Gerenciar Aluguel
    4 - Fechar Sistema""")

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