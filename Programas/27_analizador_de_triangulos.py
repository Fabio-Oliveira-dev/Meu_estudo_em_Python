print('-='*20)
print('Analizador de triângulos')
print('-='*20)
r1 = float(input('Primeiro seguimento:'))
r2 = float(input('Segundo seguimento:'))
r3 = float(input('Terceiro seguimento:'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os seguimento acima PODEM FORMAR triângulo')
else:
    print('Os seguimentos acima NÃO PODEM FORMAR triângulo')