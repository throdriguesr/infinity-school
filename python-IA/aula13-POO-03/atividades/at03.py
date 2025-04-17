'''
Crie uma classe Aluno em Python com atributos privados, como nome, idade e matrícula. Implemente métodos públicos para acessar e modificar esses atributos. 
Em seguida, crie uma instância da classe e demonstre como usar os métodos de acesso.

'''

class Aluno:
    def __init__(self, nome, idade, matricula):
        self.__nome = nome
        self.__idade = idade
        self.__matricula = matricula

    def get_nome(self):
        return self.__nome

    def set_nome(self, novo_nome):
        self.__nome = novo_nome

    def get_idade(self):
        return self.__idade

    def set_idade(self, nova_idade):
        self.__idade = nova_idade

    def get_matricula(self):
        return self.__matricula

    def set_matricula(self, nova_matricula):
        self.__matricula = nova_matricula

aluno1 = Aluno("Lucas", 20, "2025001")
print("Nome:", aluno1.get_nome())
print("Idade:", aluno1.get_idade())
print("Matrícula:", aluno1.get_matricula())

aluno1.set_nome("Lucas Silva")
aluno1.set_idade(21)
aluno1.set_matricula("2025002")

print("Novo nome:", aluno1.get_nome())
print("Nova idade:", aluno1.get_idade())
print("Nova matrícula:", aluno1.get_matricula())