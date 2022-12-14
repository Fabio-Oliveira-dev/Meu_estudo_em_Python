''' Exercício 68 – Jogo do Par ou Ímpar
Faça um programa que jogue par ou ímpar com o computador.
O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias
consecutivas que ele conquistou no final do jogo. '''
from random import randint
computador = soma = v = 0
print('=-' * 20)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-' * 20)
while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(0, 11)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PpIi': #Enquanto tipo não for par ou impar
        tipo = str(input('Par ou Ímpar? [P/I]')).strip().upper()[0]
    print('Você jogou {} e o computador jogou {}. O Total é de {} '.format(jogador, computador, total), end='')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você vendeu!')
            v += 1
        else:
            print('Você perdeu!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você vendeu!')
            v += 1
        else:
            print('Você perdeu!')
            break
    print('Vamos jogar novamente...')
print('GAME OVER! Você vendeu {} vezes'.format(v))
