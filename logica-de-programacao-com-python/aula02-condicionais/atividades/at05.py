'''
Atividade 05:
Desconto em Preço:
Peça ao usuário para inserir o preço de um produto e, em seguida,
use o operador de atribuição -= para aplicar um desconto de 5%.

'''

produto = float(input("Digite o valor do produto: R$ "))

produto -= produto * 0.05

print(f"\nO produto com 5% de desconto é: R$ {produto:.2f}")