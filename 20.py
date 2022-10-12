import random
a = str(input('Insira um aluno: '))
b = str(input('Insira um aluno: '))
c = str(input('Insira um aluno: '))
d = str(input('Insira um aluno: '))
lista = [a, b, c, d]
random.shuffle(lista)
print('A ordem de apresentação será:{}'.format(lista))