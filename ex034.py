# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1.250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%

salario = float(input('Informe o salario: R$'))
if salario > 1250:
    print(f'Com o aumento de 10% o funcionário passa a ganhar \033[32mR${salario + (salario * 0.1):.2f}\033[m.')
else:
    print(f'Com o aumento de 15% o funcionário passa a ganhar \033[1;32mR${salario + (salario * 0.15):.2f}\033[m.')

# Resolução do professor
salário = float(input('Qual é o salário do funcionário? R$ '))
if salário <= 1250:
    novo = salário + (salário * 15 / 100)
else:
    novo = salário + (salário * 10 / 100)
print(f'Quem ganhava \033[31mR${salário:.2f}\033[m passa a ganhar \033[1;32mR${novo:.2f}\033[m agora.')