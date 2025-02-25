import manipulacao_strings

texto = input("Digite uma frase ou palavra: ")

print("\nString invertida:", manipulacao_strings.inverter_string(texto))
print("Número de palavras:", manipulacao_strings.contar_palavras(texto))

if manipulacao_strings.eh_palindromo(texto):
    print("É um palíndromo!")
else:
    print("Não é um palíndromo.")