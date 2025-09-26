// array original de produtos
const produtos = [
  { nome: "Camisa", preco: 50 },
  { nome: "Calça", preco: 80 },
  { nome: "Sapato", preco: 120 }
];

// cria um novo array aplicando 10% de desconto
const produtosComDesconto = produtos.map(produto => {
  return {
    nome: produto.nome,
    preco: produto.preco * 0.9 // aplica 10% de desconto
  };
});

// exibe o array original
console.log("Produtos originais:", produtos);

// exibe o array com preços atualizados
console.log("Produtos com desconto:", produtosComDesconto);