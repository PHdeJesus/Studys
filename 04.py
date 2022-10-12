a = float(input('Insira um valor em R$: '))
b = a + (a * 15 / 100)
print('Um funcionário que recebia {:.2f}, com 15% de aumento, passará a receber R${:.2f}.'.format(a, b))
