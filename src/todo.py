from src.todo import ToDoList

def test_adicionar_tarefa_cria_uma_tarefa():
    """
    Cenário:
    - Quando eu crio uma lista de tarefas
    - E adiciono uma tarefa com título válido
    - Então a lista deve ter exatamente 1 tarefa
    """
    lista = ToDoList()  # ainda não existe -> teste vai falhar primeiro (RED)
    lista.adicionar_tarefa("Estudar TDD")

    tarefas = ToDoList()  # ainda não existe -> teste vai falhar primeiro (R
    lista.adicionar_tarefa("Estudar TDD")

    tarefas = lista.listar_tarefas()

    assert len(tarefas) == 1
    assert tarefas[0]["titulo"] == "Estudar TDD"
    assert tarefas[0]["status"] == "pendente"

   # src/todo.py

class ToDoList:
    """
    Classe responsável por gerenciar uma lista de tarefas simples.

    Por enquanto:
    - Armazena tarefas em uma lista interna.
    - Cada tarefa é um dicionário com:
        - 'titulo'
        - 'status'
    """

    def __init__(self):
        # Lista interna que vai guardar as tarefas
        self._tarefas = []

    def adicionar_tarefa(self, titulo: str) -> None:
        """
        Adiciona uma nova tarefa na lista.

        Aqui, na fase GREEN, vamos fazer o mínimo:
        - Só adiciona sem nenhuma validação sofisticada.
        """
        nova_tarefa = {
            "titulo": titulo,
            "status": "pendente",
        }
        self._tarefas.append(nova_tarefa)

    def listar_tarefas(self):
        """
        Retorna a lista de tarefas.

        Retornamos a lista diretamente por enquanto.
        Mais pra frente, podemos melhorar (REFACTOR).
        """
        return self._tarefas
