# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

continuar = 'S'
flag = 0
soma = 0
while continuar == 'S':
    numero = int(input('Digite um número: '))
    soma += numero
    flag += 1
    if flag == 1:
        maior = numero
        menor = numero
    else:
        if numero >= maior:
            maior = numero
        if numero <= menor:
            menor = numero
    continuar = str(input('Deseja continuar? [S/N]: ')).strip().upper()
    while continuar != 'N' and continuar != 'S':
        print('Digite S para continuar ou N para encerrar')
        continuar = str(input('Deseja continuar? [S/N]: ')).strip().upper()
media = soma / flag
print(f'''
A média entre todos os valores digitados é {media:.2f}
O maior valor digitado foi {maior}
O menor valor digitado foi {menor}
''')

# Resolução do professor

resp = 'S'
soma = quant = média = 0
while resp in 'Ss':
    núm = int(input('Digite um número: '))
    soma += núm
    quant += 1
    if quant == 1:
        maior = menor = núm
    else:
        if núm > maior:
            maior = núm
        if núm < menor:
            menor = núm
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
média = soma / quant
print(f'Você digitou {quant} números e a média foi {média}')
print(f'O maior valor foi {maior} e o menor foi {menor}')
