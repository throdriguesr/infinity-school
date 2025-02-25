📌 Conversor de Unidades

Desenvolva um programa que permita ao usuário converter entre diferentes unidades de medida, 
como metros para pés, quilogramas para libras, ou Celsius para Fahrenheit. 
Use módulos que contenham funções de conversão.

📋 Descrição

Este programa permite ao usuário converter entre diferentes unidades de medida, como:

- Metros para Pés
- Quilogramas para Libras
- Celsius para Fahrenheit

📂 Estrutura de Arquivos

manipulacao_strings/
│── main.py
│── conversor.py

🚀 Como Executar

1. Certifique-se de que os arquivos main.py e conversor.py estão na mesma pasta.
2. No terminal, execute o programa com: python main.py
3. Escolha a operação desejada no menu e forneça a string para manipulação.

🔧 Funcionalidades

- Conversão de Metros para Pés: O usuário insere um valor em metros, e o programa converte esse valor para pés.
- Conversão de Quilogramas para Libras: O usuário insere um valor em quilogramas, e o programa converte esse valor para libras.
- Conversão de Celsius para Fahrenheit: O usuário insere um valor em Celsius, e o programa converte esse valor para Fahrenheit.

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