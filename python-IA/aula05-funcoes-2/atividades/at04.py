'''
Crie uma função que aceita uma lista de números e use a função map para retornar uma nova lista contendo o dobro de cada número na lista de entrada.

'''

def dobrar_numeros(lista):
    return list(map(lambda x: x * 2, lista))

numeros = [1, 2, 3, 4, 5]

resultado = dobrar_numeros(numeros)

print(resultado)