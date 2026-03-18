#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

dias = int(input(f'\033[1;33mQuantos dias alugados? \033[m'))
km = float(input(f'\033[1;35mQuantos Km rodados? \033[m'))
total = (dias * 60) + (km * 0.15)
print(f'\033[1;31mO total a pagar é de R${(dias * 60) + (km * 0.15):.2f}\033[m')
