#3 maneiras diferentes de fazer o calculo da hipotenuza
'''co = float(input('Comprimento do cateto oposto:'))
ca = float(input('Comprimento do cateto adjacente:'))
h = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenuza vai medir {:.2f}'.format(h))'''

'''import math
co = float(input('Comprimento do cateto oposto:'))
ca = float(input('Comprimento do cateto adjacente:'))
h = math.hypot(co, ca)
print('A hipotenuza vai medir {:.2f}'.format(h))'''

from math import hypot
co = float(input('Comprimento do cateto oposto:'))
ca = float(input('Comprimento do cateto adjacente:'))
h = hypot(co, ca)
print('A hipotenuza vai medir {:.2f}'.format(h))
