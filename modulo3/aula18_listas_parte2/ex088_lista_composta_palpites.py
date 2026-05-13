# Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import randint
from time import sleep
cadastro = list()
numeros = list()
jogos = (int(input('Quantos jogos serão gerados? ')))
for palpite in range(0, jogos):
    while len(numeros) < 6:
        computador = randint(1, 60)
        if computador not in numeros:
            numeros.append(computador)
    numeros.sort()
    cadastro.append(numeros[:])
    numeros.clear()
    print(f'Jogo {palpite + 1}: {cadastro[palpite]}')
    sleep(1)

# Resolução do professor

from random import randint
from time import sleep
lista = list()
jogos = list()
print('-' * 30)
print('      JOGA NA MEGA SENA      ')
print('-' * 30)
quant = int(input('Quantos jogos você quer que eu sorteie? '))
tot = 1 # total
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-=' * 3, f' SORTEANDO {quant} JOGOS ', '-=' * 3)
for i, l in enumerate(jogos): # enumerate trata indice e lista, i = indice, l = lista
    print(f'Jogo {i + 1}: {l}')
    sleep(1)
print('-=' * 5, '< BOA SORTE! >', '-=' * 5)
#print(f'Os números sorteados foram {jogos}')
