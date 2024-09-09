faturamento = {}
faturamento["SP"] = 67836.43
faturamento["RJ"] = 36678.66
faturamento["MG"] = 29229.88
faturamento["ES"] = 27165.48
faturamento["Outros"] = 19849.53

def percentual(estado):
    return (faturamento[estado] / sum(faturamento.values())) * 100

def main():
    print(f'O percentual de representação de São Paulo no valor total foi {percentual("SP"):.2f}%')

    print(f'O percentual de representação do Rio de Janeiro no valor total foi {percentual("RJ"):.2f}%')

    print(f'O percentual de representação de Minas Gerais no valor total foi {percentual("MG"):.2f}%')
    
    print(f'O percentual de representação do Espírito Santo no valor total foi {percentual("ES"):.2f}%')
    
    print(f'O percentual de representação dos outros estados no valor total foi {percentual("Outros"):.2f}%')

main()