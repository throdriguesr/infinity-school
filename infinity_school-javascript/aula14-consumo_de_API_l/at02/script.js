// Criação do array de produtos
const produtos = [
  { nome: "Arroz", preco: 12.5 },
  { nome: "Feijão", preco: 8.3 },
  { nome: "Macarrão", preco: 4.9 }
];

// Conversão do array para string JSON
const produtosJSON = JSON.stringify(produtos);

// Exibição no console
console.log(produtosJSON);