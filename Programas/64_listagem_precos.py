'''Exercício 076
Crie um programa que tenha uma tupla única com nomes de produtos
e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando
os dados em forma tabular.'''

listagem = ('Lápis', 0.80,
            'Caneta', 1.50,
            'Caderno', 20,
            'Borracha', 0.50,
            'Marca texto', 4.60,
            'Mochila', 50,
            'Livros', 300,
            'Estojo', 3.75)
print('-' * 40)
print('LISTAGEM DE PREÇOS')
print('-' * 40)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print('{:.<30}'.format(listagem[pos]), end='')
    else:
        print('R${:>7.2f}'.format(listagem[pos]))
print('-' * 40)