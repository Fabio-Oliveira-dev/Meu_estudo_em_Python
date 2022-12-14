#Exercício 053 – Detector de Palíndromo

# strip() é tirar os espaços e upper() é jogar tudo para maiúscula
frase = str(input('Digite uma frase: ')).strip().upper()
palavra = frase.split() # split() separa as palavras em lista ou coleções
junto = ''.join(palavra) # ''.join() vai juntar todas as palavras sem espaço
'''inverso = '' '''
inverso = junto[::-1] # outra forma de fazer substituindo o for
'''for letra in range(len(junto) - 1, -1, -1): # fui da ultima letra ate a primeira com o len e os - 1
    inverso += junto[letra]'''
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um palíndromo')
else:
    print('A frase digitada não é um palíndromo')
