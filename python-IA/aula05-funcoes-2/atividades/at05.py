'''
Crie uma função que aceita uma lista de números e use a função filter para retornar uma nova lista contendo apenas os números pares da lista de entrada.

'''

def filtrar_pares(lista):
    return list(filter(lambda x: x % 2 == 0, lista))

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

resultado = filtrar_pares(numeros)

print(resultado)