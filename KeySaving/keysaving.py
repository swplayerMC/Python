import os
import shutil
import user_manage
import ks_safety
import ks_decrypt

ks_decrypt.ks_decrypting()

#Obtem o nome de usuário:
user0 = os.getenv("USERNAME")

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

#Ignore por enquanto
# folders = [
#     os.path.join(r"D:/Training Python/keySaving/data")
#     ]
# arquivos = []



#Verifica se a pasta "secreta" já existe.
def sfolder_verify():
    ks_data = "C:/.keysaving/.data"
    if not os.path.exists(ks_data):
        os.makedirs(ks_data)
    else:
        pass


def sfiles_verify():
    ks_files = "C:/.keysaving/.data/files"
    if not os.path.exists(ks_files):
        os.makedirs(ks_files)




#Move os arquivos da pasta atual para a pasta "secreta" e se der erro mostra diferentes mensagens
def move_to_sfolder():
    try:
        shutil.move(pathf, pathfs)
    except Exception:
        sfiles_verify()
    except FileExistsError:
        print("O arquivo já existe")
    except shutil.Error as e:
        print(f"Ocorreu um erro ao mover o arquivo: {e}")
    except FileNotFoundError:
        print("Erro: O arquivo ou diretório de origem/destino não foi encontrado.")
    except PermissionError:
        print("Erro: Permissão negada ao mover o arquivo.")

try:
    user_manage.lookfor_user()
except Exception:
    user_manage.create_user()

move_to_sfolder()
sfolder_verify()
