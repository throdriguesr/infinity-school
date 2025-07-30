// Atividade 02:
// Crie uma função chamada calcularDesconto que receba dois parâmetros: preco e desconto.
// A função deve calcular o preço final do produto após aplicar o desconto e retornar esse valor.
// Chame a função com diferentes valores e exiba o resultado no console.

// Objetivo:
// Desenvolver a compreensão de funções com múltiplos parâmetros em JavaScript,
// praticando cálculos matemáticos simples e o retorno de valores.

function calcularDesconto(preco, desconto) {
  // Calcula o valor do desconto
  let valorDesconto = preco * (desconto / 100);

  // Calcula o preço final
  let precoFinal = preco - valorDesconto;

  // Retorna o valor final
  return precoFinal;
}

// Chamando a função com diferentes valores
console.log("Preço final: R$", calcularDesconto(100, 10)); // Deve mostrar 90
console.log("Preço final: R$", calcularDesconto(250, 20)); // Deve mostrar 200
console.log("Preço final: R$", calcularDesconto(80, 5));   // Deve mostrar 76