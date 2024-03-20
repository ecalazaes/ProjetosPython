print(f'Questão 4)\n')
idades = 0
participantes = 0
while True:
    idade = int(input('Entre com a sua idade: '))
    if idade == 0:
        print(f'Idade deve ser maior que zero.')
    elif idade > 0:
        idades += idade  # soma o valor da idade a variavel idades
        participantes += 1  # soma a qtd de entradas para a variavel participantes
    else:
        print(f'Colhetamos a idade de {participantes} pessoas e a média entre elas é de {idades/participantes:.2f}.')
        break