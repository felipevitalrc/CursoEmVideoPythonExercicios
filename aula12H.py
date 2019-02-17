import math
peso = float(input('Digite o peso: '))
altura = float(input('Digite a altura: '))
alturaAoQuadrado = float(pow(altura,2))
imc = peso/alturaAoQuadrado

if imc <= 18.5:
    print('Abaixo do peso')
elif imc >= 18.6 and imc <= 25:
    print('Peso ideal')
elif imc >= 25.1 and imc <= 30:
    print('Sobrepeso')
elif imc >= 30.1 and imc <= 40:
    print('Obesidade')
elif imc >= 40.1:
    print('Obesidade mórbida')
