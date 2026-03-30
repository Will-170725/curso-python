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
for posicao, dado in enumerate(galera):
    if dado[1] > maior:
        maior = dado[1]
    if dado[1] < menor:
        menor = dado[1]
for posicao, dado in enumerate(galera):
    if dado[1] == maior:
        pesados.append(dado[0])
    if dado[1] == menor:
        leves.append(dado[0])
print(f'O maior peso foi de {maior}Kg. Peso de {pesados}')
print(f'O menor peso foi de {menor}Kg. Peso de {leves}')
