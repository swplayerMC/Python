import os
import shutil

# Função para organizar os arquivos
def organizar_arquivos(diretorio):
    # Definindo as categorias e seus subtipos com a numeração nas categorias principais
    categorias = {
        '[4] Media': {
            'Áudio': ['.mp3', '.wav', '.flac', '.m4a', '.opus'],
            'Vídeo': ['.mp4', '.avi', '.mkv', '.mov', '.webm'],
            'Imagens': ['.gif', '.jpeg', '.jpg', '.png', '.webp']
        },
        '[5] Documentos': {
            'PDF': ['.pdf'],
            'TXT': ['.txt'],
            'DOCX': ['.docx'],
            'XLSX': ['.xlsx']
        },
        '[6] Zipados': ['.zip', '.rar', '.7z', '.tar', '.gz', '.xz'],
        '[7] Executáveis': ['.exe', '.bat', '.msi', '.apk'],
        '[8] Torrent': ['.torrent'],
        '[9] Photoshop': ['.psd'],
        '[10] ISO': ['.iso'],
        '[11] Outros': []
    }

    # Criando as pastas principais
    for categoria, subcategorias in categorias.items():
        if isinstance(subcategorias, dict):  # Se for dicionário (como em 'Media' ou 'Documentos')
            for subcategoria in subcategorias:
                pasta_subcategoria = os.path.join(diretorio, categoria, subcategoria)
                if not os.path.exists(pasta_subcategoria):
                    os.makedirs(pasta_subcategoria)
        else:  # Se for lista de extensões (como em 'Torrent' ou 'Zipados')
            pasta_categoria = os.path.join(diretorio, categoria)
            if not os.path.exists(pasta_categoria):
                os.makedirs(pasta_categoria)

    # Organizando os arquivos na pasta
    for item in os.listdir(diretorio):
        caminho_item = os.path.join(diretorio, item)

        # Ignorar o arquivo atual do programa (por exemplo, "organizador_de_arquivos.py")
        if item == 'organizador de arquivos.py':
            continue

        if os.path.isfile(caminho_item):  # Verificando se é um arquivo
            # Identificando a extensão do arquivo
            nome, extensao = os.path.splitext(item)

            # Verificando a categoria e movendo o arquivo
            movido = False
            for categoria, subcategorias in categorias.items():
                if isinstance(subcategorias, dict):  # Categoria com subcategorias
                    for subcategoria, tipos in subcategorias.items():
                        if extensao.lower() in tipos:
                            pasta_destino = os.path.join(diretorio, categoria, subcategoria)
                            shutil.move(caminho_item, os.path.join(pasta_destino, item))
                            movido = True
                            break
                else:  # Categoria sem subcategorias
                    if extensao.lower() in subcategorias:
                        pasta_destino = os.path.join(diretorio, categoria)
                        shutil.move(caminho_item, os.path.join(pasta_destino, item))
                        movido = True
                        break

            if not movido:
                # Se não encontrar a categoria, move para 'Outros' com subpastas por extensão
                pasta_outros = os.path.join(diretorio, '[11] Outros')

                # Criar uma subpasta com o nome da extensão (ex: '.txt' -> 'TXT')
                subpasta_extensao = extensao[1:].upper()  # Exemplo: '.txt' -> 'TXT'
                pasta_subpasta = os.path.join(pasta_outros, subpasta_extensao)
                if not os.path.exists(pasta_subpasta):
                    os.makedirs(pasta_subpasta)

                # Mover o arquivo para dentro da subpasta da extensão
                shutil.move(caminho_item, os.path.join(pasta_subpasta, item))

# Diretório onde o programa será executado (no caso da área de trabalho, por exemplo)
diretorio_atual = os.getcwd()

# Executando a função para organizar os arquivos
organizar_arquivos(diretorio_atual)
