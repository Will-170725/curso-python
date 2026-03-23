# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
# Ex: Ana Maria de Souza
# primeiro = Ana
# último = Souza

nome = str(input('Digite seu nome completo: ')).strip()
dividido = nome.split()
print('\033[1;32mMuito prazer em te conhecer!\033[m')
print(f'\033[1;36mPrimeiro nome: {dividido[0]}\033[m')
print(f'\033[1;34mÚltimo nome: {dividido[-1]}\033[m') # O professor utilizou "dividido[len(dividido) - 1]"
