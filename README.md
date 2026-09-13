# TaskTracker

Sistema simples de gerenciamento de tarefas (Task Tracker) desenvolvido em Python como projeto acadêmico.

**Autor:** Arthur Pozzetti

---

## 📋 Sobre o Projeto

O TaskTracker é uma aplicação de linha de comando (CLI) desenvolvida em Python para gerenciamento de tarefas pessoais. O sistema permite que o usuário crie, visualize, atualize e remova tarefas, controlando seu status de conclusão de forma simples e eficiente.

Este projeto foi desenvolvido como parte de uma avaliação acadêmica, com foco na aplicação de conceitos fundamentais de programação, estruturação de código e boas práticas de desenvolvimento em Python.

---

## ✨ Funcionalidades

- ➕ Adicionar novas tarefas
- 📄 Listar todas as tarefas cadastradas
- ✏️ Editar/atualizar uma tarefa existente
- ✅ Marcar tarefas como concluídas
- ❌ Remover tarefas
- 💾 Persistência de dados (armazenamento local)

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**
- Bibliotecas padrão do Python (sem dependências externas obrigatórias)

---

## 📁 Estrutura do Projeto

```
tasktracker/
│
├── main.py              # Ponto de entrada da aplicação
├── tasks.py             # Lógica de manipulação das tarefas
├── storage.py           # Camada de persistência de dados
├── data/
│   └── tasks.json        # Arquivo de armazenamento das tarefas
├── requirements.txt      # Dependências do projeto
└── README.md             # Documentação do projeto
```

> A estrutura acima é uma referência; ajuste conforme a organização real dos arquivos do repositório.

---

## 🚀 Como Executar

### Pré-requisitos

- Python 3.8 ou superior instalado na máquina

### Passo a passo

## 💻 Exemplo de Uso

```
===== TaskTracker =====
1. Adicionar tarefa
2. Listar tarefas
3. Concluir tarefa
4. Remover tarefa
5. Sair
Escolha uma opção: 1

Digite a descrição da tarefa: Estudar para a prova de Estruturas de Dados
Tarefa adicionada com sucesso!
```

---

## 🗺️ Possíveis Melhorias Futuras

- Implementação de interface gráfica (GUI)
- Integração com banco de dados (SQLite/PostgreSQL)
- Filtros e ordenação de tarefas por prioridade ou data
- Testes automatizados com `pytest`

---

## 📄 Licença

Este projeto foi desenvolvido para fins educacionais como parte de um trabalho acadêmico.

---

## 👤 Autor

**Arthur Pozzetti**
Projeto desenvolvido para disciplina da faculdade.
