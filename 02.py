a = float(input('Insira altura: '))
b = float(input('Insira largura: '))
c = a * b
print('Sua parede tem {} de altura e {} de largura, portanto tem {}m².'.format(a, b, c))
d = c / 2 
print('Você precisará de {} litros para pintar sua parede de {}m².'.format(d, c))
