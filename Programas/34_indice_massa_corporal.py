#Exe043 – Índice de Massa Corporal
peso = float(input('Qual é o seu peso (Kg) '))
altura = float(input('Qual é a sua altura? (M) '))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa é \033[0;31m{:.1f}\033[m'.format(imc))
if imc < 18.5:
    print('Você esta ABAIXO do peso normal.')
elif 18.5 <= imc < 25:
    print('PARABÉNS, você está na faixa de peso normal.')
elif 25 <= imc < 30:
    print('Você está em SOBREPESO.')
elif 30 <= imc < 40:
    print('Você está em OBESIDADE.')
else:
    print('Você está em OBESIDADE MÓRBIDA, cuidado!.')
