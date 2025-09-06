/*
Atividade Prática
Crie uma classe chamada Carro que tenha as seguintes propriedades e métodos:

Propriedades:
marca: uma string que representa a marca do carro.
modelo: uma string que representa o modelo do carro.
ano: um número que representa o ano de fabricação do carro.

Métodos:
detalhes(): Este método deve exibir no console uma mensagem no formato
"Carro: [marca] [modelo], Ano: [ano]".

Requisitos:
Crie dois objetos (instâncias) da classe Carro com diferentes valores para as propriedades
marca, modelo, e ano.
Chame o método detalhes() para ambos os objetos e exiba as informações no console.

Objetivo:
Praticar a criação de classes e objetos em JavaScript, além de manipular métodos e propriedades
dentro de uma classe
*/

// Classe Carro com propriedades e método
class Carro {
  // Construtor para inicializar as propriedades
  constructor(marca, modelo, ano) {
    this.marca = marca;
    this.modelo = modelo;
    this.ano = ano;
  }

  // Método que mostra os detalhes do carro
  detalhes() {
    console.log(`Carro: ${this.marca} ${this.modelo}, Ano: ${this.ano}`);
  }
}

// Criação do primeiro objeto da classe Carro
const carro1 = new Carro("Toyota", "Corolla", 2020);

// Criação do segundo objeto da classe Carro
const carro2 = new Carro("Honda", "Civic", 2022);

// Exibindo os detalhes dos dois carros
carro1.detalhes();
carro2.detalhes();