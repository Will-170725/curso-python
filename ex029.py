# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre um amensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite

velocidade = float(input('Qual é a velocidade atual do carro? '))
multa = (velocidade - 80) * 7.00
if velocidade > 80:
    print(f'\033[1;31mVocê foi multado em \033[1;33mR${multa:.2f}!\033[m\033[1;31m, por correr {velocidade - 80:.0f} Km acima do limite!\033[m')
print(f'\033[1;32mTenha um bom dia! Dirija com segurança!\033[m')