// função para buscar dados da API
function buscarDados() {
  fetch("https://jsonplaceholder.typicode.com/users/1") // exemplo de API
    .then(response => {
      // verifica status da resposta
      if (response.ok) {
        return response.json(); // converte para JSON se status 200
      } else if (response.status === 404) {
        throw new Error("Recurso não encontrado"); // lança erro 404
      } else {
        throw new Error("Erro ao carregar os dados"); // outros erros
      }
    })
    .then(data => {
      // mostra dados no console
      console.log("Dados recebidos:", data);
    })
    .catch(erro => {
      // mostra mensagem de erro
      console.error(erro.message);
    });
}

// chama a função
buscarDados();