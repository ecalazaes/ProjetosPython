print(f'Questão 2)\n')
while True:
    n1 = float(input('Entre com um valor Inteiro maior que zero para o Cateto A: '))
    if n1 <= 0:  # validação para positivo maior que zero
        print('Valor inválido, tente novamente.')
    else:
        break
while True:
    n2 = float(input('Entre com um valor Inteiro maior que zero para o Cateto B: '))
    if n2 <= 0:  # validação para positivo maior que zero
        print('Valor inválido, tente novamente.')
    else:
        break
while True:
    n3 = float(input('Entre com um valor Inteiro maior que zero para a Hipotenusa: '))
    if n3 <= 0:  # validação para positivo maior que zero
        print('Valor inválido, tente novamente.')
    else:
        break
if (n1 ** 2) + (n2 ** 2) == n3 ** 2:
    print(f'Os lados {n1}, {n2} e {n3} formam um triângulo retângulo.')
else:
    print(f'Os lados {n1}, {n2} e {n3} não formam um triângulo retângulo.')
