# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça digitação novamente até ter um valor correto.

sexo = str(input(f'Digite o sexo da pessoa [M/F]: ')).strip().upper()[0]
while sexo != 'M' and sexo != 'F':
    print('\033[31mDados inválidos, por favor digite novamente \033[m')
    sexo = str(input(f'Digite o sexo da pessoa [M/F]: ')).strip().upper()[0]
if sexo == 'M':
    print('Sexo masculino registrado corretamente.')
elif sexo == 'F':
    print('Sexo feminino registrado corretamente.')

# Resolução do profesor

sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]
print(f'Sexo {sexo} registrado com sucesso')
