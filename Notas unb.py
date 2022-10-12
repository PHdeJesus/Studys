nota = int(input('Insira sua nota: '))
if nota >= 9:
    print('SS')
elif nota >= 7:
    print('MS')
elif nota >= 5:
    print('MM')
elif nota >= 3:
    print('MI')
elif nota >= 1:
    print('MR')
else:
    print('SR')