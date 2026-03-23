# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# - À vista dinheiro/cheque: 10% de desconto
# - À vista no cartão: 5% de desconto
# - Em até 2x no cartão: preço normal
# - 3x ou mais no cartão: 20% de juros

print(f'{' LOJAS GUANABARA ':=^40}')
preco = float(input('Informe o preço das compras: R$'))
condicao = int(input('''Informe a condição de pagamento: 
[ 1 ] - À vista \033[34mdinheiro/cheque\033[m
[ 2 ] - À vista no \033[34mcartão\033[m
[ 3 ] - Em até \033[34m2x no cartão\033[m
[ 4 ] - \033[34m3x ou mais\033[m no cartão
Qual é a opção? '''))
if condicao == 1:
    print(f'O valor a ser pago com \033[32m10%\033[m de desconto é R${preco - (preco * 10 / 100):.2f}')
elif condicao == 2:
    print(f'O valor a ser pago com \033[32m5%\033[m de desconto é R${preco - (preco * 5 / 100):.2f}')
elif condicao == 3:
    print(f'Sua compra será parcelada em 2x de R${preco / 2:.2f}')
    print(f'O valor a ser pago é R${preco:.2f}')
elif condicao == 4:
    parcela = int(input('Quantas parcelas? '))
    print(f'Sua compra será parcelada em {parcela:}x de R${(preco + (preco * 20 / 100)) / parcela:.2f} COM JUROS')
    print(f'O valor a ser pago com \033[31m20%\033[m de juros é R${preco + (preco * 20 / 100):.2f}')
else:
    print('\033[1;31mEscolha uma condição válida\033[m')

# Resolução do professor

print(f'{' LOJAS GUANABARA ':=^40}')
preço = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opção = int(input('Qual é a opção? '))
if opção == 1:
    total = preço - (preço * 10 / 100)
elif opção == 2:
    total = preço - (preço * 5 / 100)
elif opção == 3:
    total = preço
    parcela = total / 2
    print(f'Sua compra será parcelada em 2x de R${parcela:.2f} SEM JUROS')
elif opção == 4:
    total = preço + (preço * 20 / 100)
    total_parcelas = int(input('Quantas parcelas? '))
    parcela = total / total_parcelas
    print(f'Sua compra será parcelada em {total_parcelas}x de R${parcela:.2f} COM JUROS')
else:
    total = preço
    print(f'\033[31mOPÇÃO INVÁLIDA de pagamento. Tente novamente!\033[m')
print(f'Sua compra de R${preço:.2f} vai custar R${total:.2f} no final.')
