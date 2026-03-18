#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.
#Considere US$1,00 = R$3,27 (03/07/2017)

dinheiro = float(input('Digite quanto dinheiro você tem na carteira: R$'))
dolar = dinheiro / 3.27
print(f'Com \033[1;31mR${dinheiro:.2f}\033[m, você pode comprar \033[1;32mUS${dolar:.2f}\033[m')
print(f'Com \033[34mR${dinheiro:.2f}\033[m, você pode comprar \033[32mUS${dinheiro / 5.30:.2f}\033[m, \033[33m€{dinheiro / 6.16:.2f}\033[m, e \033[35m¥{dinheiro / 0.03427:.2f}\033[m')
