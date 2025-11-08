def test_remover_tarefa_existente():
    """
    Quando eu removo uma tarefa existente,
    ela não deve mais aparecer na lista.
    """
    lista = ToDoList()
    lista.adicionar_tarefa("Tarefa 1")
    lista.adicionar_tarefa("Tarefa 2")

    lista.remover_tarefa("Tarefa 1")

    titulos = [t["titulo"] for t in lista.listar_tarefas()]
    assert "Tarefa 1" not in titulos
    assert "Tarefa 2" in titulos
