'''Exercício 77 – Contando vogais em Tupla
Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.'''

palavras = ('Palavras', 'Curso', 'Programação', 'Carro',
            'Bicicleta', 'Trabalho', 'Familia', 'Estudar',
            'Maquina', 'Programador', 'Sistema', 'Faculdade')
for p in palavras:
    print('\nNa palavra {} temos: '.format(p.upper()), end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
