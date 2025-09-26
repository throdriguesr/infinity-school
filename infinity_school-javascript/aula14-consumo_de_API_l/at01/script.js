// Criação do objeto pessoa
const pessoa = {
  nome: "Thiago",
  idade: 30,
  cidade: "Belo Horizonte"
};

// Conversão do objeto para string JSON
const pessoaJSON = JSON.stringify(pessoa);

// Exibição no console
console.log(pessoaJSON);