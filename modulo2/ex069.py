# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) Quantos homens foram cadastrados.
# C) Quantas mulheres tem menos de 20 anos.

contadoridade = 0
contadorhomem = 0
contadormulher = 0
while True:
    idade = int(input('Digite a idade da pessoa: '))
    while idade < 0 or idade > 150:
        print('\033[31mDigite uma idade válida\033[m')
        idade = int(input('Digite a idade da pessoa: '))
    if idade > 18:
        contadoridade += 1
    sexo = str(input('Digite o sexo da pessoa [M/F]: ')).strip().upper()
    while sexo != 'M' and sexo != 'F':
        print('\033[31mDigite M para masculino ou F para feminino\033[m')
        sexo= str(input('Digite o sexo da pessoa: ')).strip().upper()
    if sexo == 'M':
        contadorhomem += 1
    if sexo == 'F' and idade < 20:
        contadormulher += 1
    continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()
    while continuar != 'S' and continuar != 'N':
        print('\033[31mDigite S para sim ou N para não\033[m')
        continuar = str(input('Deseja continuar? ')).strip().upper()
    if continuar == 'N':
        break
if contadoridade < 1:
    print('Nenhuma pessoa tem mais de 18 anos.')
elif contadoridade == 1:
    print(f'{contadoridade} pessoa tem mais de 18 anos.')
else:
    print(f'{contadoridade} pessoas tem mais de 18 anos.')
if contadorhomem < 1:
    print(f'Nenhum homem foi cadastrado')
elif contadorhomem == 1:
    print(f'{contadorhomem} homem foi cadastrado.')
else:
    print(f'{contadorhomem} homens foram cadastrados.')
if contadormulher < 1:
    print('Nenhuma mulher tem menos de 20 anos.')
elif contadormulher == 1:
    print(f'{contadormulher} mulher tem menos de 20 anos')
else:
    print(f'{contadormulher} mulheres tem menos de 20 anos.')

# Resolução do professor

tot18 = totH = totM20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        totH += 1
    if sexo == 'F' and idade < 20:
        totM20 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'Ao todo temos {totH} homens cadastrados')
print(f'E temos {totM20} mulheres com menos de 20 anos')
