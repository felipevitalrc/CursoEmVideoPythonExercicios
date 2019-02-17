soma = 0
print('-- Programa para somar números pares entre os 6 digitados --')
for c in range(1, 7, 1):
    num = int(input('Favor digitar um número inteiro: '))
    if num % 2 == 0:
        soma = soma + num
print('A soma dos número pares digitados é: {}'.format(soma))