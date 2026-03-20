# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados.
# Ex: Digite um número: 1834
# unidade: 4
# dezena: 3
# centena: 8
# milhar: 1

numero = int(input('Digite um número: '))
unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10
print(f'Unidade: \033[33m{unidade}\033[m')
print(f'Dezena: \033[34m{dezena}\033[m')
print(f'Centena: \033[35m{centena}\033[m')
print(f'Milhar: \033[36m{milhar}\033[m')

numero2 = int(input('Informe um número: '))
numero_string = str(numero2)
print(f'Analisando o número \033[1;32m{numero2}\033[m')
print(f'Unidade \033[1;33m{numero_string[3]}\033[m')
print(f'Dezena \033[1;34m{numero_string[2]}\033[m')
print(f'Centena \033[1;35m{numero_string[1]}\033[m')
print(f'Milhar \033[1;36m{numero_string[0]}\033[m')
