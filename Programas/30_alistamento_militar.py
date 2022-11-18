#ex039 – Alistamento Militar
from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print('Quem nasceu em {} anos tem {} anos em {}.'.format(nasc, idade, atual))
if idade == 18:
    print('Você tem que se alistar \033[0;31mIMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    print('\033[0;31mVocê ainda não tem 18 anos.\033[m Ainda falta {} anos para o alistamento.'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {} ano.'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('\033[0;31mVocê já deveria ter se alistado a {} anos.'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {} ano'.format(ano))


