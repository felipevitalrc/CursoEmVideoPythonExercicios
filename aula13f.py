termo = int(input('Favor digite o primeiro termo da progressão aritmética (PA): '))
razao = int(input('Favor digite a razão desta progressão aritmética: '))
proxTermo = 0
print('Sequência dos próximos 10 termos da PA, considerando o primeiro termo {} e a razão {}: '.format(termo, razao))
for c in range(1, 11, 1):
    if c == 1:
        proxTermo = termo+razao
        print(proxTermo)
    else:
        proxTermo = proxTermo+razao
        print(proxTermo)