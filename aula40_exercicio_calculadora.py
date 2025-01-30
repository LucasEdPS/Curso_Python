while True:
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Digite qual operação (+,-,/,*): ')

    validade = None
    num_1_float = 0
    num_2_float = 0

    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        validade = True

    except:
        validade = None

    if validade is None:
        print('Um ou ambos os números digitados são inválidos.')
        continue

    operadores_permitidos = '+-/*'
    
    if operador not in operadores_permitidos:
        print('Operador inválido.')
        continue
        
    if len(operador)>1:
        print('Digite apenas um operador.')
        continue    

    print('Resultado: ')

    if operador == '+':
        print(f'{num_1_float}+{num_2_float}={num_1_float+num_2_float}')
    elif operador == '-':
        print(f'{num_1_float}-{num_2_float}={num_1_float-num_2_float}')
    elif operador == '/':
        print(f'{num_1_float}/{num_2_float}={num_1_float/num_2_float}')
    elif operador == '*':
        print(f'{num_1_float}*{num_2_float}={num_1_float*num_2_float}')
    else:
        print('Espero que nunca chegue aqui')

    sair = input('Quer sair? [s]im: ').lower().startswith('s')
    if sair :
        break