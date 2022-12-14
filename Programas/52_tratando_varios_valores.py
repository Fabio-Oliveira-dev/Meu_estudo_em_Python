#Exercício 64 – Tratando vários valores v1.0
n = 0
cont = 0
soma = 0
n = int(input('Digite um número [999 para parar]:'))
while n != 999:
    soma += n
    cont += 1
    n = int(input('Digite um número [999 para parar]:'))
print('Você digitou {} números e a soma entre eles foi {}.'.format(cont, soma))
