# 💰 Sistema Bancário em Python - Versão 3

Este projeto foi desenvolvido como parte de um **desafio prático da DIO (Digital Innovation One)**.  
O objetivo foi **refatorar o sistema bancário** utilizando **Programação Orientada a Objetos (POO)**, seguindo boas práticas e o **modelo de classes UML**.

Nesta versão, temos **duas implementações** diferentes:  
- **Primeiro Desafio** → Criação da modelagem com classes e herança  
- **Desafio Extra** → Atualização completa do menu para trabalhar 100% com objetos

---

## 🚀 Funcionalidades

O sistema simula um **caixa eletrônico** e oferece as seguintes operações:

- **Depósito** 💵  
  - Registra operações com a classe `Deposito`
- **Saque** 🏧  
  - Controla limite de **R$ 500,00 por saque**
  - Permite **até 3 saques diários**
  - Implementado com a classe `Saque`
- **Extrato** 📄  
  - Usa o `Historico` para exibir todas as movimentações registradas
- **Cadastro de Usuário** 👤  
  - Agora representado pela classe `PessoaFisica`
  - Nome, CPF, data de nascimento e endereço são armazenados como atributos
- **Cadastro de Conta Corrente** 🏦  
  - Modelada com a classe `ContaCorrente`
  - Número da conta é gerado automaticamente
  - Agência padrão: `0001`
  - Permite **múltiplas contas por cliente**
- **Listar Contas** 📋  
  - Mostra número, agência e titular de todas as contas cadastradas
- **Histórico de Transações** ⏳  
  - Implementado na classe `Historico`
  - Cada depósito e saque é registrado individualmente
- **Sair do Sistema** ❌  

---

## 📦 Como executar

1. **Clone o repositório**:
```bash
git clone https://github.com/Lipebarreiro/Sistema_bancario_DIO_v3.git
```

2. **Acesse a pasta do projeto**:
```bash
cd Sistema_bancario_DIO_v3
```

3. **Escolha qual versão deseja executar**:

- Para o **primeiro desafio** (versão base):
```bash
python sistema_bancario_v3.py
```
- Para o **desafio extra** (menu atualizado):
```bash
python sistema_bancario_v3_extra.py
```

---

## 🧠 Aprendizados

Com a versão 3, foi possível aplicar conceitos avançados:

- **POO em Python**:  
  - Classes, herança, atributos e métodos
- **Modelagem UML** para guiar a implementação
- **Polimorfismo**:  
  - Transações (`Deposito` e `Saque`) herdando de `Transacao`
- **Histórico de Operações** com registro automático
- Separação clara entre **usuário**, **conta** e **transação**
- Implementação de **múltiplas contas por cliente**

---

## 🛠 Tecnologias Utilizadas

- **Python 3**

---

## 📌 Observações

- Este projeto **não utiliza banco de dados**.  
- Todos os dados são mantidos **em memória** durante a execução.  
- Ideal para fins **educacionais** e prática de **POO**.
