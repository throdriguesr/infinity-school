'''
Crie um programa que recebe dois conjuntos e exibe a interseção deles.

'''

conjunto_a = {int(x) for x in input("Digite os elementos do primeiro conjunto separados por espaço: ").split()}
conjunto_b = {int(x) for x in input("Digite os elementos do segundo conjunto separados por espaço: ").split()}

intersecao = conjunto_a & conjunto_b

print("\nA interseção dos dois conjuntos é:", intersecao)