# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle
aluno1 = str(input('\033[1;33mDigite o nome do primeiro aluno: \033[m'))
aluno2 = str(input('\033[1;34mDigite o nome do segundo aluno: \033[m'))
aluno3 = str(input('\033[1;35mDigite o nome do terceiro aluno: \033[m'))
aluno4 = str(input('\033[1;36mDigite o nome do quarto aluno: \033[m'))
lista = [aluno1, aluno2, aluno3, aluno4]
shuffle(lista)
print('\033[1;31mA ordem de apresentação será\033[m')
print(lista)
