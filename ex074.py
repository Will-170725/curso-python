# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint
tupla = (randint(0 , 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print(f'Os valores sorteados foram: {tupla}')
print(f'O maior valor sorteado foi {sorted(tupla)[-1]}')
print(f'O menor valor sorteado foi {sorted(tupla)[0]}')

# Resolução do professor

from random import randint
numeros = (randint(1,10), randint(1, 10), randint(1, 10),
     randint(0, 10), randint(1,10))
print(f'Eu sorteei os valores {numeros}')
print('Os valores sorteados foram: ', end = '')
for n in numeros:
    print(f'{n} ', end = '')
print(f'\nO maior valor sorteado foi {max(numeros)}')
print(f'O menor valor sorteado foi {min(numeros)}')
