# Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
# OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

while True:
    valor = int(input('Digite o valor a ser sacado: R$'))
    while valor < 1:
        print('\033[31mDigite um valor válido\033[m')
        valor = int(input('Digite o valor a ser sacado: R$'))
    saque50 = 0
    saque20 = 0
    saque10 = 0
    saque1 = 0
    if valor >= 50:
        saque50 = valor // 50
        valor = valor % 50
    if valor >= 20:
        saque20 = valor // 20
        valor = valor % 20
    if valor >= 10 :
        saque10 = valor // 10
        valor = valor % 10
    if valor >= 1:
        saque1 = valor
    break
if saque50 > 0:
    print(f'Total de {saque50} cédulas de R$50.00')
if saque20 > 0 :
    print(f'Total de {saque20} cédulas de R$20.00')
if saque10 > 0 :
    print(f'Total de {saque10} cédulas de R$10.00')
if saque1 > 0:
    print(f'Total de {saque1} cédulas de R$1.00')

# Resolução do professor:

print('=' * 30)
print('{:^30}'.format('BANCO CEV'))
print('=' * 30)
valor = int(input('Que valor você quer sacar? R$'))
total = valor
céd = 50
totcéd = 0
while True:
    if total >= céd:
        total -= céd
        totcéd += 1
    else:
        if totcéd > 0:
            print(f'Total de {totcéd} cédulas de R${céd}')
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 1
        totcéd = 0
        if total == 0:
            break
print('=' * 30)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')
