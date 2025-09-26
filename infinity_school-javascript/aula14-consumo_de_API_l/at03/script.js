// função para buscar usuários da API
function buscarUsuarios() {
  // faz a requisição GET
  fetch("https://jsonplaceholder.typicode.com/users")
    .then(response => response.json()) // converte a resposta para JSON
    .then(usuarios => {
      // exibe os nomes dos usuários no console
      usuarios.forEach(usuario => {
        console.log(usuario.name);
      });
    })
    .catch(erro => {
      // mostra erro caso algo dê errado na requisição
      console.error("Erro ao buscar usuários:", erro);
    });
}

// chama a função
buscarUsuarios();