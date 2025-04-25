import os
from cryptography.fernet import Fernet



#Lista dos arquivos para criptografar
folders = [
    os.path.join(r"C:/.keysaving")
]
arquivos = []

def ks_encryping():
    #Criar a chave para criptografar e descriptografar
    key = Fernet.generate_key()
    with open('chave.key', 'wb') as chave:
        chave.write(key)
    for folder in folders:
        for root, dirs, files in os.walk(folder):
            for file in files:

                if file in ['keysaving.py','user_manage.py','ks_safety.py','chave.key','ks_decrypt.py']:
                    continue

                file_path = os.path.join(root, file)
                arquivos.append(file_path)

    #Criptografar os arquivos
    for arquivo in arquivos:
        with open(arquivo, 'rb') as file:
            content = file.read()
        encrypted_content = Fernet(key).encrypt(content)
        with open(arquivo, 'wb') as file:
            file.write(encrypted_content)
ks_encryping()