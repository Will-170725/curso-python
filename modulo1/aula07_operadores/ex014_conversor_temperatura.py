#Escreva um programa que converta uma temperatura digitada em ºC e converta para ºF.

celsius = float(input(f'Informe a temperatura em ºC: '))
fahrenheit = ((9 * celsius) / 5) + 32
print(f'A temperatura  de \033[1;36m{celsius}ºC\033[m corresponde a \033[1;31m{((9 * celsius) / 5) + 32}ºF\033[m')
