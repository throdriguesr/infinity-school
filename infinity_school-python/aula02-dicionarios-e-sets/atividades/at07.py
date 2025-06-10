'''
Escreva um programa que receba duas listas e calcule
a união dos elementos únicos dessas listas, usando conjuntos.

'''

lista_a = input("Digite os elementos da primeira lista separados por espaço: ").split()
lista_b = input("Digite os elementos da segunda lista separados por espaço: ").split()

conjunto_a = set(lista_a)
conjunto_b = set(lista_b)

uniao = conjunto_a | conjunto_b

print("A união dos elementos únicos das duas listas é:", uniao)