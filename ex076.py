# Crie um programa que tenha uma tupla única com nomes de produtos e seua respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.

listagem = ('Pão', 1, 'Leite', 3.50, 'Frango', 10.90, 'Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.90, 'Estojo', 25, 'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)

print('-' * 40)
print(f'{'LISTAGEM DE PREÇOS':^40}')
print('-' * 40)
for indice in range(0, len(listagem), 2):
    print(f'{listagem[indice]:.<30}R$ {listagem[indice + 1]:>.2f}')
print('-' * 40)

# Resolução do professor

listagem = ('Lápis', 1.75,
            'Borracha', 2,
            'Caderno', 15.90,
            'Estojo', 25,
            'Transferidor', 4.20,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Canetas', 22.30,
            'Livro', 34.90)
# print(listagem)
# for item in listagem:
#     print(item)
print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end = '')
    else:
        print(f'R${listagem[pos]:>7.2f}')
print('-' * 40)
