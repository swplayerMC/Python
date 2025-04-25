import os
import json

#Caminho inicial:
pathn = r"."

#Caminho files:
pathf = r"./files"

#Caminho files "secreto":
pathfs = r'C:/.keysaving/.data/files'

#Caminho user.data.json:
pathud = r'C:/.keysaving/.data/files/user_data.json'

#Caminho "secreto":
paths = r"C:/.keysaving/.data"

#Função criar usuário (local)
def create_user():
    print("Primeiro, é necessário criar um usuário")
    setuser = "Digite o nome do usuário: "
    setpassword = "Agora, digite a senha: "
    user = input(setuser)
    password = input(setpassword)
    user_data = {
        "user":user,
        "password":password
}

    #Cria o arquivo user.data
    try:
        os.makedirs(pathf)
    except FileExistsError:
        pass
    with open('files/user_data.json', 'w') as u_data_file:
        json.dump(user_data, u_data_file)
    return user

#Função procurar usuário local
def lookfor_user():
    #Lê o arquivo user.data
    username = None

    try:
        with open(pathud, 'r') as u_data_file:
            user_data = json.load(u_data_file)
            username = user_data['user']
        print(f"Bem vindo de volta, {username}!")

    except Exception:
        print("Você não está logado")
        username = create_user()
        print(f"Você esta logado! Bem vindo, {username}!")


