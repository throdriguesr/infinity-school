/*
PRATIQUE E APRENDA

Crie uma pequena aplicação em JavaScript que analise um conjunto de dados utilizando métodos auxiliares de
arrays (forEach(), map(), filter(), reduce(), some(), find(), every()). O projeto deve incluir operações como filtragem
de dados, transformação de informações e cálculo de estatísticas.

Escolha dos Dados: Defina um array com dados fictícios, representando produtos, usuários, ou transações.

Análise de Dados: Utilize métodos auxiliares de arrays para:
Filtrar itens que atendem a certos critérios.
Transformar dados para facilitar a análise (ex.: calcular o preço com desconto).
Somar valores ou calcular médias utilizando reduce().
Verificar condições gerais ou específicas com some(), every(), ou find().

Uso de IA: Durante o desenvolvimento, utilize uma ferramenta de inteligência artificial para:
Solicitar exemplos e explicações sobre os métodos de arrays.
Obter ajuda para depurar e otimizar o código.
Buscar ideias para aprimorar a funcionalidade e eficiência do projeto.
*/

// Array de dados fictícios: produtos de uma loja
const produtos = [
    { nome: "Camisa", preco: 50, quantidade: 10 },
    { nome: "Calça", preco: 100, quantidade: 5 },
    { nome: "Tênis", preco: 150, quantidade: 8 },
    { nome: "Boné", preco: 25, quantidade: 20 },
    { nome: "Meias", preco: 10, quantidade: 50 }
];

// 1. forEach() - listar produtos e estoque
console.log("Lista de produtos e estoque:");
produtos.forEach(function(produto) {
    console.log(`${produto.nome} - Preço: R$${produto.preco}, Quantidade: ${produto.quantidade}`);
});

// 2. map() - calcular preço com 10% de desconto
const produtosComDesconto = produtos.map(function(produto) {
    return {
        nome: produto.nome,
        precoComDesconto: produto.preco * 0.9, // 10% de desconto
        quantidade: produto.quantidade
    };
});
console.log("\nProdutos com desconto de 10%:");
console.log(produtosComDesconto);

// 3. filter() - produtos com preço acima de 50
const produtosCaros = produtos.filter(function(produto) {
    return produto.preco > 50;
});
console.log("\nProdutos com preço acima de R$50:");
console.log(produtosCaros);

// 4. reduce() - calcular valor total do estoque
const valorTotalEstoque = produtos.reduce(function(acumulador, produto) {
    return acumulador + (produto.preco * produto.quantidade);
}, 0);
console.log("\nValor total do estoque: R$", valorTotalEstoque);

// 5. some() - verificar se há produtos com preço menor que 20
const temProdutosBaratos = produtos.some(function(produto) {
    return produto.preco < 20;
});
console.log("\nHá produtos com preço menor que R$20?", temProdutosBaratos);

// 6. find() - encontrar o primeiro produto com quantidade menor que 10
const produtoPoucoEstoque = produtos.find(function(produto) {
    return produto.quantidade < 10;
});
console.log("\nPrimeiro produto com estoque menor que 10:");
console.log(produtoPoucoEstoque);

// 7. every() - verificar se todos os produtos têm preço acima de 5
const todosAcimaDeCinco = produtos.every(function(produto) {
    return produto.preco > 5;
});
console.log("\nTodos os produtos têm preço acima de R$5?", todosAcimaDeCinco);