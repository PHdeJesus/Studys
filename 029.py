a = float(input('Insira a velocidade: Km/h'))
if a > 80:
    print('MULTADO! Você tá muito veloz e furiosa linda.')
    print('Quis ser a Charlie XCX vai ser a Beyzinha tá aqui seu boleto: R${},00.'.format((a - 80) * 7))
    print('Tenha um bom dia! Dirija com segurança!')
else:
    print('Tenha um bom dia! Dirija com segurança!')