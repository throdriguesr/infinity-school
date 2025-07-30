// Atividade 03:
// Crie uma função chamada calcularSoma que utilize o rest operator para aceitar um número
// indefinido de parâmetros e calcular a soma de todos eles.
// Chame a função com diferentes quantidades de números e exiba o resultado no console.

// Objetivo:
// O console deve exibir a soma dos números passados para a função.

function calcularSoma(...numeros) {
  // Cria uma variável para armazenar a soma
  let total = 0;

  // Percorre todos os números e soma um a um
  for (let numero of numeros) {
    total += numero;
  }

  // Retorna o total da soma
  return total;
}

// Chamando a função com diferentes quantidades de números
console.log("Soma 1:", calcularSoma(2, 4)); 
console.log("Soma 2:", calcularSoma(10, 20, 30));
console.log("Soma 3:", calcularSoma(1, 2, 3, 4, 5, 6));