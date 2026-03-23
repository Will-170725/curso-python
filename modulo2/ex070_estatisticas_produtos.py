# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final, mostre:
# A) Qual é o total gasto na compra.
# B) Quantos produtos custam mais de R$1000.
# C) Qual é o nome do produto mais barato.

total = 0
mais = 0
contador = 0
while True:
    nome = str(input('Digite o nome do produto: ')).strip()
    preco = float(input('Digite o preço do produto: R$'))
    while preco < 0:
        print('\033[31mDigite um preço válido\033[m')
        preco = float(input('Digite o preço do produto: R$'))
    contador += 1
    if contador == 1:
        barato = preco
        nomebarato = nome
    total += preco
    if preco > 1000:
        mais += 1
    if preco < barato:
        barato = preco
        nomebarato = nome
    continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()
    while continuar != 'S' and continuar != 'N':
        print('\033[31mDigite S para sim ou N para não\033[m')
        continuar = str(input('Deseja continuar? '))
    if continuar == 'N':
        break
print(f'O total gasto na compra é de R${total:.2f}')
if mais == 0:
    print('Nenhum produto custa mais de R$1000.00')
elif mais == 1:
    print(f'{mais} produto custa mais de R$1000.00')
else:
    print(f'{mais} produtos custam mais de R$1000.00')
print(f'O nome do produto mais barato é {nomebarato} que custa R${barato:.2f}')

# Resolução do professor

total = totmil = menor = cont = 0
barato = ''
while True:
    produto = str(input('Nome do Produto: '))
    preço = float(input('Preço: R$'))
    cont += 1
    total += preço
    if preço > 100:
        totmil += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {totmil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')
