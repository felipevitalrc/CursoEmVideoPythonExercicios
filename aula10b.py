velocidadeCarro = float(input('Digite a velocidade do carro: '))
multa = float(velocidadeCarro - 80) * 7

if velocidadeCarro > 80:
    print('O carro está acima do limite de velocidade!!!')
    print('A multa por essa negligência é R$ {}'.format(multa))
else:
    print('O carro está dentro do limite permitido de velocidade')
