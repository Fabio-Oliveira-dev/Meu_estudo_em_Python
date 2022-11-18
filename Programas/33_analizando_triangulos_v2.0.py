#ex042 – Analisando Triângulos v2.0
n1 = float(input('Primeiro Seguimento: '))
n2 = float(input('Segundo seguimento: '))
n3 = float(input('Terceiro seguimento: '))
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('Os seguimentos acima PODEM formar um triângulo ', end='')
    if n1 == n2 == n3: # if, elif ou else: dentro de outro if é uma condição aninhada
        print('EQUILÁTERO!')
    elif n1 != n2 != n3 != n1:
        print('ESCALENO!')
    else:
        print('ISÓSCELES')
else:
    print('Os seguimentos acima NÃO pode formar triângulo!')
