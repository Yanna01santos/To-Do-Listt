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