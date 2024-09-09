import json

# Função para calcular o menor valor
def min_value(data):
    min_valor = data[0]['valor']
    for i in data:
        if i['valor'] < min_valor and i['valor'] > 0:
            min_valor = i['valor']
    return min_valor

# Função para calcular o maior valor
def max_value(data):
    max_valor = data[0]['valor']
    for i in data:
        if i['valor'] > max_valor:
            max_valor = i['valor']
    return max_valor

# Função para calcular a média excluindo valores zero
def mean(data):
    soma = 0
    contagem = 0
    for i in data:
        if i['valor'] > 0:
            soma += i['valor']
            contagem += 1
    return soma / contagem if contagem > 0 else 0

# Função para contar os dias com faturamento acima da média
def great_days(data, media):
    contagem = 0
    for i in data:
        if i['valor'] > media:
            contagem += 1
    return contagem

def main():
    # Carregar o arquivo JSON
    with open('dados.json', 'r') as arquivo:
        data = json.load(arquivo)

    menor_faturamento = min_value(data)
    maior_faturamento = max_value(data)
    media_faturamento = mean(data)
    dias_acima_media = great_days(data, media_faturamento)

    print(f'O menor faturamento foi: {menor_faturamento}')
    print(f'O maior faturamento foi: {maior_faturamento}')
    print(f'A média de faturamento foi: {media_faturamento}')
    print(f'{dias_acima_media} dias tiveram faturamento acima da média')

main()
