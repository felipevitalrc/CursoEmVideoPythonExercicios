import random

numAleatorio = random.choice([1, 2, 3, 4, 5])
cores = {'limpa': '\033[m',
         'fundoVermelho': '\033[1;41m',
         'fundoVerde': '\033[1;42m'} #lista de cores
#print('{}'.format(numAleatorio))
print('-- O computador acaba de pensar em um número inteiro de 1 a 5. --')
respUser = int(input('\nQue número é esse? Digita aqui: '))

if numAleatorio == respUser:
    print('\n',cores['fundoVerde'],'Parabéns! Você acertou!',cores['limpa'])
else:
    print('\n',cores['fundoVermelho'],'Xiii, errou! Tente novamente!',cores['limpa'])
    print('\n',cores['fundoVermelho'],'O número que o computador escolheu foi: {}'.format(numAleatorio),cores['limpa'])