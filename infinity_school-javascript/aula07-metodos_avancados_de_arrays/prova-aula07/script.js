/*
[JSIA-A07]  
Crie um programa em JavaScript que gerencie uma lista de nomes utilizando diversos métodos auxiliares de arrays para realizar operações como adicionar, filtrar, encontrar e transformar os dados.

Requisitos do Projeto:
* Adicionar Nomes:
 - Permita ao usuário adicionar nomes à lista utilizando o método push().
 - Exiba a lista atualizada no console.

* Filtrar Nomes:
- Use o método filter() para criar uma nova lista contendo apenas os nomes que começam com uma letra específica fornecida pelo usuário.
 - Exiba os nomes filtrados no console.

* Buscar um Nome Específico:
- Use o método find() para localizar o primeiro nome na lista que corresponde exatamente a um valor fornecido pelo usuário.
 - Exiba o resultado no console ou uma mensagem informando que o nome não foi encontrado.

* Transformar Nomes:
- Utilize o método map() para transformar todos os nomes da lista em letras maiúsculas.
 - Exiba a nova lista no console.

* Verificar Condições:
 - Use o método every() para verificar se todos os nomes têm mais de três caracteres.
 - Exiba a resposta (true ou false) no console.

* Interação Contínua: 
 - Implementado através de botões e inputs no HTML.
*/

const nomes = [];
const resultado = document.getElementById("resultado");

function adicionarNome() {
    const nome = document.getElementById("inputNome").value.trim();
    if (nome) {
        nomes.push(nome);
        resultado.textContent = `Nome adicionado! Lista atualizada:\n${nomes.join(", ")}`;
        document.getElementById("inputNome").value = "";
    } else {
        resultado.textContent = "Digite um nome válido.";
    }
}

function filtrarNomes() {
    const letra = document.getElementById("inputLetra").value.trim().toLowerCase();
    if (letra) {
        const filtrados = nomes.filter(nome => nome.toLowerCase().startsWith(letra));
        resultado.textContent = `Nomes filtrados (iniciando com '${letra}'):\n${filtrados.join(", ") || "Nenhum encontrado"}`;
    } else {
        resultado.textContent = "Digite uma letra válida para filtrar.";
    }
}

function buscarNome() {
    const busca = document.getElementById("inputBusca").value.trim();
    if (busca) {
        const encontrado = nomes.find(nome => nome === busca);
        resultado.textContent = encontrado ? `Nome encontrado: ${encontrado}` : "Nome não encontrado.";
    } else {
        resultado.textContent = "Digite um nome válido para buscar.";
    }
}

function transformarNomes() {
    if (nomes.length > 0) {
        const maiusculas = nomes.map(nome => nome.toUpperCase());
        resultado.textContent = `Nomes em maiúsculas:\n${maiusculas.join(", ")}`;
    } else {
        resultado.textContent = "A lista de nomes está vazia.";
    }
}

function verificarNomes() {
    if (nomes.length > 0) {
        const todosMaioresQueTres = nomes.every(nome => nome.length > 3);
        resultado.textContent = `Todos os nomes têm mais de 3 caracteres? ${todosMaioresQueTres}`;
    } else {
        resultado.textContent = "A lista de nomes está vazia.";
    }
}