# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint
contador = 0
while True:
    jogador = str(input('Par ou ímpar?[P/I] ')).strip().upper()
    while jogador != 'P' and jogador != 'I':
        print(f'\033[31;1mEscolha P (par) ou I (ímpar)\033[m')
        jogador = str(input('Par ou ímpar?[P/I] ')).strip().upper()
    jogador2 = int(input('Escolha um número entre 0 e 10: '))
    while jogador2 > 10 or jogador2 < 0 :
        print(f'\033[31;1mEscolha um número válido entre 0 e 10\033[m')
        jogador2 = int(input('Escolha um número entre 0 e 10: '))
    computador = randint(0, 10)
    par = (computador + jogador2) % 2 == 0
    impar = (computador + jogador2) % 2 == 1
    if par and jogador == 'P':
        print(f'\033[32mVocê escolheu par, e jogou o número {jogador2}, eu joguei {computador}, portanto é par, parabéns você venceu!\033[m')
        contador += 1
    elif impar and jogador == 'I':
        print(f'\033[32mVocê escolheu ímpar, e jogou o número {jogador2}, eu joguei {computador}, portanto é ímpar, parabéns você venceu!\033[m')
        contador += 1
    elif impar and jogador == 'P':
        print(f'\033[31mVocê escolheu par, e jogou o número {jogador2}, eu joguei {computador}, portanto é ímpar, você perdeu.\033[m')
        break
    elif par and jogador == 'I':
        print(f'\033[31mVocê escolheu ímpar, e jogou o número {jogador2} eu joguei {computador}, portanto é par, você perdeu.\033[m')
        break
if contador > 1:
    print(f'\033[32;1mPARABÉNS você venceu {contador} vezes antes de perder!')
elif contador == 1:
    print(f'\033[32mVocê venceu {contador} vez antes de perder, parabéns.')
else:
    print(f'Você não venceu nenhuma vez antes de perder, desejo mais sorte da próxima vez.')

# Resolução do professor

from random import randint
v = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total} ', end = '')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {v} vezes.')
