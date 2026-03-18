# Desenvolva um programa que pergunte a distância de uma viagem em KM. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.

distancia = float(input('Informe a distância da viagem em Km: '))
if distancia <= 200:
    print(f'Uma viagem de \033[31m{distancia:.0f}Km\033[m custará \033[1;31mR${distancia * 0.50:.2f}\033[m.')
else:
    print(f'Uma viagem de \033[32m{distancia:.0f}Km\033[m custará \033[1;32mR${distancia * 0.45:.2f}\033[m')

# Resolução do professor
distância = float(input('Qual é a distância da sua viagem? '))
print(f'Você está prestes a começar uma viagem de \033[31m{distância}Km\033[m.')
# if distância <= 200:
#     preço = distância * 0.50
# else:
#     preço = distância * 0.45
preço = distancia * 0.50 if distância <= 200 else distância * 0.45
print(f'E o preço da sua passagem será de \033[1;31mR${preço:.2f}\033[m')
