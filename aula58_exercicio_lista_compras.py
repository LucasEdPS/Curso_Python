import os
lista_de_compras = []

while True:
    entrada = input(f'Selecione uma opção:\n A: Adicionar R: Remover L: Listar S: Sair: ').upper()


    if entrada == 'S':
        break
    elif entrada == 'A':
        os.system('cls')
        item = input('Digite o item para adicionar na lista: ')
        if bool(item):
            lista_de_compras.append(item)
        else:
            print('Digite algum item para a lista.')
            continue
    elif entrada == 'R':
        os.system('cls')
        remocao = input('Digite qual índice do item quer remover: ')
        try:
            remocao_int = int(remocao)
            if len(lista_de_compras)< remocao_int:
                print('Digite um índice valido.')
                continue
            else:
                try:
                    lista_de_compras.pop(remocao_int)
                except IndexError:
                    print('Digite um índice valido.')
                    continue
        except ValueError:
            print('Digite um índice valido.')
            continue
    elif entrada == 'L':
        os.system('cls')
        if bool(lista_de_compras):
            for indice, compras in enumerate(lista_de_compras):
                print(indice, compras)
        else:
            print('Sem item na lista')
    else:
        os.system('cls')
        print('Digite uma opção válida.')
    
    
