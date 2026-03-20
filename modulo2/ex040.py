# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# - Média abaixo de 5.0: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
print(f'Tirando {nota1:.1f} e {nota2:.1f}, a média do aluno é {media:.1f}')
if media < 5.0:
    print('\033[1;31mO aluno está REPROVADO.\033[m')
elif media <= 6.9:
    print('\033[1;34mO aluno está em RECUPERAÇÃO.\033[m')
elif media >= 7.0:
    print('\033[1;32mO aluno está APROVADO.\033[m')
else:
    print('\033[1;31mDigite um valor válido.\033[m')