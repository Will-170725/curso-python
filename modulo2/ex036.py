# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ele não pode exceder 30% do salário ou então o empréstimo será negado.

casa = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual o salário do comprador? R$'))
anos = int(input('Em quantos anos você pretende pagar? '))
prestacao = casa / (anos * 12)
limite = salario * (30 / 100)
print(f'Você terá de pagar R${prestacao:.2f} por mês, em {anos} anos')
if prestacao <= limite:
    print(f'Empréstimo bancário no valor de R${prestacao:.2f}, CONCEDIDO!')
else:
    print(f'Empréstimo NEGADO!')
