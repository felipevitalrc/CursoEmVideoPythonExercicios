kmViagem = float(input('Digite a distância (em KM) a ser percorrida na viagem: '))

if kmViagem <= 200:
    print('O valor a ser cobrado dessa viagem é R$ {}'.format(kmViagem * 0.50))
else:
    print('O valor a ser cobrado dessa viagem é R$ {}'.format(kmViagem * 0.45))
