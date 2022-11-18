#ex038 – Comparando números
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
if n1 > n2:
    print('\033[0;31mO PRIMEIRO número é maior!')
elif n2 > n1:
    print('\033[0;32mO SEGUNDO número é maior!')
else:
    print('\033[0;33mOs dois números são iguais.')

