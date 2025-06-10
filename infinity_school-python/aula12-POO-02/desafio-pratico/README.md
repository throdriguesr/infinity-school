# 💰 Sistema de Contas Bancárias em Python

Este é um projeto simples feito em Python para simular contas bancárias.  
Ele usa herança e polimorfismo, conceitos da programação orientada a objetos.

## ✅ O que o sistema faz

- Cria contas do tipo Corrente ou Poupança
- Faz depósitos e saques
- Permite usar limite (na conta corrente)
- Adiciona juros (na conta poupança)
- Mostra um resumo da conta

## 🧱 Como funciona

### Conta (classe base)

Toda conta tem:
- Número
- Nome do titular
- Saldo

Ela pode:
- Depositar dinheiro
- Sacar dinheiro
- Mostrar o saldo
- Mostrar um resumo

### ContaCorrente (herda de Conta)

Tem:
- Taxa de manutenção
- Limite do cheque especial

Pode sacar mesmo sem saldo, usando o limite.

### ContaPoupanca (herda de Conta)

Tem:
- Taxa de juros

Pode calcular e adicionar juros ao saldo.

## ▶️ Como usar

1. Salve o código em um arquivo chamado `banco.py`
2. Rode no terminal com:

```bash
python banco.py