#Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.

numero = int(input('\033[1;34mDigite um número inteiro: \033[m'))
sucessor = numero + 1
antecessor = numero - 1
print(f'Analisando o valor \033[1;32m{numero}\033[m, seu antecessor é \033[1;34m{antecessor}\033[m, e seu sucessor é \033[1;36m{sucessor}\033[m.')
print(f'Analisando o valor \033[1;33m{numero}\033[m, seu antecessor é \033[1;31m{numero - 1}\033[m, e seu sucessor é \033[1;35m{numero + 1}\033[m.')