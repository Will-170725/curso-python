# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.

numeros = []
pares = []
impares = []
continuar = 'S'
while continuar == 'S':
    numero = int(input('Digite um número: '))
    numeros.append(numero)
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)
    continuar = input('Deseja continuar? [S/N] ').strip().upper()
    while continuar != 'S' and continuar != 'N':
        continuar = input('Digite "S" para continuar ou "N" para encerrar: ').strip().upper()
print(f'Os números digitados foram {numeros}')
print(f'Os números pares digitados foram {pares}')
print(f'Os números ímpares digitados foram {impares}')

# Resolução do professor

num = list()
pares = list()
ímpares = list()
while True:
    num.append(int(input('Digite um número: ')))
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
#print(num)
for i, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        ímpares.append(v)
print('-=' * 30)
print(f'A lista completa é {num}')
print(f'A lista de pares é {pares}')
print(f'Alista de ímpares é {ímpares}')
