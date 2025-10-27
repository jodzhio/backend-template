from bcrypt import hashpw, gensalt, checkpw

def hash_password(password: str) -> str:
    password_bytes = password.encode('utf-8')
    salt = gensalt()
    hashed_bytes = hashpw(password_bytes, salt)
    return hashed_bytes.decode('utf-8')

def verify_password(password: str, hashed_str: str) -> bool:
    password_bytes = password.encode('utf-8')
    hashed_bytes = hashed_str.encode('utf-8')  # Преобразуем строку обратно в байты
    return checkpw(password_bytes, hashed_bytes)
