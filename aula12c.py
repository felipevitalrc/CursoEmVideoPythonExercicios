num1 = int(input('Digite o primeiro número inteiro: '))
num2 = int(input('Digite o segundo número inteiro: '))
if num1 > num2:
    print('O número {} é maior que o número {}'.format(num1, num2))
elif num1 < num2:
    print('O número {} é maior que o número {}'.format(num2, num1))
else:
    print('Ambos os números são iguais!')
