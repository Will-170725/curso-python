# A confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre a sua categoria, de acordo com a idade:
# - Até 9 anos: MIRIM
# - Até 14 anos: INFANTIL
# - Até 19 anos: JUNIOR
# - Até 20 anos: SÊNIOR
# - Acima: MASTER

from datetime import date
ano = int(input('Informe o ano de nascimento do atleta: '))
idade = date.today().year - ano
print(f'O atelta tem \033[33m{idade} anos\033[m')
if idade <= 9:
    print(f'Sua categoria é \033[34mMIRIM\033[m')
elif idade <= 14:
    print(f'Sua categoria é \033[34mINFANTIL\033[m')
elif idade <= 19:
    print(f'Sua categoria é \033[34mJUNIOR\033[m')
elif idade <= 20:
    print(f'Sua categoria é \033[34mSÊNIOR\033[m')
elif idade > 20:
    print(f'Sua categoria é \033[34mMASTER\033[m')
