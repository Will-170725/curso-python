# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

maior = 0
menor = 0
for pessoa in range(1, 6):
    peso = float(input(f'Digite o peso da {pessoa}ª pessoa: '))
    if pessoa == 1:
        maior = peso
        menor = peso
    if peso >= maior:
        maior = peso
    elif peso <= menor:
        menor = peso
print(f'Dos cinco pesos informados {maior}Kg é o maior.')
print(f'Dos cinco pesos informados {menor}Kg é o menor.')

# Resolução do professor

maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input(f'Peso da {p}ª pessoa: '))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso lido foi de {maior}Kg')
print(f'O menor peso lido foi de {menor}Kg')
