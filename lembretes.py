#Para obter valor de chave de um .json  :]
import json

#Quando estiver criando o arquivo:
dicionario = {
        'chave1': 'valor1',     #Pode adicionar inumeras chaves e valores. 
        'chave2': 'valor2',     #E inclusive, as chaves e/ou valores podem ser alguma variavel definida 
        'chave3': 'valor3'      #Mas não é possível printar ou obter uma chave (sem ser o valor dela, ele sempre pega o valor da chave).
    }
with open('o_nome_do_arquivo.json', 'w') as apelido:
    json.dump(dicionario, apelido)


#Quando fizer a parte de ler o arquivo:
with open('o_nome_do_arquivo.json', 'r') as apelido:
        variavel_para_load_json = json.load(apelido)
        variavel_para_receber_valor = variavel_para_load_json['chave1 (exemplo)'] #Não pode tentar carregar o valor em si, só a chave que guarda ele. Porque ela já pega o valor automaticamente
