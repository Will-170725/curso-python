# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

listanome = list()
listanota = list() #dentro da lista nome
boletim = list()
continuar = 'S'
while continuar == 'S':
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    listanome.append(nome)
    listanota.append(nota1)
    listanota.append(nota2)
    listanota.append(media)
    listanome.append(listanota[:])
    listanota.clear()
    continuar = str(input('Deseja continuar? [S/N]: ')).strip().upper()
    while continuar != 'N' and continuar != 'S':
        continuar = str(input('Digite "S" para continuar ou "N" para encerrar: ')).strip().upper()
    boletim.append(listanome[:])
    listanome.clear()
flag = 0
print(f'{"No.":<5}{"Nome":<10}{"Média":<10}')
for dados in boletim:
    print(f'{flag:<5}{dados[0]:<10}{dados[1][2]:.1f}')
    flag += 1
indice = 0
while True:
    indice = int(input('Mostrar notas de qual aluno? (999 Interrompe) '))
    if indice == 999:
        print('Finalizando')
        break
    while indice < 0 or indice >= len(boletim):
        indice = int(input('Digite o indice de um aluno existente: '))
    print(f'Notas de {boletim[indice][0]} são {[boletim[indice][1][0], boletim[indice][1][1]]}')

# Resolução do professor

ficha = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 26)
for i, a in enumerate(ficha): # i = indice, a = aluno
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-' * 35)
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe): ')) # opc = opção
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print('<<< VOLTE SEMPRE >>>')
#print(ficha)
