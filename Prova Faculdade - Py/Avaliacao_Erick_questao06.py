print(f'Questão 6)\n')
contGAS = 0  # contador
contALC = 0  # contador
contDIE = 0  # contador
escolha = 0  # contador
print(f'Gasolina (1)\nÁlcool (2)\nDiesel (3)\nFim (4)\n')
while escolha != 4:  # repete a entrada sempre que o variavel escolha for diferente de 4
    escolha = int(input(f'Qual o Produto de sua preferência:  '))
    if escolha == 1:
        contGAS += 1  # se a variavel escolha receber valor 1 soma 1 voto ao contador de gasolina
    elif escolha == 2:
        contALC += 1  # se a variavel escolha receber valor 2 soma 1 voto ao contador de alcool
    elif escolha == 3:
        contDIE += 1  # se a variavel escolha receber valor 3 soma 1 voto ao contador de diesel
    elif escolha == 4:  # se a variavel escolha receber o valor 4, encerra o programa e exibe o resultado
        print(f'\nMuito Obrigado!')
        print(f'Álcool: {contALC}')
        print(f'Gasolina: {contGAS}')
        print(f'Diesel: {contDIE}')
