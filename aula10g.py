salario = float(input('Qual é o salário do funcionário? '))
if salario > 1250:
    print('O reajuste é de R$ {}. Sendo assim o salário do funcionário passa a ser R$ {}'.format((salario * 0.10), (
                (salario * 0.10) + salario)))
else:
    print('O reajuste é de R$ {}. Sendo assim o salário do funcionário passa a ser R$ {}'.format((salario * 0.15), (
                (salario * 0.15) + salario)))
