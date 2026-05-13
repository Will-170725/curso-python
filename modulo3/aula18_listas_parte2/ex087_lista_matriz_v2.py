# Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

valores = list()
linhatemporaria = list()
soma = 0
soma2 = 0
maior = 0
for linha in range(0,3):
    for coluna in range(0,3):
        valor = int(input(f'Digite um valor para {[linha, coluna]}: '))
        linhatemporaria.append(valor)
    valores.append(linhatemporaria[:])
    linhatemporaria.clear()
for linha in valores:
    for valor in linha:
        if valor % 2 == 0:
            soma += valor
        print(f'[{valor:^5}] ', end='')
    print()
    soma2 += linha[2]
for coluna in range(0, 3):
    if coluna == 0:
        maior == valores[1][coluna]
    elif valores[1][coluna] > maior:
        maior = valores[1][coluna]
print(f'A soma de todos os valores pares digitados é igual a {soma}.')
print(f'A soma dos valores da terceira coluna é igual a {soma2}.')
print(f'O maior valor da segunda linha é {maior}.')

# Resolução do professor

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = mai = scol = 0 # spar = soma dos pares, mai = maior valor, scol = soma da coluna
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l] [c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
    print()
print('-=' * 30)
print(f'A soma dos valores pares é {spar}')
for l in range(0, 3):
    scol += matriz[l][2]
print(f'A soma dos valores da terceira coluna é {scol}.')
for c in range(0, 3):
    if c == 0:
        mai = matriz[1][c]
    elif matriz[1][c] > mai:
        mai = matriz[1][c]
print(f'O maior valor da segunda linha é {mai}.')
