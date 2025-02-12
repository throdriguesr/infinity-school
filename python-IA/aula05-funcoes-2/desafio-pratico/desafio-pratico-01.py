'''
DESAFIO PRÁTICO

Processador de Texto - passo 1

Crie um processador de texto simples que realiza várias operações em um texto de entrada, como contar palavras, contar letras, inverter o texto e substituir palavras-chave.

Requisitos:

Crie uma função chamada processador_texto que aceite uma string de texto como argumento.

'''

def processador_texto(texto):
    palavras = texto.split()
    letras = sum(c.isalpha() for c in texto)
    invertido = texto[::-1]

    return len(palavras), letras, invertido

texto_a_inverter = str(input("Digite o texto: "))
palavras, letras, invertido = processador_texto(texto_a_inverter)

print(f"\nContagem de palavras: {palavras}")
print(f"Contagem de letras: {letras}")
print(f"Texto invertido: {invertido}")