// Atividade 05
// Crie um script que contenha um array de nomes e utilize o loop for...of
// para percorrê-lo. Para cada nome no array, exiba uma mensagem de
// boas-vindas personalizada no console.
//
// Objetivo:
// Praticar o uso do loop for...of para percorrer arrays e exibir mensagens
// personalizadas.

let nomes = ["Ana", "Bruno", "Carla", "Diego", "Elaine"];

for (let nome of nomes) {
  console.log("Bem-vindo(a), " + nome + "!");
}