# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# - 1 para binário
# - 2 para octal
# - 3 para hexadecimal


numero = int(input('Digite um número inteiro: '))
print('Escolha uma \033[34mbase de conversão:\033[m')
opcao = int(input('''Digite:
\033[34m[ 1 ]\033[m - para \033[33mBINÁRIO\033[m
\033[34m[ 2 ]\033[m - para \033[33mOCTAL\033[m
\033[34m[ 3 ]\033[m - para \033[33mHEXADECIMAL\033[m
Sua opção: '''))
if opcao == 1:
    print(f'O número {numero} convertido para \033[33mBINÁRIO\033[m é igual a {bin(numero)[2:]}.')
elif opcao == 2:
    print(f'O número {numero} convertido para \033[33mOCTAL\033[m é igual a {oct(numero)[2:]}.')
elif opcao == 3:
    print(f'O número {numero} convertido para \033[33mHEXADECIMAL\033[m é igual a {hex(numero)[2:]}.')
else:
    print(f'\033[31mDigite uma opção válida entre 1 e 3\033[m')