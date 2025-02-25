def inverter_string(texto):
    return texto[::-1]

def contar_palavras(texto):
    palavras = texto.split()
    return len(palavras)

def eh_palindromo(texto):
    texto = texto.lower().replace(" ", "")
    return texto == texto[::-1]