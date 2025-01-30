palavra = 'onomatopeia'
verificador = ''
tentativas = 0
while True:
    entrada = input('Digite uma letra: ').lower()
    tentativas +=1

    if len(entrada)!=1 or entrada.isnumeric():
        print('É para digitar uma letra!')
        continue
    
    if entrada in palavra:
        print('Parabens, a palavra tem essa letra.')
        for letra in palavra:
            if letra == entrada:
                print(entrada)
                if letra not in verificador:
                    verificador += entrada
            else:
                if letra in verificador:
                    print(letra)
                else:
                    print('*')

    else:
        print('Infelizmente não tem esssa letra')
    
    for letra in palavra:
        if letra in verificador:
            continue
        else:
            break
    else:
        print(f'Você acertou a palavra em {tentativas} tentativas')
        break