print('---PROGRAMA PARA CALCULAR SE É POSSÍVEL FORMAR UM TRIÂNGULO---')
ladoA = float(input('Digite a primeira reta: '))
ladoB = float(input('Digite a segunda reta: '))
ladoC = float(input('Digite a terceira reta: '))

if (ladoA - ladoB) < ladoA and ladoA < (ladoB + ladoC):
    if (ladoA - ladoC) < ladoB and ladoB < (ladoA + ladoC):
        if (ladoA - ladoB) < ladoC and ladoC < (ladoA + ladoB):
            print('Com estas retas é possível formar um triângulo!')
        else:
            print('Com estas retas não é possível formar um triângulo')
