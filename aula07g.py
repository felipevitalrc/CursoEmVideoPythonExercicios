#Cálculo de tinta

altura = float(input('Digite a altura da parede: '))
largura = float(input('Digite a largura da parede: '))
qtdeTinta = float((altura*largura)/2)

print('Para pintar essa parede você precisará de {} litros de tinta'.format(qtdeTinta))