#Exercício 59 – Criando um Menu de Opções
from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opçao = 0
while opçao != 5:
    print('''    [ 1 ] SOMAR
    [ 2 ] MULTIPLICAR
    [ 3 ] MAIOR
    [ 4 ] NOVOS NÚMEROS
    [ 5 ] SAIR DO PROGRAMA''')
    opçao = int(input('Qual é a sua opção? '))
    if opçao == 1:
        soma = n1 + n2
        print('A soma de {} + {} é {}'.format(n1, n2, soma))
    elif opçao == 2:
        produto = n1 * n2
        print('O resultado de {} x {} é {}'.format(n1, n2, produto))
    elif opçao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {}, o maior valor é {}'.format(n1, n2, maior))
    elif opçao == 4:
        print('Informa os números novamente: ')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opçao == 5:
        print('Finalizando...')
    else:
        print('Opção inválida! Digite novamente.')
    print('=-=' * 10)
    sleep(2)
print('Fim do programa! Volte sempre.')
