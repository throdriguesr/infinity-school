// dados simulados da API
const apiSimulada = {
  1: [
    { nome: "Camisa", preco: 50, estoque: 10, dataLancamento: "2025-01-10" },
    { nome: "Calça", preco: 80, estoque: 0, dataLancamento: "2025-02-15" },
    { nome: "Sapato", preco: 120, estoque: 5, dataLancamento: "2025-03-05" }
  ],
  2: [
    { nome: "Boné", preco: 25, estoque: 8, dataLancamento: "2025-01-20" },
    { nome: "Meias", preco: 12, estoque: 0, dataLancamento: "2025-02-18" },
    { nome: "Jaqueta", preco: 150, estoque: 2, dataLancamento: "2025-03-10" }
  ],
  3: [
    { nome: "Camiseta", preco: 40, estoque: 12, dataLancamento: "2025-01-25" },
    { nome: "Tênis", preco: 200, estoque: 3, dataLancamento: "2025-02-22" },
    { nome: "Short", preco: 35, estoque: 0, dataLancamento: "2025-03-15" }
  ]
};

let paginaAtual = 1;
let filtroAtivo = false;

const tabela = document.getElementById("tabelaProdutos");
const mensagemErro = document.getElementById("mensagemErro");
const paginaSpan = document.getElementById("paginaAtual");

// função para simular fetch da API
function fetchProdutos(pagina) {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      const dados = apiSimulada[pagina];
      if (dados) {
        resolve(dados);
      } else {
        reject(new Error("Erro ao carregar os produtos"));
      }
    }, 800); // delay simulado
  });
}

// função para formatar preço
function formatarPreco(valor) {
  return valor.toLocaleString("pt-BR", { style: "currency", currency: "BRL" });
}

// função para formatar data
function formatarData(data) {
  const d = new Date(data);
  return d.toLocaleDateString("pt-BR");
}

// função para atualizar tabela
function atualizarTabela() {
  mensagemErro.textContent = "";
  tabela.innerHTML = "";

  fetchProdutos(paginaAtual)
    .then(produtos => {
      if (filtroAtivo) {
        produtos = produtos.filter(p => p.estoque > 0);
      }

      produtos.forEach(p => {
        const tr = document.createElement("tr");
        tr.innerHTML = `
          <td>${p.nome}</td>
          <td>${formatarPreco(p.preco)}</td>
          <td>${p.estoque}</td>
          <td>${formatarData(p.dataLancamento)}</td>
        `;
        tabela.appendChild(tr);
      });

      paginaSpan.textContent = paginaAtual;
    })
    .catch(erro => {
      mensagemErro.textContent = erro.message;
    });
}

// eventos dos botões
document.getElementById("proximo").addEventListener("click", () => {
  if (paginaAtual < 3) {
    paginaAtual++;
    atualizarTabela();
  }
});

document.getElementById("anterior").addEventListener("click", () => {
  if (paginaAtual > 1) {
    paginaAtual--;
    atualizarTabela();
  }
});

document.getElementById("filtroEstoque").addEventListener("click", () => {
  filtroAtivo = !filtroAtivo;
  atualizarTabela();
});

// inicializa tabela
atualizarTabela();