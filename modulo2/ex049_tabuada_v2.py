# Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

numero = int(input('Digite um número: '))
for contador in range(1, 11):
    tabuada = numero * contador
    print(f'{numero} x {contador:2} = {tabuada}')

# Resolução do professor

num = int(input('Digite um número para ver sua tabuada: '))
for c in range(1, 11):
    print(f'{num} x {c:2} = {num * c}')
