import bcrypt

def criptografar(password):
    password_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password_bytes, salt)
    return hashed.decode('utf-8')

def checar_senha(password, hashed):
    password_bytes = password.encode('utf-8')
    print(f"Password bytes: {password_bytes}")
    print(f"Hashed: {hashed}")

    #return bcrypt.checkpw(password_bytes, hashed)


