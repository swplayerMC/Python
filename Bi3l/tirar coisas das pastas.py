import os
import shutil

def mover_para_diretorio_principal(diretorio):
    # Percorre todas as pastas e subpastas dentro do diretório especificado
    for root, dirs, files in os.walk(diretorio, topdown=False):
        for file in files:
            caminho_arquivo = os.path.join(root, file)

            # Cria um caminho de destino para o arquivo no diretório principal
            destino = os.path.join(diretorio, file)

            # Verifica se o arquivo já existe no diretório principal
            if os.path.exists(destino):
                # Se existir, cria um nome único para o arquivo
                nome, extensao = os.path.splitext(file)
                contador = 1
                novo_nome = f"{nome}_{contador}{extensao}"
                destino = os.path.join(diretorio, novo_nome)
                # Garante que o nome seja único, incrementando até encontrar um nome disponível
                while os.path.exists(destino):
                    contador += 1
                    novo_nome = f"{nome}_{contador}{extensao}"
                    destino = os.path.join(diretorio, novo_nome)

            # Move o arquivo para o diretório principal
            shutil.move(caminho_arquivo, destino)

        # Exclui as pastas vazias após mover os arquivos
        for dir in dirs:
            caminho_pasta = os.path.join(root, dir)
            if not os.listdir(caminho_pasta):  # Se a pasta estiver vazia
                os.rmdir(caminho_pasta)

# Caminho do diretório onde as pastas estão localizadas (pode ser o caminho completo ou o diretório atual)
diretorio_atual = os.getcwd()  # Use o diretório atual ou forneça um caminho absoluto, se necessário

# Executando a função para mover os arquivos para o diretório principal
mover_para_diretorio_principal(diretorio_atual)
