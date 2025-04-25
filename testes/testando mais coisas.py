
def jogar():
    #Defini umas variáveis para escrever menos...
    erros = 0
    errou = "Você errou! "
    acertou ="Você acertou! "
    print("Vamos começar o jogo!\n")
    
    #Questão 1:
    pergunta1 = int(input("\nQuanto é 1 + 1? "))
    if pergunta1 != 2:
        print(errou)
        erros += 1
    else:
        print(acertou)
        next
    
    #Questão 2:
    pergunta2 = input("\nQual é a tradução de HELLO? ").lower()
    pergunta2resp = ["ola", "olá"]
    if pergunta2 not in pergunta2resp:
        print(errou)
        erros += 1
    else:
        print(acertou)
        next
    
    #Questão 3:
    pergunta3 = input("\nMacã, pera, abacaxi, pedra, mamão, banana\nQual desses não é uma fruta? ")
    if not pergunta3 == "pedra":
        print(errou)
        erros += 1
    else:
        print(acertou)
        next
    
    #Final:
    if erros == 1:
        print(f"\nVocê teve {erros} erro\n")
    elif erros >= 2:
        print(f"\nVocê teve {erros} erros\n")
    else:
        print(f"\nParabéns! Você acertou tudo! 0 erros!\n")
    
    #Jogar de novo:
    again = input("Escreva AGAIN para jogar denovo! ").lower()
    if again == "again":
        jogar()
    else:
        StopIteration

#Início   (SIM O INICIO TA NO FINAL DO CÓDIGO)
print("Bem vindo! Precione a tecla ENTER para iniciar o jogo!       Ou escreva CANCELAR para sair...")
start = input().lower()
if start == "cancelar":
    StopIteration
else:
    jogar()