n1 = float(input('Digite a primeira nota do aluno: '))
n2 = float(input('Digite a segunda nota do aluno: '))
m = (n1+n2)/2

if m < 6:
    print('A media do aluno foi: {}. Com isso, ele não passou, está de recuperação.'.format(m))
if 6 <= m and m <= 10:
    print('A nota do aluno foi {}. Com esta nota, ele passou! O deseje boas férias! :)'.format(m))
else:
    print('As notas digitadas são inválidas. Favor digitar notas entre 0 e 10.')
print('---FIM DA EXECUÇÃO DO PROGRAMA---')