#// LOOP DE SOLETRAR LETRA EM "nome" //
#nome = "Calebe"
#for letra in nome:
#    print(letra)
#// LOOP COM CONTADOR ATÉ 8 //
#contador = 0
#while contador <= 8:
#    print(f"O contador está no valor {contador}")
#    contador +=1
#// LOOP COM WHILE TRUE //
#while True:
#    numero = int(input("Digite um número par: "))
#    if numero % 2 == 0:
#        print("Você digitou um número par. Obrigado!")
#        break
#    else:
#        print("Você digitou um número ímpar! seu burro")
#// DESAFIOS DA AULA //
#contador = 0
#while contador <= 9:
#    contador +=1
#    print(contador)
#numero = int(input("Escolha um número de 1 a 10: "))
#multi = 0
#while multi < 10:
#    multi += 1
#    resultado = numero * multi
#    print(f"\n{numero} x {multi}= {resultado}")
#def contagem_regressiva(n1):
#    contador = n1
#    while contador >= 0:
#        print(contador)
#        contador -= 1
#contagem_regressiva(10)
#def maior_numero(lista_de_numeros):
#    maior_numero = lista_de_numeros[0]
#    for numero in lista_de_numeros:
#       if numero > maior_numero:
#           maior_numero = numero
#    return maior_numero
#
#lista = [ 1, 2, 3, 4, 5, 6, 12, 64, 857, 29419248 ]
#maior_numero_da_lista = maior_numero(lista)
#print(f"O maior numero da lista é {maior_numero_da_lista}")