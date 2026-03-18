# Crie um programa que leia dois valores e mostre um menu na tela:
# [1] somar
# [2] multiplicar
# [3] maior
# [4] novos números
# [5] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

from time import sleep
numero1 = int(input('Digite o primeiro valor: '))
numero2 = int(input('Digite o segundo valor: '))
menu = 0
while menu != 5:
    print('''----- MENU -----
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa''')
    menu = int(input('>>>>> Escolha uma das opções: '))
    if menu == 1:
        soma = numero1 + numero2
        print(f'A soma entre {numero1} e {numero2} é igual a {soma}')
    elif menu == 2:
        multiplicacao = numero1 * numero2
        print(f'{numero1} multiplicado por {numero2} é igual a {multiplicacao}')
    elif menu == 3:
        # O professor fez
        # if n1 > n2
        #   maior = n1
        # else:
        #   maior = n2
        # print(f'Entre {n1} e {n2} o maior valor é {maior}')
        if numero1 > numero2:
            print(f'{numero1} é maior que {numero2}')
        elif numero2 > numero1:
            print(f'{numero2} é maior que {numero1}')
        else:
            print('Os dois números são iguais')
    elif menu == 4:
        print('Informe os números novamente:')
        numero1 = int(input('Digite o primeiro valor: '))
        numero2 = int(input('Digite o segundo valor: '))
    elif menu == 5:
        print('Finalizando...')
    else:
        print(f'\033[31mEscolha uma opção válida!\033[m')
    print('=-=' * 10)
    sleep(2)
print('Fim do programa! Volte sempre!')
