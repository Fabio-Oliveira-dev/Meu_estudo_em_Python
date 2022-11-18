#Exercício 051 – Progressão Aritmética
print('=')
print('10 TERMOS DE UMA PA')
print('=')
termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = termo + (10 - 1) * razao
for c in range(termo, decimo + razao, razao):
    print('{} '.format(c), end=' • ')
print('ACABOU')
