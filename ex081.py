# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

numeros = []
continuar = 'S'
while continuar == 'S':
    numeros.append(int(input('Digite um valor: ')))
    continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()
    while continuar != 'S' and continuar != 'N':
        continuar = str(input('Digite "S" para continuar ou "N" para encerrar: ')).strip().upper()
print(f'Foram digitados {len(numeros)} números')
numeros.sort(reverse=True)
print(f'Lista ordenada de forma decrescente: {numeros}')
if 5 in numeros:
    print(f'O número 5 se encontra na lista nas posições ', end = '')
    for posicao, numero in enumerate(numeros):
        if numero == 5:
            print(posicao, end = '... ')
else:
    print('O número 5 não foi digitado.')

# Resolução do professor

valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'Você digitou {len(valores)} elementos.')
valores.sort(reverse=True)
print(f'Os valores em ordem decrescente são {valores}')
if 5 in valores:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista!')
