# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

nome = str(input('\033[1;36mDigite seu nome: \033[m')).strip()
print(f'\033[1;34mTem o nome "SILVA"? {'SILVA' in nome.upper()}\033[m')