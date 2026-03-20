# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for impar, desconsidere-o

soma = 0
contador = 0
for c in range(1, 7):
    numero = int(input('Digite um número: '))
    if numero % 2 == 0:
        soma += numero
        contador += 1
if contador == 1:
    print(f'Foi digitado apenas um numero par: {soma}')
else:
    print(f'A soma dos {contador} números pares digitados é {soma}')

# Resolução do professor

soma = 0
contador = 0
for c in range(1, 7):
    num = int(input(f'Digite o {c}º valor: '))
    if num % 2 == 0:
        soma =  soma + num
        contador = contador + 1
print(f'Você informou {contador} números PARES e a soma foi {soma}')
