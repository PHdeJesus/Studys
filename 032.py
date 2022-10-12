import datetime
print('***' * 10) 
print('ANALISADOR DE ANO BISSEXTO')
print('***' * 10) 
a = int(input('Qual ano gostaria de analisar? Caso seja o ano corrente insira 0: '))
if a == 0:
    a = datetime.date.today().year
if a % 4 == 0 and a % 100 !=0 or a % 400 == 0:
    print('O ano {} é bissexto.'.format(a))
else:
    print('O ano {} não é bissexto.'.format(a))
    