import datetime
print('--CATEGORIA DE NATAÇÃO--')
anoNascimento = int(input('Favor informar o ano de nascimento do atleta: '))
anoAtual = int(datetime.date.today().year)
idadeAtleta = int(anoAtual - anoNascimento)

if idadeAtleta> 0  and idadeAtleta <= 9:
    print('Este atleta pertence a categoria mirim!')
elif idadeAtleta >= 10 and idadeAtleta <= 14:
    print('Este atleta pertence a categoria infantil!')
elif idadeAtleta>=15 and idadeAtleta <= 19:
    print('Este atleta pertence a categoria júnior')
elif idadeAtleta == 20:
    print('Este atleta pertence a categoria Sênior')
elif idadeAtleta > 20:
    print('Este atleta pertence a categoria Master! ')
else:
    print('Data de nascimento inválida!')