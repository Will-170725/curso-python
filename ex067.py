# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.

while True:
    numero = int(input('Quer a tabuada de que valor? '))
    if numero < 0:
        break
    print('-' * 20)
    contador = 0
    while contador < 10:
        contador += 1
        tabuada = numero * contador
        print(f'{numero:^} x {contador:^} = {tabuada:^}')
    print('-' * 20)
print('FIM')

# Resolução do professor

while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 30)
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} x {c} = {n * c}')
    print('-' * 30)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
