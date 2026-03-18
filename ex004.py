#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

algo = input('\033[1;30;107mDigite algo: \033[m')
print(f'\033[1;97mO tipo primitivo desse valor é {type(algo)}\033[m', )
print(f'\033[1;31mSó tem espaços? {algo.isspace()}\033[m')
print(f'\033[1;32mÉ um número? {algo.isnumeric()}\033[m')
print(f'\033[1;33mÉ alfabético? {algo.isalpha()}\033[m')
print(f'\033[1;34mÉ alfanumérico? {algo.isalnum()}\033[m')
print(f'\033[1;35mEstá em maiúsculas? {algo.isupper()}\033[m')
print(f'\033[1;36mEstá em minúsculas? {algo.islower()}\033[m')
print(f'\033[1;37mEstá capitalizada? {algo.istitle()}\033[m')
