# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# A média de idade do grupo.
# Qual é o nome do homem mais velho.
# Quantas mulheres têm menos de 20 anos.

soma = 0
maior = 0
mulher = 0
velho = ''
for pessoa in range(1, 5):
    print(f'-------------  {pessoa}ª PESSOA -------------')
    nome = str(input('Digite o nome de uma pessoa: ')).strip()
    idade = int(input('Digite a idade dessa pessoa: '))
    sexo = str(input('Digite o sexo dessa pessoa [M/F]: ')).strip().upper()
    soma += idade
    if sexo != 'M' and sexo != 'F':
        print('\033[31mInforme uma opção válida\033[m')
    if pessoa == 1 and sexo == 'M':
        maior = idade
        velho = nome
    if sexo == 'M' and idade >= maior:
        maior = idade
        velho = nome
    elif sexo == 'F' and idade < 20:
        mulher += 1
media = soma / 4
print(f'A \033[34mmédia de idade\033[m desse grupo é {media:.1f} anos')
if velho == '':
    print('Não há homens nesse grupo')
else:
    print(f'{velho} é o homem \033[34mmais velho\033[m com {maior} anos.')
if mulher < 1:
    print(f'Não há mulheres com menos de 20 anos nesse grupo')
elif mulher == 1:
    print(f'{mulher} mulher desse grupo têm \033[34mmenos de 20\033[m anos')
else:
    print(f'{mulher} mulheres desse grupo têm \033[34mmenos de 20\033[m anos')

# Resolução do professor

somaidade = 0
médiaidade = 0
maioridadehomem = 0
nomevelho= ''
totmulher20 = 0
for p in range(1, 5):
    print(f'----- {p}ª PESSOA -----')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in  'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
médiaidade = somaidade / 4
print(f'A média de idade do grupo é de {médiaidade} anos')
print(f'O homem mais velho tem {maioridadehomem} e se chama {nomevelho}.')
print(f'Ao todo são {totmulher20} mulheres com menos de 20 anos')
