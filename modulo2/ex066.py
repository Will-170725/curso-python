# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

contador = soma = 0
while True:
    numero = int(input('Digite um número (999 para parar): '))
    if numero == 999:
        break
    contador += 1
    soma += numero
print(f'Foram digitados {contador} números e a soma entre eles é {soma}')

# Resolução do professor

soma = cont = 0
while True:
    num = int(input('Digite um valor (999 para parar): '))
    if num == 999:
        break
    cont += 1
    soma += num
print(f'A soma dos {cont} valores foi {soma}!')
