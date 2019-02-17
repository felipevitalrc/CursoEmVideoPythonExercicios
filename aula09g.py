#Receber um nome e escrever separadamente o primeiro e o último

nome = str(input('Digite um nome completo: '))
primeiroNome = nome.split()[0]
ultimoNome = nome.split()[-1]
print('O primeiro nome da pessoa é: {}'.format(primeiroNome))
print('O último nome da pessoa é: {}'.format(ultimoNome))