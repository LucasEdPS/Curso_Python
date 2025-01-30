nome = 'Luiz Otávio'

i = 0
nova_string = ''
while i < len(nome):
    nova_string += f'*{nome[i]}'
    i += 1

print(nova_string)