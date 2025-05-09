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


#Para digitar commandos no terminal (na pasta atual)
import subprocess
subprocess.run('comando')


#Para obter data e hora do dispositivo
from datetime import datetime #pode ser time e date separadamente também
data = datetime.now()
dia = data.strftime('%d')
mes = data.strftime('%m')
ano = data.strftime('%Y')
hora = data.strftime('%H')
minutos = data.strftime('%M')
# %d = dia, %m = mes, %Y = ano, %H = hora, %M = minutos, %S = segundos
print(f'Hoje é dia {dia} do {mes} de {ano}')
print(f'E são {hora} horas e {minutos} minutos')
#É só um exemplo (é obvio que pode ser bem mais otimizado o código)