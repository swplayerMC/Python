import os
from cryptography.fernet import Fernet



#Lista dos arquivos para criptografar
folders = [
    os.path.join(r"C:/.keysaving")
]
arquivos = []
def ks_decrypting():
    #Criar a chave para criptografar e descriptografar
    with open('chave.key', 'rb') as chave:
        secret_key = chave.read()
    for folder in folders:
        for root, dirs, files in os.walk(folder):
            for file in files:

                if file in ['keysaving.py','user_manage.py','ks_safety.py','chave.key']:
                    continue

                file_path = os.path.join(root, file)
                arquivos.append(file_path)

    #Descriptografar os arquivos
    for arquivo in arquivos:
        with open(arquivo, 'rb') as file:
            content = file.read()
        decrypted_content = Fernet(secret_key).decrypt(content)
        with open(arquivo, 'wb') as file:
            file.write(decrypted_content)
ks_decrypting()