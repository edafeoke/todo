from passlib.context import CryptContext

password_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

class Hashing():
    def hash_password(password: str):
        '''A function that hashes a password'''
        hashed_password = password_context.hash(password)
        return hashed_password