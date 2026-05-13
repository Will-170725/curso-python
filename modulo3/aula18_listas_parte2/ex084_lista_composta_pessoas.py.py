# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

galera = list()
dados = list()
continuar = 'S'
pesados = list()
leves = list()
while continuar == 'S':
    nome = str(input('Nome: '))
    peso = float(input('Peso: '))
    dados.append(nome)
    dados.append(peso)
    galera.append(dados[:])
    dados.clear()
    continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()
    while continuar != 'S' and continuar != 'N':
        continuar = str(input('Digite "S" para continuar ou "N" para encerrar: ')).strip().upper()
print(f'No total, foram cadastradas {len(galera)} pessoas')
maior = galera[0][1]
menor = galera[0][1]
for dado in galera:
    if dado[1] > maior:
        maior = dado[1]
    if dado[1] < menor:
        menor = dado[1]
for dado in galera:
    if dado[1] == maior:
        pesados.append(dado[0])
    if dado[1] == menor:
        leves.append(dado[0])
print(f'O maior peso foi de {maior}Kg. Peso de {pesados}')
print(f'O menor peso foi de {menor}Kg. Peso de {leves}')

# Resolução do professor

temporaria = []
principal = []
maior = menor = 0
while True:
    temporaria.append(str(input('Nome: ')))
    temporaria.append(float(input('Peso: ')))
    if len(principal) == 0:
        maior = menor = temporaria[1]
    else:
        if temporaria[1] > maior:
            maior = temporaria[1]
        if temporaria[1] < menor:
            menor = temporaria[1]
    principal.append(temporaria[:])
    temporaria.clear()
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-=' * 30)
#print(f'Os dados foram {princ}')
print(f'Ao todo, você cadastrou {len(principal)} pessoas.')
print(f'O maior peso foi de {maior}Kg. Peso de ', end='')
for pessoa in principal:
    if pessoa[1] == maior:
        print(f'[{pessoa[0]}] ', end='')
print()
print(f'O menor peso foi de {menor}Kg. Peso de ', end='')
for pessoa in principal:
    if pessoa[1] == menor:
        print(f'[{pessoa[0]}] ', end='')
print()
