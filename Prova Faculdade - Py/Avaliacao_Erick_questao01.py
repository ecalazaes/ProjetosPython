print(f'Questão 1)\n')
while True:
    a = float(input(f'Entre com um valor de cateto A, deve ser positivo maior que zero: '))
    if a <= 0:  # validação para positivo maior que zero
        print(f'Valor inválido, tente novamente.')
    else:
        break
while True:
    b = float(input(f'Entre com um valor de cateto B, deve ser positivo maior que zero: '))
    if b <= 0:  # validação para positivo maior que zero
        print(f'Valor inválido, tente novamente.')
    else:
        break
c = ((a ** 2) + (b ** 2)) ** (1 / 2)
print(f'O valor da Hipotenusa deste triângulo é {c:.2f}.')
