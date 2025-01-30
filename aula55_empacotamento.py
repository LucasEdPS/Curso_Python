"""
Introdução ao empacotamento e desempacotamento
"""
nome, *resto = ['Maria', 'Helena', 'Luiz']
print(nome, resto)

_, _, nome, *resto = ['Maria', 'Helena', 'Luiz']
print(nome, resto)

nome, *_ = ['Maria', 'Helena', 'Luiz']
print(nome)