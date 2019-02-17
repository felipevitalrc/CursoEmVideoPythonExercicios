num = int(input('Digite um número inteiro para calcularmos a sua tabuada: '))
for c in range(1, 11, 1):
    tab = num*c
    print('{} x {} = {}'.format(num, c, tab))