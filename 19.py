import random
a = str(input('Insira um aluno: '))
b = str(input('Insira um aluno: '))
c = str(input('Insira um aluno: '))
d = str(input('Insira um aluno: '))
lista =  [a, b, c, d]
print('O aluno escolhido foi {}.'.format(random.choice(lista)))