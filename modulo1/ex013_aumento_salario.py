#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Digite o salário do funcionario: R$'))
novo_salario = salario + (salario * 15 / 100)
print(f'O novo salario do funcionario passa a ser de \033[32mR${novo_salario:.2f}\033[m')
print(f'Um funcionário que ganhava \033[1;31mR${salario:.2f}\033[m, com 15% de aumento, passa a receber \033[1;32mR${salario + (salario * 15 / 100):.2f}\033[m')

produto = float(input('Digite o preço do produto: R$'))
print(f'Se você pagar a vista o preço com 10% de desconto vai ser \033[4;32m{produto - (produto * 10 / 100):.2f}\033[m')
print(f'Se você pagar a prazo o preço com acrescimo de 8% vai ser \033[4;31m{produto + (produto * 8 / 100):.2f}\033[m')