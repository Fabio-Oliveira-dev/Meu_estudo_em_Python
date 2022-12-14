'''Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos. '''

tot18 = totm = totm20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' ' # Para não aceitar se o usuario gisitar outra coisa alem de M e F
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        totm += 1
    if sexo == 'F' and idade < 20:
        totm20 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('Total de pessoas com mais de 18 anos: {}.'.format(tot18))
print('Ao todo temos {} homens cadastrados.'.format(totm))
print('E temos o total de {} mulheres com menos de 20 anos.'.format(totm20))
