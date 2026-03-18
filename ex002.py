#Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas.

nome = input('\033[1;34mDigite seu nome: \033[m')
print('\033[1;36mÉ um prazer te conhecer,', nome + '!\033[m')
print('\033[36mÉ um prazer te conhecer, {}!\033[m'.format(nome))
print(f'\033[1;36mÉ um prazer te conhecer, {nome}!\033[m')
