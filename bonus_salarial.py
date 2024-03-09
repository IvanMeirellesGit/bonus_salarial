def obter_salario():
    while True:
        try:
            salario = float(input('Digite seu salário R$: '))
            return valida_salario(salario)
        except ValueError:
            print('Valor de salário digitado é inválido!')

def valida_salario(salario):
    try:
        if salario > 0:
            print(f'Valor do salário R${salario:.2f} é válido.')
            return salario
        else:
            print(f'Valor do Salário R${salario:.2f} é inválido.')
            # Se a entrada for inválida, o loop continua pedindo ao usuário para tentar novamente
            return None
    except TypeError:
        print(f'Valor do salário R${salario:.2f} é inválido.')
        return None

def obter_tempo():
    while True:
        try:
            tempo = float(input('Digite seu tempo de empresa: '))
            return valida_tempo(tempo)
        except ValueError:
            print('Tempo de empresa digitado é inválido!')

def valida_tempo(tempo):
    try:
        if tempo > 0:
            print(f'Tempo de empresa: {tempo} é válido.')
            return tempo
        else:
            print(f'O tempo de empresa deve ser um valor positivo.')
            # Se a entrada for inválida, o loop continua pedindo ao usuário para tentar novamente
            return None
    except TypeError:
        print(f'Tempo de empresa: {tempo} anos é inválido.')
        return None

def calcula_aumento_salario(salario, tempo):
    if salario is not None and tempo is not None:
        anos_de_aumento = tempo // 5
        aumento_acumulado = 1.05 ** anos_de_aumento
        novo_salario = salario * aumento_acumulado # Aumento de 5%
        print(f'Parabéns! Você recebeu um aumento de 5% no salário. Novo salário: R${novo_salario:.2f}')
    else:
        print('Você não recebeu aumento no salário.')

salario = obter_salario()
tempo = obter_tempo()
calcula_aumento_salario(salario, tempo)
