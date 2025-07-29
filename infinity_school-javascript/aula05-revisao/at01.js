// [Atividade 01]
// Crie um arquivo JavaScript e siga os passos abaixo para
// praticar a declaração e uso de variáveis com var, let e const.
//
// Objetivo:
// Entender a diferença entre var, let e const, exercitar a reatribuição de
// valores em variáveis e compreender o comportamento de constantes.
//
// Declare três variáveis:
// - Uma variável nome usando var com seu nome.
// - Uma variável idade usando let com sua idade.
// - Uma constante cidade usando const com o nome da cidade onde você mora.
//
// Exiba os valores das variáveis no console usando console.log().
// Altere o valor da variável nome para um novo nome.
// Reatribua o valor da variável idade para um novo número.
// Tente alterar o valor da constante cidade e veja o que acontece.
// Exiba novamente os valores de nome e idade no console.

var nome = "Thiago";
let idade = 30;
const cidade = "Belo Horizonte";

console.log("Nome:", nome);
console.log("Idade:", idade);
console.log("Cidade:", cidade);

// Reatribuição
nome = "Rodrigues";
idade = 31;

// Tentar alterar uma constante (vai gerar erro)
// cidade = "São Paulo"; // Descomente esta linha para ver o erro

console.log("Novo nome:", nome);
console.log("Nova idade:", idade);