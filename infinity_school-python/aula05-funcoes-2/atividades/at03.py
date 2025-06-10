'''
Crie uma função chamada concatenar_strings que aceita um número variável de strings como argumentos posicionais (usando *args). A função deve concatenar todas as strings em uma única string e retorná-la.

'''

def concatenar_strings(*args):
    resultado = ""
    for string in args:
        resultado += string  # Adiciona cada string à variável resultado
    return resultado

# Exemplo de uso
resultado = concatenar_strings("Olá, ", "Thiago! ", "Como ", "você ", "está?")
print(resultado)