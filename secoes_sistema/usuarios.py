from sistema_principal.config_db import criar_conexao
from funcionalidades.limpador_tela import limpar_terminal
from funcionalidades.seguranca import criptografar, checar_senha
import msvcrt

def cadastrar_usuario(name_users, email_users, password):
    try:
        limpar_terminal()
        hashed_password = criptografar(password)
        conn = criar_conexao()
        cursor = conn.cursor()

        query = 'INSERT INTO users (name_users, email_users, password) values (%s, %s, %s)'
        cursor.execute(query, (name_users, email_users, hashed_password))
        conn.commit()
        print(f'Usuário {name_users} cadastrado com sucesso!')
        msvcrt.getch()
    except Exception as e:
        print(f'Erro ao cadastrar usuário: {e}')
        msvcrt.getch()
    finally:
        conn.close()

def login_sistema(email_users, password):
    limpar_terminal()
    try:
        conn = criar_conexao()
        cursor = conn.cursor()

        query = 'SELECT * FROM users WHERE email_users = %s;'
        cursor.execute(query, (email_users,))
        resultado = cursor.fetchone()

    except Exception as e:
        print(f'Erro ao realizar login: {e}')
        msvcrt.getch()
        return False
    finally:
        conn.close()

    if resultado:
        senha_hash = resultado[3]
        if not isinstance(senha_hash, memoryview):
             senha_hash = bytes(senha_hash)

        if checar_senha(password, senha_hash):
            return resultado
    return False


def delete_users(email_users):
    limpar_terminal()
    conn = criar_conexao()
    try:
        cursor = conn.cursor()
        query = 'DELETE FROM users WHERE email_users like %s;'
        cursor.execute(query, (email_users,))
        print('Usuário excluido com sucesso!')
        conn.commit()    
    except Exception as e:
        print(f'Erro ao excluir o usuário: {e}')
    finally:
        cursor.close()
        conn.close()
        msvcrt.getch()