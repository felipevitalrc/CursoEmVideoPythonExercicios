# Verificar se existe "Silva" no nome da pessoa

nome = str (input('Digite um nome: ')) #Código para receber o nome
validaSilva = ' silva ' in ' '+nome.lower()+' ' #Código que coloca o nome em letras minúsculas, adiciona um espaço antes e depois da variável para encontrar o 'silva' tanto no começo, quanto no meio quanto no fim.
print('Existe ''Silva'' no nome da pessoa? {}'.format(validaSilva))