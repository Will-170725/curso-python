#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

numero = int(input('Digite um número: '))
dobro = numero * 2
triplo = numero * 3
raiz = numero ** (1/2)
print(f'O dobro de \033[1;32m{numero}\033[m, é \033[1;31m{dobro}\033[m.')
print(f'O triplo de \033[1;33m{numero}\033[m, é \033[1;34m{triplo}\033[m.')
print(f'A raiz quadrada de \033[1;35m{numero}\033[m, é \033[1;36m{raiz:.2f}\033[m.')

print(f'O dobro de \033[36m{numero}\033[m vale \033[35m{numero * 2}\033[m.')
print(f'O triplo de \033[34m{numero}\033[m vale \033[33m{numero * 3}\033[m. \nA raiz quadrada de \033[31m{numero}\033[m é igual a \033[32m{pow(numero, (1/2)):.2f}\033[m.')
