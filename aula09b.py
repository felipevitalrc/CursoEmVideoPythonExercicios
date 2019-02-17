nomeCompleto = str(input('Por favor, digite seu nome completo: '))
print('Seu nome completo em letras maiúsculas é: {}'.format(nomeCompleto.upper())) #Nnome completo da pessoa em letras maiúsculas
print('Seu nome completo em letras minúsculas é: {} '.format(nomeCompleto.lower())) #Nnome completo da pessoa em letras minúsculas
print('Seu nome completo tem {} letras'.format(len(''.join(nomeCompleto.split())))) #Nome completo da pessoa separado pelo sprint e depois juntado pelo join para contagem
print('Seu primeiro nome tem {} letras'.format(nomeCompleto.find(' ')))



