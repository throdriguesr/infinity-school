'''
Verificar Múltiplos de 5 e Parar:
Escreva um programa que use um laço for para imprimir números de 1 a 30.
Use uma condicional para verificar se um número é múltiplo de 5 e outro
para verificar se é maior que 20 e interromper o loop com break.

'''

for numero in range(1, 31):
    if numero % 5 == 0:
        print(f"{numero} é múltiplo de 5")
    
    if numero > 20:
        break