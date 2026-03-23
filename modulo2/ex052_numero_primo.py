# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

numero = int(input('Digite um número: '))
c = 1
ainda_nao_achei_divisor = True
for c in range(numero - 1, 1, -1):
    if numero % c == 0:
        ainda_nao_achei_divisor = False
if ainda_nao_achei_divisor == False and numero > 2:
    print(f'\033[31;1mO número {numero} não é um número primo, é um número composto\033[m')
elif numero >= 2:
    print(f'\033[32mO número {numero} é um numero primo!\033[m')
else:
    print(f'\033[31mO número {numero} não é um numero primo!\033[m')

# Resolução do professor

núm = int(input('Digite um número: '))
total = 0
for contador in range(1, núm + 1):
    if núm % contador == 0:
        print('\033[33m', end = '')
        total += 1
    else:
        print('\033[31m', end = '')
    print(f'{contador} ', end = '')
print(f'\n\033[mO número {núm} foi divisível {total} vezes')
if total == 2:
    print('E por isso ele É PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')
