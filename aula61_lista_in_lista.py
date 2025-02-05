"""
Lista de listas e seus índices
"""
salas = [
    # 0        1
    ['Maria', 'Helena', ],  # 0
    # 0
    ['Elaine', ],  # 1
    # 0       1       2
    ['Luiz', 'João', 'Eduarda', (0,10,20,30,40)],  # 2
]

print(salas[1][0])
print(salas[0][1])
print(salas[2][2])
print(salas[2][3][3])

for sala in salas:
    print(f'A sala é {sala}')
    for item in sala:
        if type(item) == type('a'):
            print(item)
        for numero in item:
            if type(numero) != type('a') :
                print(numero)





"""
Interpretador do Python

python mod.py (executa o mod)
python -u (unbuffered)
python -m mod (lib mod como script)
python -c 'cmd' (comando)
python -i mod.py (interativo com mod)

The Zen of Python, por Tim Peters

Bonito é melhor que feio.
Explícito é melhor que implícito.
Simples é melhor que complexo.
Complexo é melhor que complicado.
Plano é melhor que aglomerado.
Esparso é melhor que denso.
Legibilidade conta.
Casos especiais não são especiais o bastante para quebrar as regras.
Embora a praticidade vença a pureza.
Erros nunca devem passar silenciosamente.
A menos que sejam explicitamente silenciados.
Diante da ambiguidade, recuse a tentação de adivinhar.
Deve haver um -- e só um -- modo óbvio para fazer algo.
Embora esse modo possa não ser óbvio à primeira vista a menos que você seja holandês.
Agora é melhor que nunca.
Embora nunca frequentemente seja melhor que *exatamente* agora.
Se a implementação é difícil de explicar, é uma má ideia.
Se a implementação é fácil de explicar, pode ser uma boa ideia.
Namespaces são uma grande ideia -- vamos fazer mais dessas!
"""