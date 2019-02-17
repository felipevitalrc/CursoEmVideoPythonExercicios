nota1 = float(input('Digite a primeira nota do aluno: '))
nota2 = float(input('Digite a segunda nota do aluno: '))
media = float((nota1+nota2)/2)

if media<5 and media > 0:
    print('Aluno reprovado! :(')
elif media >=5 and media <= 6.9:
    print('O aluno está de recuperação.')
elif media >= 7 and media <= 10:
    print('Aluno está aprovado! :)')
else:
    print('Média maior que 10 ou menor que 0. Favor rever notas digitadas. As notas não podem ser maior que 10 ou menor que 0.')
