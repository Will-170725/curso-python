# Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
# - O primeiro valor é maior
# - O segundo valor é maior
# - Não existe valor maior, os dois são iguais

numero1 = int(input('Digite o primeiro número inteiro: '))
numero2 = int(input('Digite o segundo número inteiro: '))
if numero1 > numero2:
    print('O \033[33mPRIMEIRO\033[m valor é \033[34mmaior\033[m')
elif numero2 > numero1:
    print('O \033[33mSEGUNDO\033[m valor é \033[34mmaior\033[m')
else:
    print('\033[33mNÃO EXISTE\033[m valor maior, os dois valores são \033[34mIGUAIS\033[m')
