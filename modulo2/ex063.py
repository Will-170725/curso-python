# Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma Sequência de Fibonacci.
#Ex: 0 → 1 → 1 → 2 → 3 → 5 → 8

n = int(input('Quantos termos você quer mostrar? '))
contador = 0
num1 = 0
num2 = 1
if n <= 0:
    print('Digite um número positivo maior que 0')
elif n == 1:
    print(f'{num1} ', end = '→ ')
elif n == 2:
    print(f'{num1} →', f'{num2} ', end = '→ ')
else:
    print(f'{num1} →', f'{num2} ', end = '→ ')
    while contador < n - 2:
        fibonacci = num1 + num2
        print(f'{fibonacci} ', end = '→ ')
        contador += 1
        num1 = num2
        num2 = fibonacci
print('ACABOU')

# Resolução do professor

print('-' * 30)
print('Sequência de Fibonacci')
print('-' * 30)
n = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
print('~' * 30)
print(f'{t1} → {t2}', end = '')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(f' → {t3}', end = '')
    t1 = t2
    t2 = t3
    cont += 1
print(' → FIM')
