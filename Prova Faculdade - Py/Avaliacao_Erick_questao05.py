print(f'Questão 5)\n')
while True:
    num = int(input('Digite um número inteiro maior que zero: '))
    if num <= 0:  # Validacao para numero maior que zero
        print(f'Valor inválido')
    else:
        break
d = 1  # contador
while d <= num:  # enqto variavel d for menor ou igual ele executa a repeticao
    if num % d == 0:  # verifica se a variavel d é divisor com resto 0 da variavel num
        print(d)  # printa se for divisor
    d += 1  # soma 1 ao contador até igualar ao número de entrada