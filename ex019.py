# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

from random import choice
aluno1 = str(input('\033[1;32mPrimeiro aluno: \033[m'))
aluno2 = str(input('\033[1;33mSegundo aluno: \033[m'))
aluno3 = str(input('\033[1;34mTerceiro aluno: \033[m'))
aluno4 = str(input('\033[1;35mQuarto aluno: \033[m'))
lista = [aluno1, aluno2, aluno3, aluno4]
escolhido = choice(lista)
print(f'\033[1;31mO aluno escolhido foi {escolhido}.\033[m')
