# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

numero = 0
acumulador = 0
contador = 0
while numero < 999:
    numero = int(input('Digite um número [999 para parar]: '))
    if numero < 999:
        soma = numero + acumulador
        numero = soma
        acumulador = numero
        contador += 1
print(f'Foram digitados {contador} números, e a soma entre eles é igual a {soma}.')
print('ACABOU')

# Resolução do professor

núm = cont = soma = 0
núm = int(input('Digite um número [999 para parar]: '))
while núm != 999:
    soma += núm
    cont += 1
    núm = int(input('Digite um número [999 para parar]: '))
print(f'Você digitou {cont} número e a soma entre eles foi {soma}.')
