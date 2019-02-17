print('--Programa para identificar se um número é primo--')
num = int(input('Digite um número inteiro: '))
contadorPrimo = int(1)
for c in range(1, num, 1):
    if (num % num) == 0 and (num % 1) == 0 and (num % c) != 0:
        contadorPrimo = contadorPrimo
    else:
        contadorPrimo = contadorPrimo + 1
if contadorPrimo == 2:
    print('Este número É primo.')
else:
    print('Este número NÃO É primo.')
