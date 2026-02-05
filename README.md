# Sistema de Atendimento por Prioridade

Este projeto implementa um **sistema simples de atendimento ao cliente com fila por prioridade**, desenvolvido em Python, com foco em **estruturas de dados**, **organização de código** e **lógica de ordenação**.

O objetivo é simular o funcionamento de um sistema de suporte técnico onde solicitações são atendidas de acordo com o nível de prioridade e, em caso de empate, pela ordem de chegada.

---

## 🎯 Objetivo do Projeto

- Aplicar conceitos de **fila com prioridade**
- Trabalhar com **listas, dicionários e funções**
- Separar **lógica do sistema** e **execução/testes**
- Demonstrar organização e clareza de código para fins de portfólio

---

## 🧠 Regras de Prioridade

Cada solicitação possui um tipo de problema, que define sua prioridade:

| Tipo de problema | Prioridade |
|------------------|------------|
| Software         | 3 (alta)   |
| Hardware         | 2 (média)  |
| Consultoria      | 1 (baixa)  |

As solicitações são atendidas seguindo as regras:
1. Maior prioridade primeiro
2. Em caso de empate, quem chegou antes é atendido primeiro

---

## 🗂️ Estrutura do Projeto

sistema_atendimento/
│
├── sistema.py
├── teste.py 
└── README.md

---

## ⚙️ Funcionamento do Sistema

O sistema é composto por três funções principais:

- `criar_solicitacao(...)`  
  Cria uma solicitação contendo cliente, tipo de problema, prioridade e ordem de chegada.

- `inserir_solicitacao(fila, solicitacao)`  
  Insere a solicitação na fila respeitando as regras de prioridade e ordem.

- `atender_solicitacao(fila)`  
  Remove e retorna a próxima solicitação a ser atendida.

O controle da ordem de chegada é feito por meio de um contador externo, garantindo que cada solicitação tenha uma ordem única.

---

## ▶️ Como Executar

1. Clone o repositório
2. Execute o arquivo de testes:

```bash
python teste.py
```
