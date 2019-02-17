#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados

#Forma de string
#num = str(input('Digite um número entre 0 e 9999: '))
#rint('Unidade do número: {}'.format(num[3]))
#print('Dezena do número: {}'.format(num[2]))
#print('Centena do número: {}'.format(num[1]))
#print('Milhar do número: {}'.format(num[0]))

#Forma matemática

num1 = int(input('Digite um número: '))
unidade = num1 //1 % 10
dezena = num1 // 10 % 10
centena = num1 //100 % 10
milhar = num1 // 1000 % 10
print('Analisando o número {}'.format(num1))
print('Unidade: {}'.format(unidade))
print('Dezena: {}'.format(dezena))
print('Centena: {}'.format(centena))
print('Milhar: {}'.format(milhar))