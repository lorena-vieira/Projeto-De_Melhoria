def get_user_input():
    km = input("Informe o Km da OAE: ")
    linha = input("Informe a linha: ")
    cidade = input("Informe a cidade: ")
    estado = input("Informe o estado: ")
    natureza_transposicao = input("Informe a natureza da transposição: ")
    bitola = input("Informe a bitola: ")
    tracado = input("Informe o traçado: ")
    trilhos = input("Informe os trilhos: ")
    fixacao = input("Informe a fixação: ")
    comprimento = input("Informe o comprimento: ")
    largura = input("Informe a largura: ")
    altura = input("Informe a altura: ")

    return {
        'km': km,
        'linha': linha,
        'cidade': cidade,
        'estado': estado,
        'natureza_transposicao': natureza_transposicao,
        'bitola': bitola,
        'tracado': tracado,
        'trilhos': trilhos,
        'fixacao': fixacao,
        'comprimento': comprimento,
        'largura': largura,
        'altura': altura,
    }







