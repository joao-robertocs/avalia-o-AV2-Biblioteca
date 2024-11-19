from sistema_principal.config_db import criar_conexao
from funcionalidades.limpador_tela import limpar_terminal

def cadastrar_usuario(name_users, email_users, password):
    limpar_terminal()
    conn = criar_conexao()
    cursor = conn.cursor()

    sql = 'INSERT INTO users (name_users, email_users, password) values (%s, %s, %s)'
    cursor.execute(sql, (name_users, email_users, password))
    conn.commit()

    print(f'Usuário {name_users} cadastrado com sucesso!')