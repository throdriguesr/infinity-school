'''
Algoritmo de Cálculo de Desconto:
Desenvolva um algoritmo que calcule o preço de um produto
após aplicar um desconto. Solicite o preço original e o percentual
de desconto.

'''

preco_original = float(input("Digite o preço original do produto (em reais): "))

percentual_desconto = float(input("Digite o percentual de desconto (%): "))

preco_com_desconto = preco_original * (1 - (percentual_desconto / 100))

print(f"\nO preço com desconto é R$ {preco_com_desconto:.2f}")