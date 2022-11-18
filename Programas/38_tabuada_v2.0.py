#Ex 049 – Tabuada v.2.0
n = int(input('Digite um número para ver a sua tabuada: '))
for c in range(1, 11):
    print('{} x {} = {}'.format(n, c, n*c))
