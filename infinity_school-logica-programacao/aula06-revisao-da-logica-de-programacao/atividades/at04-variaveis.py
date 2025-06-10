'''
Cálculo de Juros Simples:
Crie um programa que calcule o valor futuro de um investimento
usando a fórmula de juros simples. Peça ao usuário para digitar o
capital inicial, a taxa de juros e o tempo de aplicação.

'''

capital_inicial = float(input("Digite o capital inicial (em reais): "))

taxa_juros = float(input("Digite a taxa de juros (em % ao ano): "))

tempo = float(input("Digite o tempo de aplicação (em anos): "))

valor_futuro = capital_inicial * (1 + (taxa_juros / 100) * tempo)

print(f"\nO valor futuro do investimento é R$ {valor_futuro:.2f}")