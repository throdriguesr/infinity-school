📌 Manipulação de Strings

Crie um módulo chamado manipulacao_strings que contenha funções para realizar operações com strings, como inverter uma string, contar o número de palavras em uma string e verificar se uma string é um palíndromo (lê-se igual de trás para frente). 
Crie um programa principal que importe o módulo e use essas funções com strings fornecidas pelo usuário.

📋 Descrição

Este programa implementa um módulo de manipulação de strings (manipulacao_strings.py) com funções para:

- Inverter uma string
- Contar o número de palavras
- Verificar se uma string é um palíndromo

O programa principal (main.py) importa esse módulo e apresenta um menu interativo para o usuário.

📂 Estrutura de Arquivos

manipulacao_strings/
│── main.py
│── manipulacao_strings.py

🚀 Como Executar

1. Certifique-se de que os arquivos main.py e manipulacao_strings.py estão na mesma pasta.
2. No terminal, execute o programa com: python main.py
3. Escolha a operação desejada no menu e forneça a string para manipulação.
4. Após cada operação, o usuário pode decidir continuar ou sair do programa.

🔧 Funcionalidades

- Inversão de strings: transforma "Python" em "nohtyP".
- Contagem de palavras: "Olá, mundo!" retorna 2.
- Verificação de palíndromos: reconhece palavras como "radar" e "ovo".
- Menu interativo para facilitar a escolha das operações.

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
