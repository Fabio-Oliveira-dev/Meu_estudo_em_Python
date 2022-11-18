'''import math
an = float(input('Digite o ângulo desejado:'))
seno = math.sin(math.radians(an))
print('O ângulo de {} tem o seno de {:.2f}'.format(an, seno))
cosseno = math.cos(math.radians(an))
print('O ângulo de {} tem o cosseno {:.2f}'.format(an, cosseno))
tangente = math.tan(math.radians(an))
print('O ângulo de {} tem a tangente de {:.2f}'.format(an, tangente))'''

from math import radians, sin, cos, tan
an = float(input('Digite o ângulo desejado:'))
seno = sin(radians(an))
print('O ângulo de {} tem o seno de {:.2f}'.format(an, seno))
cosseno = cos(radians(an))
print('O ângulo de {} tem o cosseno {:.2f}'.format(an, cosseno))
tangente = tan(radians(an))
print('O ângulo de {} tem a tangente de {:.2f}'.format(an, tangente))

#2 maneiras diferentes de fazer o exercício