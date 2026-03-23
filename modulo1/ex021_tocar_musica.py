# Faça um programa em Python que abra e reproduza o audio de um arquivo mp3.

import pygame
pygame.mixer.init()
pygame.mixer.music.load('../johnnycash-hurt.mp3') # Coloque um arquivo mp3 na pasta para funcionar
pygame.mixer.music.play()
input()
