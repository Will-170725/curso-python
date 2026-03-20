#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

nota1 = float(input('Informe a primeira nota: '))
nota2 = float(input('Informe a segunda nota: '))
media =  (nota1 + nota2) / 2
print(f'A media entre \033[1;34m{nota1:.1f}\033[m e \033[1;36m{nota2:.1f}\033[m é \033[1;32m{media:.1f}\033[m')
print(f'A média entre \033[31m{nota1:.1f}\033[m e \033[35m{nota2:.1f}\033[m é igual a \033[33m{(nota1 + nota2) / 2:.1f}\033[m')
