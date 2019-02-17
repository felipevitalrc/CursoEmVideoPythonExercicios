valorCasa = float(input('Informe o valor do imóvel: '))
salario = float(input('Informe o salário do interessado: '))
tempoPgto = (int(input('Em quantos anos será feito o pagamento? '))*12)
valorParcela = float(valorCasa/tempoPgto)
percentualSalario = float(0.30*salario)
limiteMensal = float(valorCasa/tempoPgto)

if limiteMensal>percentualSalario:
    print('Infelizmente o cliente não foi aprovado. Tente aumentar o prazo de financiamento. :(')
else:
    print('Seu empréstimo foi aprovado. Você precisará pagar {} por mês, durante {} meses'.format(valorParcela, tempoPgto))
print('--OBRIGADO PELA PREFERÊNCIA--')