"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

numero_str = input('Digite um número inteiro: ')
try:
    numero_int = int(numero_str)
    if numero_int % 2 == 0:
        print(f'O número {numero_int} é par')
    else:
        print(f'O número {numero_int} é ímpar')
except:
    print('O que vc digitou não é um número inteiro')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

hora_str = input('Digite que horas são em numeros inteiros: ')
try:
    hora_int = int(hora_str)

    if hora_int >= 0 and hora_int <= 11:
        print('Bom dia')
    elif hora_int >= 12 and hora_int <= 17:
        print('Boa tarde')
    elif hora_int >= 18 and hora_int <= 23:
        print('Boa noite')
    else:
        print('Não conheço essa hora')
except:
    print('O que vc digitou não é um numero inteiro')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input('Digite seu nome: ')
tamanho_nome = len(nome)

if tamanho_nome > 1 :
    if tamanho_nome <= 4:
        print('Seu nome é curto')
    elif tamanho_nome >= 5 and tamanho_nome <= 6:
        print('Seu nome é normal')
    else:
        print('Seu nome é muito grande')
else:
    print('Digite mais de uma letra.')