#Ex045 – GAME: Pedra Papel e Tesoura
from random import randint #randint o computador faz escolhas aleatórias
from time import sleep
itens = ('\033[0;31mPedra\033[m', '\033[0;32mPapel\033[m', '\033[0;33mTesoura\033[m')
computador = randint(0, 2)
print(''' Suas opções:
[ 0 ] \033[0;31mPEDRA\033[m
[ 1 ] \033[0;32mPAPEL\033[m
[ 2 ] \033[0;33mTESOURA\033[m''')
jogador = int(input('Qual a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ !!!')
print('-=' * 11)
print('O COMPUTADOR jogou {}'.format(itens[computador]))
print('O JOGADOR jogou {}'.format(itens[jogador]))
print('-=' * 11)
if computador == 0: # o computador jogou pedra
    if jogador == 0:
        print('EMPATE')
    if jogador == 1:
        print('JOGADOR VENCE')
    if jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVÁLIDA!.')
elif computador == 1: # o computador jogou papel
    if jogador == 0:
        print('COMPUTADOR VENCE')
    if jogador == 1:
        print('EMPATE')
    if jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVÁLIDA!.')
elif computador == 2: # o computador jogou tesoura
    if jogador == 0:
        print('JOGADOR VENCE')
    if jogador == 1:
        print('COMPUTADOR VENCE')
    if jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA!.')
