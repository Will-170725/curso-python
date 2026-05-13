# Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
# No final, mostre a matriz na tela, com a formatação correta.

valores = list()
linhatemporaria = list()
for linha in range(0, 3):
    for coluna in range(0,3):
        valor = int(input(f'Digite um valor para {[linha, coluna]}: '))
        linhatemporaria.append(valor)
    valores.append(linhatemporaria[:])
    linhatemporaria.clear()
for linha in valores:
    for valor in linha:
        print(f'[{valor:^5}] ', end = '')
    print()

# Resolução do professor

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3): # l de linha
    for c in range(0, 3): # c de coluna
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
#print(matriz)
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
