import subprocess
commitar = input('Escreva a mensagem para o commit: ')
if commitar == '':
    print('A mensagem de commit não pode ser vazia! ')
else:
    subprocess.run('git add .')
    subprocess.run(f'git commit -m "{commitar}"')
    subprocess.run('git push origin main')