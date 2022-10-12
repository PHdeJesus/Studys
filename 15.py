a = int(input('Quantos dias: '))
b = float(input('Quantos km: '))
d = a * 60 + 0.15 * b
print('Um carro alugado por {} dias e que rodou {}kms deve a locadora R${:.2f}.'.format(a, b, d))
