funcionario = str(input('Qual é o seu nome?'))
salario = float(input('Qual é o seu salario atual? R$'))
novo = salario + (salario * 15 / 100)
print('Funcionario {}, o seu salario atual é de R${:.2f} com o novo reajuste de 15% passará a ser de R${:.2f}'.format(funcionario, salario, novo))

