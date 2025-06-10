'''
Dada uma lista de números, crie uma nova lista contendo apenas os números pares.

'''

numeros = input("Digite os números separados por espaço: ")  
numeros = list(map(int, numeros.split()))  

pares = []  

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)  

print("Números pares:", pares)