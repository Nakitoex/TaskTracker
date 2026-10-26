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
├── src/
│  └── main.py              # Ponto de entrada da aplicação
├── storage.py           # Camada de persistência de dados
├── Docs/
│   └── Planejamento Lógico       # Documento do planejamento do projeto
└── README.md             # Documentação do projeto
```
### Pré-requisitos

- Python 3.8 ou superior instalado na máquina

## 🚀 Como Executar

## 🐳 Docker

**Pré-requisito:** Docker instalado.

Como construir a imagem:
```bash
docker build -t tasktracker .
```

Como rodar o container em modo isolado:
```bash
docker run -it --rm tasktracker
```

Como rodar via orquestração (Recomendado):
```bash
docker compose run --rm tasktracker
```

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
