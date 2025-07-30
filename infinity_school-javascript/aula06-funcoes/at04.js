// Atividade 04:
// Crie uma função chamada saudacao que receba um parâmetro nome
// e retorne uma string de saudação no formato "Olá, [nome]!".

// Em seguida:
// 1. Chame a função saudacao passando diferentes nomes.
// 2. Exiba o resultado no console.

// Objetivo:
// Praticar o uso de funções com lógica condicional e manipulação de arrays.

function saudacao(nome) {
  // Se nenhum nome for passado, retorna uma saudação padrão
  if (!nome) {
    return "Olá, visitante!";
  }

  return "Olá, " + nome + "!";
}

// Lista de nomes para testar a função
let nomes = ["Thiago", "Rodrigues", "Ribeiro", "Helena", ""];

// Percorre o array de nomes e exibe as saudações no console
for (let nome of nomes) {
  console.log(saudacao(nome));
}