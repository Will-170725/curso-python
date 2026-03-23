# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()).
# No final, mostre a lista ordenada na tela.

valores = []
for contador in range(0, 5):
    valor = int(input('Digite um número: '))
    flag = 0
    if valores == []:
        valores.append(valor)
        print(f'Primeiro valor da lista...')
    else:
        for indice in range(0, len(valores)):
            if valor < valores[indice]:
                valores.insert(indice, valor)
                print(f'Adicionado na posição {indice} da lista...')
                flag += 1
                break
        if flag == 0:
            valores.append(valor)
            print('Adicionado ao final da lista...')
print(f'Os valores digitados em ordem foram {valores}')

# Resolução do professor

lista = []
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[len(lista) - 1]: # ou lista[-1]
        lista.append(n)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos += 1
print('-=' * 30)
print(f'Os valores digitados em ordem foram {lista}')
