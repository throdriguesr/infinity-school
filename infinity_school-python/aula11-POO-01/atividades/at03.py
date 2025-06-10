'''
Crie uma classe Empresa que permita gerenciar funcionários. 
Os funcionários devem ter informações como nome, cargo e salário. 
A empresa deve ser capaz de adicionar, remover e listar funcionários.

'''

class Funcionario:
    def __init__(self, nome, cargo, salario):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario

class Empresa:
    def __init__(self, nome):
        self.nome = nome
        self.funcionarios = []

    def adicionar_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)

    def remover_funcionario(self, nome):
        self.funcionarios = [f for f in self.funcionarios if f.nome != nome]

    def listar_funcionarios(self):
        if not self.funcionarios:
            print("Nenhum funcionário cadastrado.")
        else:
            print(f"Funcionários da empresa {self.nome}:")
            for f in self.funcionarios:
                print(f"Nome: {f.nome}, Cargo: {f.cargo}, Salário: R${f.salario:.2f}")

empresa = Empresa("Tech Solutions")

func1 = Funcionario("João", "Desenvolvedor", 4500)
func2 = Funcionario("Maria", "Analista", 5200)

empresa.adicionar_funcionario(func1)
empresa.adicionar_funcionario(func2)

empresa.listar_funcionarios()

empresa.remover_funcionario("João")

empresa.listar_funcionarios()