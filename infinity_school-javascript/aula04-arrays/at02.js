// Atividade 02
// Crie um array chamado animais contendo os seguintes elementos:
// Cachorro, Gato, Papagaio. Em seguida:
//
// Adicione o elemento Tartaruga ao final do array.
// Remova o primeiro elemento e adicione o elemento Coelho no início.
// Depois, substitua o elemento na posição 2 por Hamster.
// Exiba o comprimento atual do array.
// Acesse e exiba no console o elemento na posição 1.
// Finalmente, exiba o array final no console.
//
// Objetivo:
// Praticar operações básicas de criação, acesso e modificação de elementos
// em arrays.

let animais = ["Cachorro", "Gato", "Papagaio"];

animais.push("Tartaruga");
animais.shift();
animais.unshift("Coelho");
animais[2] = "Hamster";

console.log(animais.length);
console.log(animais[1]);
console.log(animais);