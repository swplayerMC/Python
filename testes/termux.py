user = input('Nome de usuário: ')
print(f'Oi, {user}!')
with open('arquivo.txt', 'w') as arquivo:
	arquivo.write(f'Oi, {user}!')
