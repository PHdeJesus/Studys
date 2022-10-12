n = float(input('Insira um valor: R$ '))
d = n / 4.61
e = n / 5.06
y = n / 0.72
i = n / 0.038
h = n / 1.42
print('Com R${:.2f} você pode comprar US$ {:.2f}.'.format(n, d))
print('Com R${:.2f} você pode comprar EUR {:.2f}.'.format(n, e))
print('Com R${:.2f} você pode comprar CNY {:.2f}.'.format(n, y))
print('Com R${:.2f} você pode comprar JP¥ {:.2f}.'.format(n, i))
print('Com R${:.2f} você pode comprar AED {:.2f}.'.format(n, h))