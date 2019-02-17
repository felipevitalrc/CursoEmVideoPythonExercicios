import emoji
import random

print('--VAMOS JOGAR JOKENPÔ?--')
print('[1] Pedra'
      '\n[2] Papel'
      '\n[3] Tesoura')
jogadorHumano = int(input('Escolha a sua opção: '))
maquina = random.choice([1,2,3])
dicionarioOpcoes = {1:'pedra',2:'papel',3:'tesoura'}

if jogadorHumano == maquina:
    print('Deu empate! Nós dois escolhemos {}'.format(dicionarioOpcoes[maquina]))
elif jogadorHumano == 1 and maquina == 2:
    print('Eu ganhei!'
          '\nEu escolhi papel ', emoji.emojize(':page_facing_up:', use_aliases=True))
elif jogadorHumano == 1 and maquina == 3:
    print('Você ganhou!'
          '\nEu escolhi tesoura ', emoji.emojize(':scissors:', use_aliases=True))
elif jogadorHumano == 2 and maquina == 1:
    print('Você ganhou!'
          '\nEu escolhi pedra ', emoji.emojize(':crystal_ball:', use_aliases=True))
elif jogadorHumano == 2 and maquina == 3:
    print('Eu ganhei!'
          '\nEu escolhi tesoura ', emoji.emojize(':scissors:', use_aliases=True))
elif jogadorHumano == 3 and maquina == 1:
    print('Eu ganhei!'
          '\nEu escolhi pedra ', emoji.emojize(':crystal_ball:', use_aliases=True))
elif jogadorHumano == 3 and maquina == 2:
    print('Você ganhou!'
          '\nEu escolhi papel ', emoji.emojize(':page_facing_up:', use_aliases=True))
else:
    print('Escolha inválida. Jogue novamente.')


#print(emoji.emojize(':crystal_ball:', use_aliases=True)) #pedra
#print(emoji.emojize(':page_facing_up:', use_aliases=True)) #papel
#print(emoji.emojize(':scissors:', use_aliases=True)) #tesoura



