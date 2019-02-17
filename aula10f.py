num1 = float(input('Digite um número: '))
num2 = float(input('Digite outro número: '))
num3 = float(input('Digite mais um número: '))

if num1 > num2 and num1 > num3:
    if num2 < num3:
        print('O maior número digitado é o {} e o menor é o {}'.format(num1, num2))
    else:
        print('O maior número digitado é o {} e o menor é o {}'.format(num1, num3))
if num2 > num1 and num2 > num3:
    if num3 < num1:
        print('O maior número digitado é o {} e o menor é o {}'.format(num2, num3))
    else:
        print('O maior número digitado é o {} e o menor é o {}'.format(num2, num1))
if num3 > num1 and num3 > num2:
    if num2 < num1:
        print('O maior número digitado é o {} e o menor é o {}'.format(num3, num2))
    else:
        print('O maior número digitado é o {} e o menor é o {}'.format(num3, num1))
