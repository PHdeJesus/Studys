import math
a = float(input('Insira o �ngulo desejado: '))
print('O �ngulo de {} tem o SENO de {:.2f}.'.format(a, math.sin(math.radians((a)))))
print('O �ngulo de {} tem o COSSENO de {:.2f}.'.format(a, math.cos(math.radians(a))))
print('O �ngulo de {} tem a TANGENTE de {:.2f}.'.format(a, math.tan(math.radians(a))))