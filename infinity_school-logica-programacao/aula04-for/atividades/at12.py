'''
Soma de Números com Desconto:
Peça ao usuário para inserir 5 preços de produtos. Use um laço for para
calcular o total. Aplique um desconto de 10% se o total ultrapassar 100 e
interrompa o loop com break.

'''

total = 0

for _ in range(5):
    preco = float(input("Digite o preço do produto: "))
    total += preco
    
    if total > 100:
        total *= 0.9  #Aplica o desconto de 10%
        break

print(f"\nTotal com desconto (se aplicável): {total:.2f}")