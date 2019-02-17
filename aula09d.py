# Ver se o nome da cidade informada começa com "Santo"

nomeCid = str(input('Digite o nome da cidade: ')) #Variável de recepção da informação
inicioNomeCid = (nomeCid.strip()).upper() #Este código está separando o nome da cidade em partes de acordo com os espaços e transformando tudo em letra maiúscula
validaNome = 'SANTO' in inicioNomeCid.split()[0] #Este código está verificando se o nome da cidade começa com 'SANTO' considerando a variável inicioNomeCid
print('Existe ''Santo'' no início do nome da cidade? {}'.format(validaNome)) #Este código está imprimindo a resposta na tela
