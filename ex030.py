# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

numero = int(input('\033[35mDigite um número inteiro: \033[m'))
if numero % 2 == 0:
    print(f'O número {numero} é \033[34mPAR\033[m')
else:
    print(f'O número {numero} é \033[34mÍMPAR\033[m')

# Resoluição do profesor
número = int(input('\033[35mMe diga um número: \033[m'))
resultado= número % 2
if resultado == 0:
    print(f'O número {número} é \033[34mPAR\033[m')
else:
    print(f'O número {número} é \033[34mÍMPAR\033[m')
