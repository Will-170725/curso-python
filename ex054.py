# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date
menor = 0
maior = 0
for pessoa in range(1, 7 + 1):
    ano = int(input(f'Digite o {pessoa}º ano de nascimento: '))
    if ano + 21 > date.today().year:
        menor += 1
    elif ano + 21 <= date.today().year:
        maior += 1
if menor == 1:
    print(f'Das 7 pessoas digitadas, {menor} ainda não atingiu a maioridade')
else:
    print(f'Das 7 pessoas digitadas, {menor} ainda não atingiram a maioridade.')
if maior == 1:
    print(f'Das 7 pessoas digitadas, {maior} já é maior de idade')
else:
    print(f'Das 7 pessoas digitadas, {maior} já são maiores de idade.')

#Resolução do professor

from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1, 8):
    nasc = int(input(f'Em que ano a {pess}ª pessoa nasceu? '))
    idade = atual - nasc
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print(f'Ao todo tivemos {totmaior} pessoas maiores de idade')
print(f'E também tivemos {totmenor} pessoas menores de idade')
