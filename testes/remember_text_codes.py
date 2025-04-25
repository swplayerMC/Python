#Tupla para as cores disponíveis
cores = (
    "branco",
    "prata",
    "cinza",
    "preto",
    "vermelho escuro",
    "amarelo",
    "azul escuro",
    "verde",
    "ciano",
    "roxo",
    "dourado",
    "laranja",
    "azul",
    "lima",
    "aqua",
    "vermelho",
    "rosa"
)


#Tupla para os estilos disponíveis
estilos = (
    "negrito",
    "italico",
    "ofuscante",
    "sublinhado",
    "cortado"
)


#Dicionário para cores e seus codigos
cores_cod = {  
    "branco": "§f",
    "prata": "§7",
    "cinza": "§8",
    "preto": "§0",
    "vermelho escuro": "§4",
    "amarelo": "§e",
    "azul escuro": "§1",
    "verde": "§2",
    "ciano": "§3",
    "roxo": "§5",
    "dourado": "§6",
    "laranja": "§v",
    "azul": "§9",
    "lima": "§a",
    "aqua": "§b",
    "vermelho": "§c",
    "rosa": "§d"
}


#Dicionário para estilos e seus codigos
estilos_cod = {
    "negrito":"§l",
    "italico": "§o",
    "ofuscante": "§k",
    "sublinhado": "§n",
    "cortado": "§m",
    "reset": "§r"
}


#Apenas definindo variáveis para usar nas funções
cor = "cor"

estilo = "estilo"

cancelar = ""

jogador_cancelou = "</> O jogador decidiu cancelar..."

print("Presione ENTER para cancelar")
cor_ou_estilo = input("Você quer lembrar uma cor ou estilo? Digite COR ou ESTILO: ").lower()    #Pergunta se escolhe cor ou estilo


#Definindo as funções:
def escolha_cor():
    lembrar_cor = input("Qual é a cor a ser lembrada? ").lower()
    if lembrar_cor in cores:    #Se a resposta pro input coincidir com algum item em cores_cod:
        print(f"O símbolo § para a cor {lembrar_cor} é:")
        print(cores_cod[lembrar_cor])   #Dá um print da chave e valor do item que coincidiu
    elif lembrar_cor == cancelar:   #Se o "jogador" não digitar nada ele vai mostrar um print("</> O jogador decidiu cancelar...")
        print(jogador_cancelou)
        StopIteration
    else:
        print(f"A cor {lembrar_cor} não foi encontrada!")
        print("As cores disponíveis são:")
        for cor in cores:
            print(f"\n{cor}")


def escolha_estilo():
    lembrar_estilo = input("Qual é o estilo a ser lembrado? ").lower()
    if lembrar_estilo in estilos:   #Se a resposta pro input coincidir com algum item em estilos_cod:
        print(f"Para o usar o estilo {lembrar_estilo}, use:")
        print(estilos_cod[lembrar_estilo])  #Dá um print da chave e valor do item que coincidiu
    elif lembrar_estilo == cancelar:    ##Se o "jogador" não digitar nada ele vai mostrar um print("</> O jogador decidiu cancelar...")
        print(jogador_cancelou)
        StopIteration
    else:
        print(f"O estilo {lembrar_estilo} não foi encontrado!")
        print("Os estilos disponíveis são:")
        for estilo in estilos:
            print(f"\n{estilo}")


#Programando quando as funções definidas devem ser usadas:

if cor_ou_estilo == cor:    #Se a escolha for COR ele vai chamar a função escolha_cor()
    escolha_cor()

elif cor_ou_estilo == estilo:   #Caso contrario e se a escolha for ESTILO ele vai chamar a função escolha_estilo()
    escolha_estilo()

elif cor_ou_estilo == cancelar:     #Se o "jogador" não digitar nada ele vai mostrar um print("</> O jogador decidiu cancelar...")
    print(jogador_cancelou)
    StopIteration
else:
    print("É para digitar COR ou ESTILO ")  #E caso nenhuma condição seja atendida, ele vai mostrar a mensagem nesse print()