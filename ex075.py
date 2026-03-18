# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

posicao = 0
flag = 0
numero1 = int(input('Digite o primeiro valor: '))
numero2 = int(input('Digite o segundo valor: '))
numero3 = int(input('Digite o terceiro valor: '))
numero4 = int(input('Digite o quarto valor: '))
tupla = (numero1, numero2, numero3, numero4)
print(tupla)
print(f'O valor 9 apareceu {tupla.count(9)} vezes.')
for contador in range(0, len(tupla)):
    if tupla[contador] == 3:
        flag = 1
        if flag == 1:
            posicao = contador + 1
if posicao > 0 :
    print(f'O primeiro valor 3 foi digitado na {posicao}ª posição')
else:
    print(f'O valor 3 não foi digitado em nenhuma posição')
flag = 0
tuplapar = ()
print(f'Os números pares digitados foram ', end = '')
for numero in tupla:
    if numero % 2 == 0:
        if numero % 2 == 1:
            print('Não foi digitado nenhum número par')
        else:
            print(numero, end = ' ')

print('\n')
# Resolução do professor

núm = (int(input('Digite um número: ')),
       int(input('Digite outro número: ')),
       int(input('Digite mais um número: ')),
       int(input('Digite o último número: ')))
print(f'Você digitou os valores {núm}')
print(f'O valor 9 apareceu {núm.count(9)} vezes')
if 3 in núm:
    print(f'O valor 3 apareceu na {núm.index(3) + 1}ª posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print('Os valores pares foram ', end = '')
for n in núm:
    if n % 2 == 0:
        print(n, end = ' ')
