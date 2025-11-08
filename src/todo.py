# tests/test_todo.py

# Importa a classe ToDoList que ainda vamos criar
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
# src/todo.py

class TarefaDuplicadaError(Exception):
    """Exceção lançada quando já existe uma tarefa com o mesmo título."""
    pass


class ToDoList:
    """
    Gerenciador de tarefas.

    Regras principais:
    - Não permite título vazio.
    - Não permite tarefas com títulos duplicados.
    """

    def __init__(self):
        # Lista interna que vai guardar as tarefas.
        # Cada tarefa é um dicionário com 'titulo' e 'status'.
        self._tarefas = []

    def adicionar_tarefa(self, titulo: str) -> None:
        """
        Adiciona uma tarefa na lista.

        Regras:
        - Título não pode ser vazio ou só espaços.
        - Título não pode se repetir.
        """
        # strip() remove espaços do início e do fim
        titulo_normalizado = titulo.strip()

        # Validação de título vazio
        if not titulo_normalizado:
            raise ValueError("Título da tarefa não pode ser vazio.")

        # Verifica se já existe tarefa com o mesmo título
        if any(t["titulo"] == titulo_normalizado for t in self._tarefas):
            raise TarefaDuplicadaError(
                f"Já existe uma tarefa com o título '{titulo_normalizado}'."
            )

        nova_tarefa = {
            "titulo": titulo_normalizado,
            "status": "pendente",
        }
        self._tarefas.append(nova_tarefa)

    def listar_tarefas(self):
        """
        Retorna uma cópia da lista de tarefas.

        Usamos list(...) para evitar que o código externo modifique
        a lista interna diretamente.
        """
        return list(self._tarefas)
    
    class TodoList:
        ...# restante do código permanece o mesmo
        def remover_tarefa(self, titulo: str) -> None:
            """
            Remove uma tarefa da lista pelo título.

            Levanta ValueError se a tarefa não for encontrada.
            """
            titulo_normalizado = titulo.strip()

            for i, tarefa in enumerate(self._tarefas):
                if tarefa["titulo"] == titulo_normalizado:
                    # Remove a tarefa da lista pela a posição

                    self._tarefas[i]
                    return
            
            # Se a tarefa não foi encontrada, levanta erro
            raise ValueError(f"Tarefa com título '{titulo_normalizado}' não encontrada.")
             f"Não foi encontrada tarefa com o título '{titulo_normalizado}'."