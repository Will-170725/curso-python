# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
# - Abaixo de 18.5: Abaixo do Peso
# - Entre 18.5 e 25: Peso ideal
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade mórbida

peso = float(input('Informe seu peso (Kg): '))
altura = float(input('Informe sua altura (m): '))
imc = peso / (altura ** 2)
print(f'O \033[33mIMC\033[m dessa pessoa é de \033[33m{imc:.1f}\033[m')
if imc < 16:
    print('Você está com \033[31mMAGREZA GRAVE\033[m')
elif imc >= 16 and imc <= 16.9:
    print('Você está com \033[31mMAGREZA MODERADA\033[m')
elif imc >= 17 and imc <= 18.4:
    print('Você está \033[31mABAIXO DO PESO\033[m normal')
elif imc >= 18.5 and imc < 25:
    print('PARABÉNS, você está na faixa de \033[32mPESO IDEAL!\033[m')
elif imc >= 25 and imc < 30:
    print('Você está com \033[31mSOBREPESO!\033[m')
elif imc >= 30 and imc <= 34.99:
    print('Você está com \033[31mOBESIDADE!\033[m')
elif imc > 35 and imc <= 39.99:
    print('Você está com \033[31mOBESIDADE SEVERA!\033[m, cuidado!')
elif imc >= 40:
    print('Você está com \033[31mOBESIDADE MÓRBIDA\033[m, cuidado!')
