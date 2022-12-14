# Exercício 66 – Vários números com flag
soma = cont = 0
while True:
    n = int(input('Digite um número [999 para parar]: '))
    if n == 999:
        break
    soma += n
    cont += 1
print('Você digitou {} números!'.format(cont))
print('A soma dos valores foi {}!'.format(soma))
