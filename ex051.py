# Desenvolva um programa que leia o primeiro termo e a razão de uma PA(Progressão Aritmética). No final, mostre os 10 primeiros termos dessa progressão.

termo = int(input('Digite o primeiro termo da Progressão Aritmética: '))
razao = int(input('Digite a razão dessa PA: '))
for contador in range(termo, termo + (10 * razao), razao):
    print(f'{contador} ', end = '→ ')
print('Acabou')

# Resolução do professor

primeiro = int(input('\nPrimeiro termo: '))
razão = int(input('Razão: '))
décimo = primeiro + (10 - 1) * razão
for c in range(primeiro, décimo + razão, razão):
    print(f'{c} ', end = '→ ')
print('ACABOU')
