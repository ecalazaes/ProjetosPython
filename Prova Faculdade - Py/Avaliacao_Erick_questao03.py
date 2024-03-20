print(f'Questão 3)\n')
while True:
    n = int(input('Entre com um número que seja menor que 1000: '))
    if n > 1000:  # validação para positivo menor que 1000 e maior que zero
        print(f'Valor inválido.')
    elif n > 0:
        for i in range(1, n + 1, 2):  # lógica para exibir impares a partir de uma entrada positiva
            print(i)
        break
    else:
        if n % 2 == 0:
            for i in range(n + 1, 2, 2):  # lógica para exibir impares a partir de uma entrada negativa par
                print(i)
        else:
            for i in range(n, 2, 2):  # lógica para exibir impares a partir de uma entrada negativa impar
                print(i)
        break
