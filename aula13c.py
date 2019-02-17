soma = 0
for c in range(1, 501, 1):
    if (c % 2) != 0:
        if c % 3 == 0:
            soma = soma + c
print('A soma de todos os números entre 1 e 500 que são ímpares e múltiplos de 3 é: {}'.format(soma))
        #else:
            #print(c, 'Não é múltiplo de 3')
    #else:
        #print(c, 'Não é ímpar')
