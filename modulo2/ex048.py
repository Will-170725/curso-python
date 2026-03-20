# Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500.

soma = 0
for contador in range(1, 501):
    if contador % 2 == 1 and contador % 3 == 0:
        soma += contador
print(f'A soma entre todos os números ímpares que são múltiplos de três entre 1 e 500, é: {soma}')

# Resolução do professor

soma = 0
contador = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        contador = contador + 1
        soma += c
print(f'A soma de todos os {contador} valores solicitados é {soma}')
