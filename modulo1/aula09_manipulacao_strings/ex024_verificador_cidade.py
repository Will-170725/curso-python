# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO"

cidade = str(input('\033[1;31mDigite o nome da cidade: \033[m'))
dividido = cidade.split()
print(f'\033[1;33mComeça com o nome "SANTO"? {'SANTO' in dividido[0].upper().strip()}\033[m')

# Solução do professor

cid = str(input('\033[1;97;40mEm que cidade você nasceu: \033[m')).strip()
print(cid[0:5].upper() == 'SANTO')