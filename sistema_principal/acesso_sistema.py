import msvcrt
import sys
import getpass
from funcionalidades.limpador_tela import limpar_terminal

def acessar_sistema():
    usuario = 'admin'
    senha = 'admin'
    limite_tentativas = 3
    tentativas = 0

    print('Para acessar o sistema digite usuário e senha corretos')
    while True:
        solicita_usuario = input('Usuário: ')
        solicita_senha = getpass.getpass('Senha: ')
    
        if solicita_usuario == usuario and solicita_senha == senha:
            limpar_terminal()
            print('Acesso Permitido!')
            print('Aperte qualquer tecla para ir para próxima sessão')
            msvcrt.getch()
            break
        else:
            tentativas += 1
            limpar_terminal()
            print('Senha incorreta \nTente de novo')
        
        if tentativas == limite_tentativas:
            limpar_terminal()
            print('Número máximo de tentativas atingido! \nAcesso Negado!')
            sys.exit()
