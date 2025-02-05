import random

for _ in range(100):
    cpf = ''
    for i in range(9):
        cpf += str(random.randint(0,9))




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

    print(validador)