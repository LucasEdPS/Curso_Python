"""
Fatiamento de strings
 012345678
 Olá mundo
-987654321
Fatiamento [i:f:p] [::]
i - inicio
f - fim
p - quantidade de passos
Obs.: a função len retorna a qtd 
de caracteres da str
"""
variavel = 'Olá mundo'
print(len(variavel))
print(variavel[0:len(variavel)])
print(variavel[0:9])
print(variavel[0:3])
print(variavel[:3])
print(variavel[4:9])
print(variavel[4:])
print(variavel[::-1])
print(variavel[-1:-10:-1])
print(variavel[::2])
print(variavel[::-2])