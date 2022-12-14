#Exercício 60 – Cálculo do Fatorial

'''Biblioteca para calculo de fatorial
from math import factorial
n = int(input('Digite um número para calcular o seu fatorial: '))
f = factorial(n)
print('O fatorial de {} é {}.'.format(n, f))'''

# Outro modo de escrever o programa manualmente
n = int(input('Digite um número para calcular o seu fatorial: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end='') # Esclamação (!) depois de um número significa fatorial
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}.'.format(f))

