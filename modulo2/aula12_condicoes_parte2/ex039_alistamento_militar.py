# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# - Se ele ainda vai se alistar ao serviço militar.
# - Se é a hora de se alistar.
# - Se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date
atual = date.today().year
ano = int(input('Ano de nascimento: '))
sexo = str(input('Informe o sexo:\n'
                 '[M] - para masculino\n'
                 '[F] para feminino\n')).strip().upper()
idade = atual - ano
print(f'Quem nasceu em {ano} completa {idade} anos de idade em {atual}.')
if sexo == 'F':
    print('Você não precisa fazer o alistamento militar obrigatório!')
elif sexo == 'M':
    if idade < 18:
        print(f'Você \033[33mainda vai se alistar\033[m ao serviço militar, falta(m) {18 - idade} ano(s) para você se alistar!\n'
              f'Seu alistamento será em {ano + 18}.')
    elif idade == 18:
        print(f'Já é a \033[33mhora de se alistar\033[m, ALISTE-SE AGORA!')
    elif idade > 18:
        print(f'\033[31mVocê já deveria ter se alistado há {idade - 18} ano(s)\033[m.\n'
              f'Seu alistamento foi em {ano + 18}.')

# Resolução do professor:

from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print(f'Quem nasceu em {nasc} tem {idade} ano(s) em {atual}.')
if idade == 18:
    print(f'Você tem que se alistar IMEDIATAMENTE!')
elif idade< 18:
    saldo = 18 - idade
    print(f'Ainda faltam {saldo} ano(s) para o alistamento.')
    ano = atual + saldo
    print(f'Seu alistamento será em {ano}.')
elif idade > 18:
    saldo = idade - 18
    print(f'Você já deveria ter se alistado há {saldo} anos.')
    ano = atual - saldo
    print(f'Seu alistamento foi em {ano}.')
