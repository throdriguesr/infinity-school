'''
Você possui dados de vendas trimestrais de uma empresa em uma lista. 
Cada trimestre é representado como uma lista de números, onde cada número representa o valor de vendas de um mês (janeiro a março, abril a junho, julho a setembro e outubro a dezembro).

Você deve realizar as seguintes tarefas:

- Calcule a média de vendas por trimestre.
- Encontre o trimestre com a maior soma de vendas.
- Encontre o trimestre com a menor soma de vendas.
- Calcule o total de vendas no ano inteiro.

Construa seus dados fictícios.

'''

# Dados fictícios: vendas por trimestre (cada número representa um mês)
vendas_trimestrais = [
    [10000, 12000, 11000],  # 1º trimestre (jan-mar)
    [15000, 14000, 13000],  # 2º trimestre (abr-jun)
    [16000, 17000, 18000],  # 3º trimestre (jul-set)
    [9000,  9500,  9700]    # 4º trimestre (out-dez)
]

somas = [sum(trimestre) for trimestre in vendas_trimestrais]

medias = [soma / 3 for soma in somas]

maior_trimestre = somas.index(max(somas)) + 1
menor_trimestre = somas.index(min(somas)) + 1

total_anual = sum(somas)

print("\nMédia de vendas por trimestre:", medias)
print("Trimestre com maior soma de vendas:", maior_trimestre)
print("Trimestre com menor soma de vendas:", menor_trimestre)
print("Total de vendas no ano:", total_anual)