#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira.
#Ex: Digite um número: 6.127. O número 6.127 tem a parte inteira 6

from math import trunc
numero = float(input('Digite um valor: '))
inteira = trunc(numero)
print(f'A porção inteira de \033[1;31m{numero}\033[m é \033[1;34m{inteira}\033[m')
print(f'O valor digitado foi \033[1;33m{numero}\033[m e a sua porção inteira é \033[1;32m{trunc(numero)}\033[m')

print(f'O valor digitado foi \033[1;35m{numero}\033[m e a sua porção inteira é \033[1;36m{int(numero)}\033[m')