from sistema_principal.config_db import criar_conexao
from funcionalidades.limpador_tela import limpar_terminal
from sistema_principal.acesso_sistema import acessar_sistema
from secoes_sistema.usuarios import cadastrar_usuario, login_sistema, delete_users
import msvcrt
import sys
import getpass

limite_tentativas = 3
tentativas = 0

conn = criar_conexao()

if conn:
    conn.close()

while True:
    limpar_terminal()
    print('Bem vindo ao sistema da biblioteca!')
    print('Digite sua escolha')
    print('1 - Login  || 2 - Cadastrar Novo Usuário || 3 - Excluir Usuário || 4 - Fechar Sistema')
    
    opcao = input('Digite sua opção: ')

    
    if opcao == '1':
        limpar_terminal()
        email_users = input('Digite o email de um usuário cadastrado: ')
        password = getpass.getpass('Digite a senha do usuário: ')
        autenticar_usuario = login_sistema(email_users, password)
        if autenticar_usuario:
            print('Acesso Permitido!')
            print('Aperte qualquer tecla para ir para próxima sessão')
            msvcrt.getch()
            acessar_sistema(autenticar_usuario)
        else:
            print('Usuário ou senha incorreto!')
            tentativas += 1
            msvcrt.getch()

            if tentativas == limite_tentativas:
                limpar_terminal()
                print('Número máximo de tentativas atingido! \nAcesso Negado!')
                sys.exit()

    if opcao == '2':
        limpar_terminal()
        name_users = input('Digite o nome do novo usuário: ')
        email_users = input('Digite um email para cadastrar o usuário: ')
        password = getpass.getpass('Digite uma senha de acesso para o usuário: ')
        cadastrar_usuario(name_users, email_users, password)

    if opcao == '3':
        email_users = input('Informe o email do usuário que deseja excluir: ')
        delete_users(email_users)

    if opcao == '4':
        break