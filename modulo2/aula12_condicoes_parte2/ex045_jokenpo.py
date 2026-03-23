# Crie um programa que faça o computador jogar Jokenpô com você.

from random import randint
itens = ('PEDRA', 'PAPEL', 'TESOURA')
jogador = int(input('''Informe um número:
[ 0 ] - Pedra
[ 1 ] - Papel
[ 2 ] - Tesoura
Qual é a sua jogada? '''))
computador = randint(0, 2)
if jogador == 0 and computador == 2 or jogador == 1 and computador == 0 or jogador == 2 and computador == 1:
    print(f'\033[32mEu escolhi {itens[computador]}, PARABÉNS VOCÊ VENCEU!\033[m')
elif jogador == 0 and computador == 1 or jogador == 1 and computador == 2 or jogador == 2 and computador == 0:
    print(f'\033[31mEu escolhi {itens[computador]}, VOCÊ PERDEU!\033[m')
elif jogador == 0 and computador == 0 or jogador == 1 and computador == 1 or jogador == 2 and computador == 2:
    print(f'\033[34mEu escolhi {itens[computador]}, PORTANTO FOI EMPATE!\033[m')
else:
    print('\033[1;31mDigite um número válido de 1 à 3\033[m')

# Resolução do professor

from random import randint
from time import sleep
import emoji
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
if jogador != 0 and jogador != 1 and jogador != 2:
    print(emoji.emojize(emoji.emojize('\033[31mJOGADA INVÁLIDA!\033[m :disappointed_face:')))
else:
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO!!!')
    print('-=' * 15)
    print(f'O computador escolheu {itens[computador]}')
    print(f'O jogador escolheu {itens[jogador]}')
    print('-=' * 15)
    if computador == 0: # Computador jogou PEDRA
        if jogador == 0:
            print(emoji.emojize('EMPATE :anguished_face:'))
        elif jogador == 1:
            print(emoji.emojize('\033[32mJOGADOR VENCE\033[m :1st_place_medal:'))
        elif jogador == 2:
            print(emoji.emojize('\033[31mCOMPUTADOR VENCE\033[m :angry_face:'))
        else:
            print(emoji.emojize('\033[31mJOGADA INVÁLIDA!\033[m'))
    elif computador == 1: # Computador jogou PAPEL
        if jogador == 0:
            print(emoji.emojize('\033[31mCOMPUTADOR VENCE\033[m :crying_cat:'))
        elif jogador == 1:
            print(emoji.emojize('EMPATE :anxious_face_with_sweat:'))
        elif jogador == 2:
            print(emoji.emojize('\033[32mJOGADOR VENCE\033[m :beaming_face_with_smiling_eyes:'))
        else:
            print('\033[31mJOGADA INVÁLIDA!\033[m')
    elif computador == 2: # Computador jogou TESOURA
        if jogador == 0:
            print(emoji.emojize('\033[32mJOGADOR VENCE\033[m :cat_with_tears_of_joy:'))
        elif jogador == 1:
            print(emoji.emojize('\033[31mCOMPUTADOR VENCE\033[m :crying_face:'))
        elif jogador == 2:
            print(emoji.emojize('EMPATE :astonished_face:'))
        else:
            print('\033[31mJOGADA INVÁLIDA!\033[m')
