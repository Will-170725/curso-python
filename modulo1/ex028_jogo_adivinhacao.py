# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep
numero = randint(0, 5) # Faz o computador "PENSAR", na verdade ele sorteia um número entre 0 e 5
print('\033[33m-=-\033[m' * 20)
print('\033[34mVou pensar em um número entre 0 e 5. Tente adivinhar...\033[m')
print('\033[33m-=-\033[m' * 20)
resposta = int(input('Descubra o número escolhido pelo computador: ')) # O jogador tenta adivinhar
print('\033[35mPROCESSANDO...\033[m')
sleep(3)
if resposta == numero:
    print('\033[1;32mPARABÉNS você venceu!\033[m')
else:
    print(f'\033[1;31mGANHEI! Eu pensei no número {numero} e não no {resposta}!\033[m')
