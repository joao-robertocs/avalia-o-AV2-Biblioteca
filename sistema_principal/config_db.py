import psycopg2

def criar_conexao():
    try:    
        conn = psycopg2.connect(
            dbname = 'postgres',
            user = 'postgres',
            password = '201526j',
            host = 'localhost',
            port = '5432',
        )
        print('Conexão Realizada com Sucesso!')
        return conn
    except Exception as e:
        print(f'Erro ao conectar com o banco de dados: {e}')
        return None 