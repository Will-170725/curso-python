# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

galera = list()
dados = list()
continuar = 'S'
pesados = list()
leves = list()
maior = 0
menor = 0
flagp = 0
flagl = 0
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
for posicao, dado in enumerate(galera):
    dado[1] = maior
    dado[1] = menor
    if dado[1] >= maior:
        pesados.append(dado[0])
        pesados.append(dado[1])
        flagp += 1
    if dado[1] <= menor:
        leves.append(dado[0])
        leves.append(dado[1])
        flagl += 1
    for pessoa in pesados:
        if dado[1] > pessoa[1] and flagp > 1:
            pesados.pop()
            pesados.append(dado[1])
            pesados.append(dado[0])

print(f'O maior peso foi de {max(pesados)}Kg. Peso de {pesados}')
#print(f'O menor peso foi de {min(menor)}Kg. Peso de {leves}')

