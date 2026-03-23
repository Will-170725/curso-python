# Melhore o jogo do desafio 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint
palpite = 1
numero = randint(0, 10)
print('\033[33m-=-\033[m' * 20)
print('\033[34mVou pensar em um número entre 0 e 10. Tente adivinhar...\033[m')
print('\033[33m-=-\033[m' * 20)
resposta = int(input('O número que você pensou foi: '))
print('\033[35mPROCESSANDO...\033[m')
while resposta != numero:
    palpite += 1
    print(f'\033[1;31mNÃO!\033[m')
    resposta = int(input('...Foi: '))
    print('\033[35mPROCESSANDO...\033[m')
print('\033[1;32mPARABÉNS você venceu!\033[m')
if palpite == 1:
    print(f'Foi necessário apenas {palpite} palpite para vencer, parabéns')
else:
    print(f'Foram necessários {palpite} palpites para vencer')

# Resolução do professor

from random import randint
computador = randint(0, 10)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi? ')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        elif jogador > computador:
            print('Menos... Tente mais uma vez.')
print(f'Acertou! com {palpites} tentativas. Parabéns!')
