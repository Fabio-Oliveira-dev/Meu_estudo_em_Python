from random import randint
from time import sleep #o programa da uma pausa de 3 segundos antes de mostrar o resultado
computador = randint(0, 5) #faz o computador 'pensar' ou sortear o número.
print('-=-' *20)
print('Vou pensar em algum número entre 0 e 5. Tente advinhar')
print('-=-' *20)
jogador = int(input('Em que número eu pensei!')) #o jogador tenta advinhar
print('PROCESSANDO...')
sleep(3) #é os segundos que o programa vai esperar para executar
if jogador == computador:
    print('PARÁBENS! Você conseguiu me vender!')
else:
    print('GANHEI! Eu pensei no número {} e não no número {}'.format(computador, jogador))

        

