# Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# - Equilátero: todos os lados iguais
# - Isósceles: dois lados iguais
# - Escaleno: todos os lados diferentes

print('-=' * 20)
print('Analisador de Triângulos 2')
print('-=' * 20)
reta1 = float(input('Digite o comprimento da primeira reta: '))
reta2 = float(input('Digite o comprimento da segunda reta: '))
reta3 = float(input('Digite o comprimento da terceira reta: '))
if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('Os seguimentos acima \033[1;32mPODEM FORMAR\033[m um triângulo ', end = '')
    if reta1 == reta2 == reta3:
        print('\033[1;34mEQUILÁTERO!\033[m')
    elif reta1 != reta2 != reta3 != reta1:
        print('\033[1;34mESCALENO!\033[m')
    else:
        print('\033[1;34mISÓSCELES!\033[m')
else:
    print('Os seguimentos acima \033[1;31mNÃO PODEM FORMAR\033[m um triângulo ')

