# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas
# O nome com todas minúsculas.
# Quantas letras ao todo (sem considerar espaços).
# Quantas letras tem o primeiro nome.

nome = str(input('\033[1;37mDigite seu nome completo: \033[m')).strip()
separa = nome.split()
print('\033[1;32mAnalisando seu nome...\033[m')
print(f'\033[1;31mSeu nome em maiúsculas é {nome.upper()}\033[m')
print(f'\033[1;33mSeu nome em minúsculas é {nome.lower()}\033[m')
print(f'\033[1;34mSeu nome tem ao todo {len(nome)-nome.count(' ')} letras\033[m')
print(f'\033[1;35mSeu primeiro nome tem {nome.find(' ')} letras\033[m')
print(f'\033[1;36mSeu primeiro nome é {separa[0]} e ele tem {len(separa[0])} letras\033[m')
