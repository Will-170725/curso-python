# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

expressao = []
string = str(input('Digite a expressão: '))
for caractere in string:
    expressao.append(caractere)
contador = 0
for caractere in expressao:
    if caractere == '(':
        contador += 1
    if caractere == ')':
        contador -= 1
    if contador < 0:
        print('Sua expressão está errada!')
        break
if contador >= 0:
    if contador == 0:
        print('Sua expressão está válida!')
    elif contador > 0:
        print('Sua expressão está errada!')

# Resolução do professor

expr = str(input('Digite a expressão: '))
pilha = []
for símb in expr:
    if símb == '(':
        pilha.append('(')
    elif símb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')
