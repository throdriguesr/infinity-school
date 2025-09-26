// função para criar um novo post
function criarPost() {
  // dados que serão enviados
  const novoPost = {
    title: "Meu título",
    body: "Conteúdo do post",
    userId: 1
  };

  // faz a requisição POST
  fetch("https://jsonplaceholder.typicode.com/posts", {
    method: "POST", // define método como POST
    headers: {
      "Content-Type": "application/json" // diz que os dados são JSON
    },
    body: JSON.stringify(novoPost) // converte objeto para JSON
  })
  .then(response => response.json()) // converte resposta para JSON
  .then(data => {
    // mostra objeto retornado no console
    console.log("Post criado:", data);
  })
  .catch(erro => {
    // mostra erro caso aconteça
    console.error("Erro ao criar post:", erro);
  });
}

// chama a função
criarPost();