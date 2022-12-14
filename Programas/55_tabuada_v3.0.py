# Exercício 67 – Tabuada v3.0
while True:
    n = int(input('A tabuada de qual valor você quer ver? '))
    print('-' * 30)
    if n < 0:
        break
    for c in range(1, 11):
        print('{} x {} = {}'.format(n, c, n*c))
    print('-' * 30)
print('PROGRAMA ENCERRADO! Volte sempre.')
