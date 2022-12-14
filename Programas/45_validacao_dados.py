#Exercício 57 – Validação de Dados
sexo = str(input('Informa o seu sexo: [M/F]')).strip().upper()[0] # O 0 no upper é para pegar apenas a primeira letra
while sexo not in 'MmFf':
    sexo = str(input('Dados incorretos. Por favor, informe o seu sexo: [M/F]')).strip().upper()[0]
print('Sexo {} registrado com sucesso.'.format(sexo))
