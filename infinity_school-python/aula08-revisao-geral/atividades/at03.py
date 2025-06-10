'''
Crie um conjunto com nomes de cores. 
Implemente uma função que retorne as cores que têm mais de quatro letras.

'''

def cores_maiores_que_quatro(cores):
    cores_filtradas = set()
    for cor in cores:
        if len(cor) > 4:
            cores_filtradas.add(cor)
    return cores_filtradas

cores = {"azul", "verde", "amarelo", "preto", "branco", "roxo", "laranja"}
resultado = cores_maiores_que_quatro(cores)
print(resultado)