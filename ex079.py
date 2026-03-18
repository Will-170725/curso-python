# Crie um ´programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

valores = []
continuar = 'S'
while continuar == 'S':
    valor = int(input('Digite um valor: '))
    if valor in valores:
        print('Valor duplicado! Não vou adicionar...')
    else:
        valores.append(valor)
    continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()
    while continuar != 'S' and continuar != 'N':
        continuar = str(input('Digite "S" para continuar ou "N" para parar: ' )).strip().upper()
valores.sort()
print(f'Você digitou os valores {valores}')

# Resolução do profesor

números = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in números:
        números.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    r = str(input('Quer continuar? [S/N] '))
    if r in 'Nn':
        break
print('-=' * 30)
números.sort()
print(f'Você digitou  os valores {números}')
