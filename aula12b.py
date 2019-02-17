print('---PROGRAMA PARA CONVERTER NÚMEROS EM BINÁRIOS, HEXAS OU OCTAIS')
num = int(input('Informe o número: '))
print('[1] Binário'
      '\n[2] Hexadecimal'
      '\n[3] Octal')
baseConversao = int(input('Informe a base de conversão:' ))
if baseConversao == 1:
    print('O número em binário é: {}'.format(bin(num)[2:]))
elif baseConversao == 2:
    print('O número em hexadecimal é: {}'.format(hex(num)[2:]))
elif baseConversao == 3:
    print('O número em octal é: {}'.format(oct(num)[2:]))
else:
    print('Você esolheu uma opção errada. Favor reexecutar o programa com uma opção correta.')