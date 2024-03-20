print(f'Questão 7)\n')
n1 = 1
n2 = 1
qtd_sequencia = -1
while qtd_sequencia <= 0:
    qtd_sequencia = int(input(f'Digite a quantidade de numeros da sequência Fibonacci: '))
    if qtd_sequencia <= 0:
        print(f'Digite um número maior que zero.')
    elif qtd_sequencia == 1:
        print(f'O primeiro termo da sequência Fibonnaci é {n1}.')
    else:
        print(f'Sequência Fibonacci com {qtd_sequencia} termos:')
        print(n1)
        print(n2)
        for i in range(2, qtd_sequencia):
            proximo_numero = n1 + n2
            print(proximo_numero)
            n1 = n2
            n2 = proximo_numero
