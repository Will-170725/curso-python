# Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')
for palavra in palavras:
    tuplavogal = ()
    for letra in palavra:
        if letra in 'aeiou':
            tuplavogal += (letra,)
    vogal = ' '.join(tuplavogal)
    print(f'Na palavra {palavra} temos {vogal}')

# Resolução do professor

palavras = ('aprender', 'programar', 'linguagem', 'python',
            'curso', 'grátis', 'estudar', 'praticar'
            'trabalhar', 'mercado', 'programador', 'futuro')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end = '')
    for letra in p:
        if letra.lower() in 'aáãâeéêiou':
            print(letra, end = ' ')
