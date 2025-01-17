'''
Crie uma tupla para representar as informações de três palestrantes, cada uma contendo o nome, o tema da
palestra e a instituição à qual estão vinculados.

Exiba na tela as informações do terceiro palestrante, incluindo nome, tema da palestra e instituição.

'''

palestrantes = (
    ('Thiago Rodrigues', 'Engenharia de Software', 'Universidade A'),
    ('Helena Lima', 'Engenharia Civil', 'Instituto B'),
    ('Beatriz Rodrigues', 'Biomedicina', 'Faculdade C'),
)

nome, tema, instituicao = palestrantes[2]
print(f'Nome: {nome}\nTema: {tema}\nInstituição: {instituicao}')