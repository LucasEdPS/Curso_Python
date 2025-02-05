import re
import sys
entrada = input('CPF: ')
cpf = re.sub(r'[^0-9]', '', entrada)
entrada_e_sequencial = entrada[0]*len(entrada) == entrada

if entrada_e_sequencial:
    print('Você enviou dados sequenciais')
    sys.exit()

digitos_cpf = []
for n in cpf:
    try:
        digitos_cpf.append(int(n))
        if len(digitos_cpf) == 9:
            break
    except ValueError:
        continue

soma_1 = 0
for i in range(len(digitos_cpf)):
   soma_1 += (10-i)*(digitos_cpf[i])

digito = (soma_1*10) % 11
primeiro_digito = digito if digito<=9 else 0

digitos_cpf.append(primeiro_digito)

soma_2 = 0
for i in range(len(digitos_cpf)):
   soma_2 += (11-i)*(digitos_cpf[i])

digito = (soma_2*10) % 11
segundo_digito = digito if digito<=9 else 0

digitos_cpf.append(segundo_digito)
validador = ''
for digito in digitos_cpf:
    validador += str(digito)

if validador == cpf:
    print(f'{cpf} é válido')
else:
    print('CPF Inválido')