precoProduto = float(input('Informe o preço do produto: '))
print('[1] A vista em dinheiro ou cheque'
      '\n[2] A vista no cartão'
      '\n[3] 2 vezes no cartão'
      '\n[4] 3 ou mais vezes no cartão')
opcaoEscolhida = int(input('\nQual a opção de pagamento escolhida? '))

if opcaoEscolhida == 1:
    print('O valor final do produto é R$ {}'.format(precoProduto - (precoProduto*0.10)))
elif opcaoEscolhida == 2:
    print('O valor final do produto é R$ {}'.format(precoProduto - (precoProduto * 0.05)))
elif opcaoEscolhida == 3:
    print('O valor final do produto é R$ {}'.format(precoProduto))
elif opcaoEscolhida == 4:
    print('O valor final do produto é R$ {}'.format(precoProduto + (precoProduto * 0.20)))
else:
    print('Opção escolhida inválida. Favor reexecutar o programa e escolher uma das opções válidas.')