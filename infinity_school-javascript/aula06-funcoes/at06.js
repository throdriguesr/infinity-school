// Atividade 06:
// Crie uma função chamada processarArray que receba um array de números e uma função de callback.
//
// 1 - A função processarArray deve aplicar o callback a cada elemento do array e retornar um novo array com os resultados.
// 2 - Crie duas funções de callback:
//     - dobrarNumero: recebe um número e retorna o dobro dele.
//     - raizQuadrada: recebe um número e retorna sua raiz quadrada.
// 3 - Use a função processarArray com o callback dobrarNumero para dobrar os valores de um array de números.
// 4 - Use processarArray com o callback raizQuadrada para calcular a raiz quadrada dos números.
// 5 - Exiba no console os arrays resultantes de cada operação.
//
// Objetivo:
// Praticar o uso de funções de callback, passando diferentes funções para realizar operações distintas em um array.

// Função principal que processa o array com base no callback fornecido
function processarArray(array, callback) {
  let novoArray = [];

  for (let item of array) {
    novoArray.push(callback(item));
  }

  return novoArray;
}

// Função de callback: dobra o número
function dobrarNumero(numero) {
  return numero * 2;
}

// Função de callback: calcula a raiz quadrada
function raizQuadrada(numero) {
  return Math.sqrt(numero);
}

// Array de exemplo
let numeros = [4, 9, 16, 25, 36];

// Processando com as duas funções de callback
let arrayDobrado = processarArray(numeros, dobrarNumero);
let arrayRaiz = processarArray(numeros, raizQuadrada);

// Exibindo os resultados no console
console.log("Array original:", numeros);
console.log("Valores dobrados:", arrayDobrado);
console.log("Raízes quadradas:", arrayRaiz);