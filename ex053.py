# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
# APOS A SOPA
# A SACADA DA CASA
# A TORRE DA DERROTA
# O LOBO AMA O BOLO
# ANOTARAM A DATA DA MARATONA

frase = ''.join(str(input('Digite uma frase: ')).upper().split())
contrario = ''
for letra in range(len(frase) -1, -1, -1):
    contrario = contrario + frase[letra]
print(f'{frase} ao contrario é {contrario}')
if contrario == frase:
    print('\033[32mA frase digitada é um palíndromo!\033[m')
else:
    print('\033[31mA frase digitada não é um palindromo!\033[m')

# Resolução do professor

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
'''inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]'''
print(f'O inverso de {junto} é {inverso}')
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')
