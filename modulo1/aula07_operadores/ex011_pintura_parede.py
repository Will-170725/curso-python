#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².

largura = float(input('Digite a largura da parede em metros: '))
altura = float(input('Digite a altura da parede em metros: '))
area = largura * altura
tinta = area / 2
print(f'A área dessa parede é \033[32m{area}\033[m metros², e a quantidade de tinta necessária para pintá-la é \033[31m{tinta}\033[m litros')
print(f'Sua parede tem a dimensão de \033[1;33m{largura}\033[mx\033[1;34m{altura}\033[m e sua área é de \033[1;32m{largura * altura}m²\033[m')
print(f'Para pintar essa parede você precisará de \033[1;31m{area / 2}l\033[m de tinta')