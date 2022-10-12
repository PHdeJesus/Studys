import random
import time
a = random.randint(0, 10)
print('-=-' * 25)
print(' VOU PENSAR EM UM VALOR, TENTE ADIVINHAR...')
print('-=-' * 25)
valor = int(input('QUE VALOR EU PENSEI???: '))
print('PROCESSANDO...')
time.sleep(3)
if valor == a:
    print('Parabéns, você conseguiu')
else:
    print('buá buá você errrou!')