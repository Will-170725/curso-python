#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
#R$10 = 100%
# x   =  5%
#10 * 5 / 100 = 0.5
#1500 * 10 / 100 = 150.0
#875 * 15 / 100 = 131.25

preco = float(input('Digite o preço do produto: R$'))
desconto = preco - (preco * 5 / 100)
print(f'O preco do produto com desconto é \033[32mR${desconto:.2f}\033[m')
print(f'O produto que custava \033[1;31mR${preco:.2f}\033[m, na promoção com desconto de 5% vai custar \033[1;32mR${preco - (preco * 5 / 100):.2f}\033[m')
