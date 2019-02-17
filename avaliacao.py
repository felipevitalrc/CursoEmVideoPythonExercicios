from datetime import date

ano = date.today().year

print(ano)

num = 5 % 2
num2 = 9 % 2
num3 = 4 % 2
num4 = 1 % 2
num5 = 4 % 2
print(num, num2, num3, num4, num5)


from random import randint

num6 = randint(1, 6)
res = num // 2
res2 =  5 // 2
print(res2)
print(res)

texto = ('Tres Pratos de Trigo para Tigres Tristes')
total = texto.upper().count(texto[0])
print(total)