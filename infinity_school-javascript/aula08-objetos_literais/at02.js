/*
Atividade 02
Crie um objeto chamado pessoa com as propriedades nome, idade, e profissao.

Em seguida:
Altere a propriedade profissao para um novo valor.
Adicione uma nova propriedade chamada cidade ao objeto.
Exiba no console o objeto completo após as modificações.

Objetivo:
Praticar a manipulação de objetos, alterando propriedades existentes, adicionando novas propriedades, e exibindo o objeto atualizado.
*/

let pessoa = {
    nome: "Thiago",
    idade: 30,
    profissao: "Engenheiro de Software"
};

pessoa.profissao = "Engenheiro de Dados";

pessoa.cidade = "Belo Horizonte";

console.log(pessoa);