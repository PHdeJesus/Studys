a = float(input('Insira um valor em R$: '))
b = a - (a * 5 / 100)
print('O produto que custava R${} com 5% de desconto custará R${:.2f}.'.format(a,b))
