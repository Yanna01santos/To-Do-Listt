# Gerenciador de Tarefas (To-Do List)

Uma aplicação simples para gerenciar tarefas, desenvolvida em Python usando TDD (Test Driven Development).

## Funcionalidades

- ✅ Adicionar novas tarefas
- ✅ Remover tarefas existentes
- ✅ Marcar tarefas como concluídas
- ✅ Listar todas as tarefas
- ❌ Validação de títulos duplicados
- ❌ Tratamento de erros personalizado

## Instalação

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/To-Do-Listt.git
cd To-Do-Listt
```

2. Crie e ative um ambiente virtual:
```bash
python -m venv .venv
.venv\Scripts\activate
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

## Executando os Testes

Para rodar os testes unitários:

```bash
python -m pytest -v
```

## Estrutura do Projeto

```
To-Do-Listt/
├── src/
│   ├── __init__.py
│   └── todo.py
├── test/
│   └── test_todo.py
├── README.md
└── requirements.txt
```

## Como Usar

```python
from src.todo import ToDoList

# Criar nova lista
lista = ToDoList()

# Adicionar tarefas
lista.adicionar_tarefa("Estudar Python")
lista.adicionar_tarefa("Fazer exercícios")

# Concluir tarefa
lista.concluir_tarefa("Estudar Python")

# Listar tarefas
tarefas = lista.listar_tarefas()

# Remover tarefa
lista.remover_tarefa("Fazer exercícios")
```

## Contribuindo

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## Licença

Este projeto está licenciado sob a MIT License - veja o arquivo [LICENSE](LICENSE) para detalhes.