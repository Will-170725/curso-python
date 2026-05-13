# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. Nofinal, mostre os valores em ordem crescente.

valores = [[], []]
numero = 0
for contador in range(0,7):
    numero = int(input(f'Digite um valor o {contador + 1}º valor: '))
    if numero % 2 == 0:
        valores[0].append(numero)
    else:
        valores[1].append(numero)
valores[0].sort()
valores[1].sort()
print(f'Os valores pares digitados foram: {valores[0]}')
print(f'Os valores ímpares digitados foram: {valores[1]}')

# Resolução do professor

número = [[], []]
valor = 0
for contador in range(1, 8):
    valor = int(input(f'Digite o {contador}o. valor: '))
    if valor % 2 == 0:
        número[0].append(valor)
    else:
        número[1].append(valor)
print('-=' * 30)
número[0].sort()
número[1].sort()
print(f'Os valores pares digitados foram: {número[0]}')
print(f'Os valores ímpares digitados foram: {número[1]}')