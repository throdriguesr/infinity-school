📌 Calculadora Modular

Crie um programa que será uma calculadora.
Nesta calculadora você deverá ter um módulo para as operações matemáticas, o arquivo principal deverá conter apenas um menu de escolha para o usuário (soma, subtração, multiplicação e divisão).

📋 Descrição

Este programa implementa uma calculadora interativa que permite ao usuário realizar operações matemáticas básicas: soma, subtração, multiplicação e divisão. As operações são definidas em um módulo separado (operacoes.py), enquanto o arquivo principal (calculadora.py) contém apenas o menu de interação.

📂 Estrutura de Arquivos

calculadora/
│── calculadora.py
│── operacoes.py

🚀 Como Executar

1. Certifique-se de que os arquivos calculadora.py e operacoes.py estão na mesma pasta.
2. No terminal, execute o programa com: python calculadora.py
3. Escolha a operação desejada no menu e forneça os números.
4. Após cada operação, o usuário pode decidir continuar ou sair do programa.

🔧 Funcionalidades

- Operações básicas: soma, subtração, multiplicação e divisão.
- Verificação de entrada para evitar erros com caracteres inválidos.
- Opção de repetir operações sem precisar reiniciar o programa.

📌 Observações

O Python pode criar uma pasta __pycache__ automaticamente ao executar o programa. Essa pasta armazena versões compiladas dos arquivos para melhorar a performance.

- Caso queira excluir a pasta __pycache__, use o comando: rm -rf __pycache__
- ou no Windows: rmdir /s /q __pycache__

📌 Requisitos

- Python 3.x instalado
- Executar os scripts em um ambiente adequado (terminal, cmd ou IDE como VSCode, PyCharm, etc.)

💡 Dicas

Se ocorrer erro na importação dos módulos, verifique:

- Se os arquivos estão na mesma pasta.
- Se está executando o script principal.
- Se precisar rodar como módulo, use: python -m main