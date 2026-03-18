#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa

from math import hypot
cateto_oposto = float(input('\033[1;33mComprimento do cateto oposto: \033[m'))
cateto_adjacente = float(input('\033[1;32mComprimento do cateto adjacente: \033[m'))
hipotenusa = (cateto_oposto ** 2 + cateto_adjacente ** 2) ** (1/2)
print(f'\033[1;34mA hipotenusa vai medir {hipotenusa:.2f}\033[m')
hipotenusa2 = hypot(cateto_oposto, cateto_adjacente)
print(f'\033[1;36mA hipotenusa vai medir {hipotenusa2:.2f}\033[m')
