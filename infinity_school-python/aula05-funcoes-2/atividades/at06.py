'''
Crie uma função que aceita uma lista de strings e use a função reduce (importada de functools) para encontrar a maior string na lista.

'''

from functools import reduce

def maior_string(lista):
    return reduce(lambda a, b: a if len(a) > len(b) else b, lista)

palavras = ["Python", "Java", "JavaScript", "C", "HTML", "CSS"]

resultado = maior_string(palavras)

print(resultado)