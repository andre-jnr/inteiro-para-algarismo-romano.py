def converter_para_romanos(numero):
    romanos = {
        1: 'I',
        4: 'IV',
        5: 'V',
        9: 'IX',
        10: 'X',
        40: 'XL',
        50: 'L',
        90: 'XC',
        100: 'C',
        400: 'CD',
        500: 'D',
        900: 'CM',
        1000: 'M'
    }

    resultado = ''
    while numero >= 1:
        for chave in romanos.keys():
            if chave <= numero:
                maior_possivel = chave
        numero -= maior_possivel
        resultado += romanos[maior_possivel]

    return resultado


while True:
    print('=' * 43)
    print('CONVERSOR DE ALGARISMOS ROMANOS EM INTEIROS')
    valor_usuario = int((input('Digite um número: ')))
    print('=' * 43)

    algarismo_romano = converter_para_romanos(valor_usuario)

    print('-' * 18)
    print(f'ARABICO: {valor_usuario}')
    print(f'ROMANO: {algarismo_romano}')
    print('-' * 18)

    opcao_usuario = 3
    while opcao_usuario not in [1, 2]:
        print('Deseja verificar mais algum número?')
        print(f"{'[1] - SIM':^35}")
        print(f"{'[2] - NÃO':^35}")
        opcao_usuario = int(input('-> '))
        if opcao_usuario not in [1, 2]:
            print()
            print('Não entendi!')
    if opcao_usuario == 2:
        print('Tchau, tenha um otimo dia.')
        break
