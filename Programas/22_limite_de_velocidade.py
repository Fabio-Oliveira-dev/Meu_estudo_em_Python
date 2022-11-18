from time import sleep
velocidade = float(input('Qual a velocidade atual do veiculo?'))
print('PROCESSANDO...')
sleep(2)
if velocidade > 80:
    print('VOCÊ FOI MULTADO! Você excedeu o limite de velocidade máxima que é de 80 km/h!.')
    multa = (velocidade-80) *7
    print('Você deve pagar a multa de R$ {:.2f}!'.format(multa))
else:
    print('Você está dentro do limite de velocidade!')
print('Tenha um bom dia! Dirija com segurança!.')
