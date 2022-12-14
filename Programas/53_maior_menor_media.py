#Exercício 65 – Maior e Menor valores
resp = 's'
soma = quant = media = maior = menor = 0 # Todas as variaveis em uma única linha para facilitar na escrita do codigo
while resp in 'Ss':
    n = int(input('Digite um número: '))
    soma += n
    quant += 1
    if quant == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resp = str(input('Quer ccontinuar? [S/N]')).strip()[0].upper()
media = soma / quant
print('Você digitou {} números e a média foi {}.'.format(quant, media))
print('O maior valor foi {} e o menor valor foi {}.'.format(maior, menor))
