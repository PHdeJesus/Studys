a = float(input('Qual a distância em km: '))
if a <= 200:
    print('Só isso linda? {:.1f}kms pra ver macho??'.format(a))
    print('Vai pagar R${:.2f} pra largar de ser otária.'.format(a * 0.5))
else:
    print('Ela não mede distancia meixmo! {:.1f}kms pra ver o macho meia-boca dela.'.format(a))
    print('Aproveita que não tá sabendo contar e paga R${:.2f}, burra do caralho.'.format(a * 0.45))
    