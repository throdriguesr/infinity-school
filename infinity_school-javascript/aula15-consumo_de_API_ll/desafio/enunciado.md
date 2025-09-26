PRATIQUE E APRENDA

Você foi contratado para desenvolver um dashboard que exiba uma lista de produtos de uma loja virtual.
Siga as instruções abaixo para construir sua aplicação:

Requisitos:

- Utilizar a API fictícia: https://api.example.com/produtos?page=X
- Cada produto contém: nome, preco, estoque, dataLancamento.

Implementar as funcionalidades:

- Exibir a lista de produtos com paginação.
- Exibir somente produtos com estoque disponível ao aplicar o filtro.
- Tratar erros de resposta da API, como status inválido ou timeout.
- Formatar preços para o formato R$0,00 e datas para o formato DD/MM/AAAA.

Passo a Passo:

1 - Criar a Estrutura HTML:
- Uma tabela para exibir os produtos.
- Botões de navegação para avançar e retroceder nas páginas.
- Um botão para ativar o filtro de estoque.

2 - Implementar o Consumo da API:
- Usar fetch para obter os dados.
- Tratar respostas com response.ok e erros de conexão.

3 - Adicionar Funcionalidades:
- Paginação: Atualizar os produtos exibidos ao clicar nos botões de página.
- Filtragem: Exibir somente produtos com estoque ao ativar o filtro.
- Formatação: Ajustar preços e datas antes de exibi-los.

4 - Atualizar o DOM:
- Popular a tabela com os dados formatados.
- Exibir mensagens de erro caso a API retorne falhas.