#Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros.
#km hm dam m dm cm mm

metros = float(input('Digite uma distância em metros: '))
centimetros = metros * 100
milimetros = metros * 1000
print(f'O valor em metros informado foi \033[1;32m{metros}\033[mm, convertido para: \ncentimetros é \033[1;36m{centimetros:.0f}\033[mcm \nmilimetros é \033[1;34m{milimetros:.0f}\033[mmm')
print(f'A medida de \033[31m{metros}\033[mm corresponde a: \n\033[32m{metros * 0.001}\033[mkm \n\033[33m{metros * 0.01}\033[mhm \n\033[34m{metros * 0.1:.1f}\033[mdam \n\033[35m{metros * 10:.0f}\033[mdm \n\033[36m{metros * 100:.0f}\033[mcm \n\033[37m{metros * 1000:.0f}\033[mmm')