'''
Contagem de Vogais em uma Palavra:
Crie um programa que solicite uma palavra ao usuário e use um laço for com
uma condicional para contar quantas vogais (a, e, i, o, u) a palavra contém.

'''

palavra = input("Digite uma palavra: ")
vogais = 0

for letra in palavra.lower():
    if letra in "aeiou":
        vogais += 1

print(f"\nA palavra '{palavra}' contém {vogais} vogais.")