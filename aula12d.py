import datetime

anoNascimento = int(input('Favor informar o ano de nascimento do jovem (ano com 4 digítos): '))
anoAtual = int(datetime.date.today().year)
idadeCandidato = int(anoAtual - anoNascimento)
idadeAlistamento = int(18)
anosDiferenca = int(idadeCandidato - idadeAlistamento)

if idadeCandidato > idadeAlistamento:
    print('A idade do alistamento já passou em {} ano(s)'.format(anosDiferenca))
elif idadeCandidato < idadeAlistamento:
    print('O candidato deverá se alistar em {} anos(s)'.format((str(anosDiferenca))[1:]))
else:
    print('O candidato está em ano de alistamento!')
