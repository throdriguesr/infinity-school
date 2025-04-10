'''
Crie uma classe base chamada "Animal" com um método "emitirSom".

Em seguida, crie classes derivadas como "Cachorro, "Gato" e "Pássaro" que herdem de "Animal" e sobrescrevam o método "emitirSom" para cada tipo de animal.

Crie uma lista de animais e percorra-a, chamando o método "emitirSom" para cada animal. 

Demonstre como o polimorfismo permite que diferentes tipos de animais emitam seus sons de maneira uniforme.

'''

class Animal:
    def emitirSom(self):
        pass

class Cachorro(Animal):
    def emitirSom(self):
        print("Cachorro: Au au!")

class Gato(Animal):
    def emitirSom(self):
        print("Gato: Miau!")

class Passaro(Animal):
    def emitirSom(self):
        print("Pássaro: Piu piu!")

animais = [Cachorro(), Gato(), Passaro()]

for animal in animais:
    animal.emitirSom()