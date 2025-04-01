'''
Analise de Produção anual.

Você tem um conjunto de dados que contém informações sobre a produção anual de diferentes culturas em diversas fazendas ao longo de vários anos. 

O objetivo é realizar uma análise simples desses dados usando apenas as funções agregadoras.

Tarefas: Encontre o ano em que a produção total foi máxima e o ano em que foi mínima. 
Identifique a cultura que teve a maior produção total e a cultura com a menor produção total ao longo dos anos. 
Encontre a fazenda que obteve a produção máxima em um determinado ano e a fazenda com a produção mínima no mesmo ano.

Construa seus próprios dados fictícios.

'''

# Dados fictícios: produção por ano (ano -> fazenda -> cultura -> produção)
producao_anual = {
    2020: {
        "Fazenda A": {"Milho": 1000, "Soja": 1500, "Trigo": 1200},
        "Fazenda B": {"Milho": 1100, "Soja": 1400, "Trigo": 1300},
    },
    2021: {
        "Fazenda A": {"Milho": 1200, "Soja": 1600, "Trigo": 1100},
        "Fazenda B": {"Milho": 1300, "Soja": 1550, "Trigo": 1250},
    },
    2022: {
        "Fazenda A": {"Milho": 900, "Soja": 1450, "Trigo": 1050},
        "Fazenda B": {"Milho": 950, "Soja": 1350, "Trigo": 1150},
    }
}

producao_por_ano = {ano: sum(sum(fazenda.values()) for fazenda in fazendas.values()) for ano, fazendas in producao_anual.items()}

ano_max = max(producao_por_ano, key=producao_por_ano.get)
ano_min = min(producao_por_ano, key=producao_por_ano.get)

producao_por_cultura = {}
for fazendas in producao_anual.values():
    for producoes in fazendas.values():
        for cultura, qtd in producoes.items():
            producao_por_cultura[cultura] = producao_por_cultura.get(cultura, 0) + qtd

cultura_max = max(producao_por_cultura, key=producao_por_cultura.get)
cultura_min = min(producao_por_cultura, key=producao_por_cultura.get)

ano_escolhido = 2021
fazendas_no_ano = producao_anual[ano_escolhido]

producao_por_fazenda = {fazenda: sum(producoes.values()) for fazenda, producoes in fazendas_no_ano.items()}

fazenda_max = max(producao_por_fazenda, key=producao_por_fazenda.get)
fazenda_min = min(producao_por_fazenda, key=producao_por_fazenda.get)

print("\nAno com maior produção total:", ano_max)
print("Ano com menor produção total:", ano_min)
print("\nCultura com maior produção total:", cultura_max)
print("Cultura com menor produção total:", cultura_min)
print(f"\nFazenda com maior produção em {ano_escolhido}:", fazenda_max)
print(f"Fazenda com menor produção em {ano_escolhido}:", fazenda_min)