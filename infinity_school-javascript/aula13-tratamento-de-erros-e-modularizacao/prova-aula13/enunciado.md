Desenvolvimento de Sistema de Cadastro de Usuários com Tratamento de Erros

Crie um programa em JavaScript que simule um sistema de cadastro de usuários. O sistema deve validar os dados de entrada e tratar possíveis erros para garantir a integridade do sistema. O programa deve incluir validação dos dados e lançamento de erros personalizados com mensagens específicas. Utilize boas práticas no tratamento de erros.

Requisitos do Projeto:

a) Interface HTML Inicial:
- Crie um formulário com campos Nome, Usuário, Senha, Email e Idade/ Data de nascimento.
- Inclua um botão "Cadastrar" que será usado para enviar o formulário.

b) Validação dos Dados:
- Ao clicar no botão "Cadastrar", o programa deve verificar se todos os campos estão preenchidos, em formato válido, e se a idade inserida é maior ou igual a 18 anos.

c) Lançamento de Erros:
- Para cada erro de validação, lance um erro com uma mensagem específica correspondente ao campo:

d) Tratamento de Erros:
- Utilize um bloco try...catch para capturar os erros lançados durante a validação.
- Exiba as mensagens de erro diretamente abaixo dos campos correspondentes, no formulário.

e) Cadastro Bem-Sucedido:
- Se todos os dados forem válidos, exiba uma mensagem de sucesso na tela, como: "Cadastro realizado com sucesso!".