lar = float(input('Qual a largura da parede?'))
alt = float(input('Qual a altura da parede?'))
área = lar * alt
print('Sua parede tem as dimensões de {}x{} e a sua área é de {:.2f}m2.'.format(lar, alt, área))
tinta = área / 2
print('Você precisara de {} litros de tinta para pintar essa parede!.'.format(tinta))

