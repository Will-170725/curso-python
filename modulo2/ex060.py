# Faça um programa que leia um número qualquer e mostre seu fatorial.
# Ex:
# 5! = 5x4x3x2x1 = 120

numero = int(input('Digite um número: '))
contador = numero
resultado = 1
while contador > 1:
    resultado = resultado * contador
    contador -= 1
if numero < 0:
    print(f'Digite um valor válido, maior que 0')
else:
    print(f'O fatorial de {numero}! é igual a {resultado}')

numero = int(input('Digite um número: '))
resultado = numero
for contador in range(numero - 1, 0, -1):
    resultado *= contador
if numero < 0:
    print('Digite um valor válido maior que 0')
else:
    print(f'O fatorial de {numero} é igual a {resultado}')

# Resolução do professor

from math import factorial
n = int(input('Digite um número para calcular seu Fatorial: '))
f = factorial(n)
print(f'O fatorial de {n} é {f}.')

n = int(input('Digite um número para calcular seu Fatorial: '))
c = n
f = 1
print(f'Calculando {n}! = ', end = '')
while c > 0:
    print(f'{c}', end = '')
    print(' x ' if c > 1 else ' = ', end = '')
    f *= c
    c -= 1
print(f'{f}')
