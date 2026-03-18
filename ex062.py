# Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos.

termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
contador = 1
while contador < 11:
    decimo = termo + (contador - 1) * razao
    print(f'{decimo} ', end = '→ ')
    contador += 1
print('PAUSA')
quantidade = 1
contador2 = contador
while quantidade != 0:
    quantidade = int(input('Você quer mostrar mais quantos termos? [0 para encerrar] '))
    contador2 += quantidade
    while contador < contador2:
        decimo = termo + (contador - 1) * razao
        print(f'{decimo} ', end = '→ ')
        contador += 1
    if quantidade > 0:
        print('PAUSA')
print('ACABOU')

# Resolução do professor

print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print(f'{termo} → ', end = '')
        termo += razão
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print(f'Progressão finalizada com {total} termos mostrados.')
