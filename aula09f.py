#Quantas vezes aparece a letra 'A'. Em que posição a letra 'A' aparece pela primeira vez. Em que posição a letra 'a' aparece pela última vez.

frase = str(input('Digite uma frase qualquer: '))
contadorA = (frase.lower()).count('a')
primeiroA = (frase.lower()).find('a')
ultimoA = (frase.lower()).rfind('a')
print('A letra ''A'' aparece {} vezes na frase'.format(contadorA))
print('A letra A aparece na posição {} pela primeira vez'.format(primeiroA))
print('A letra A aparece pela última vez na posição {}'.format(ultimoA))
