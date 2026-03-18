# Faça um programa que leia uma frase pelo teclado e mostre:
# Quantas vezes aparece a letra "A".
# Em que posição ela aparece a primeira vez.
# Em que posição ela aparece a última vez.

frase = str(input('Digite uma frase: ').strip()).upper()
print(f'\033[1;34mA letra "A" aparece {frase.count('A')} vez(es)\033[m')
print(f'\033[1;32mA letra "A" aparece pela primeira vez na posição {frase.find('A') + 1}\033[m')
print(f'\033[1;31mA letra "A" aparece pela última vez na posição {frase.rfind('A') + 1}\033[m')
