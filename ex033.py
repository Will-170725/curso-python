# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))
numero3 = int(input('Digite o terceiro número: '))
# Verificando quem é o menor
if numero1 < numero2 and numero1 < numero3:
    menor = numero1
if numero2 < numero1 and numero2 < numero3:
    menor = numero2
if numero3 < numero1 and numero3 < numero2:
    menor = numero3
# Verificando quem é o maior
if numero1 > numero2 and numero1 > numero3:
    maior = numero1
if numero2 > numero1 and numero2 > numero3:
    maior = numero2
if numero3 > numero1 and numero3 > numero2:
    maior = numero3
print(f'O menor valor digitado foi \033[34m{menor}\033[m')
print(f'O maior valor digitado foi \033[31m{maior}\033[m')

a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print(f'O numero \033[1;36m{menor}\033[m é o menor')
print(f'O numero \033[1;31m{maior}\033[m é o maior.')
