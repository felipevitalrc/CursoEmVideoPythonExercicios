print('---PROGRAMA PARA CALCULAR TIPO DE TRIÂNGULO---')
ladoA = float(input('Digite a primeira reta: '))
ladoB = float(input('Digite a segunda reta: '))
ladoC = float(input('Digite a terceira reta: '))
triangulo = bool(False) #variável para identificar se foi formado triângulo com os valores informados '0' para não '1' para sim


if (ladoA - ladoB) < ladoA and ladoA < (ladoB + ladoC):
    if (ladoA - ladoC) < ladoB and ladoB < (ladoA + ladoC):
        if (ladoA - ladoB) < ladoC and ladoC < (ladoA + ladoB):
            triangulo = True
        else:
            triangulo = False

if triangulo == True:
    if ladoA == ladoB == ladoC:
        print('Este triângulo é um equilátero.')
    elif ladoA == ladoB or ladoA == ladoC or ladoB == ladoC:
        print('Este triângulo é um isósceles.')
    else:
        print('Todos os lados são diferentes. Estre triângulo é um escaleno.')

if triangulo == False:
    print('Os valores informados não formam um triângulo.')

