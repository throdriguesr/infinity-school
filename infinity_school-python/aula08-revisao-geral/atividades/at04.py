'''
Crie uma função que receba uma lista de strings e retorne uma nova lista contendo apenas as strings palíndromos.

'''

def eh_palindromo(palavra):
    return palavra == palavra[::-1]

palavras = input("Digite palavras separadas por espaço: ").split()
palindromos = [p for p in palavras if eh_palindromo(p)]

print("\nPalavras palíndromas:", palindromos if palindromos else "Nenhuma")