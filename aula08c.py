import math

catetoOposto = float(input('Digite o valor do cateto oposto: '))
catetoAdjacente = float(input('Digite o valor do cateto subjacente: '))
hipotenusa = math.hypot(catetoOposto, catetoAdjacente)

print('A hipotenusa dessa conta é: {}'.format(hipotenusa))