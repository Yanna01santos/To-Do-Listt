import os
import sys

# Adiciona o diretório src ao PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "src")))
class TarefaDuplicadaError(Exception):
    """Exceção lançada quando já existe uma tarefa com o mesmo título."""
    pass

class ToDoList:
    """
    Gerenciador de tarefas.
    
    Responsabilidades:
    - Gerenciar lista de tarefas (adicionar, remover, concluir)
    - Validar regras de negócio (título único, não vazio)
    - Manter estado consistente das tarefas
    """

    def __init__(self) -> None:
        self._tarefas: list[dict[str, str]] = []

    def adicionar_tarefa(self, titulo: str) -> None:
        """Adiciona nova tarefa à lista."""
        titulo_normalizado = self._validar_titulo(titulo)
        
        if self._tarefa_existe(titulo_normalizado):
            raise TarefaDuplicadaError(f"Já existe tarefa '{titulo_normalizado}'")

        self._tarefas.append({
            "titulo": titulo_normalizado,
            "status": "pendente"
        })

    def remover_tarefa(self, titulo: str) -> None:
        """Remove tarefa da lista pelo título."""
        titulo_normalizado = self._validar_titulo(titulo)
        
        for i, tarefa in enumerate(self._tarefas):
            if tarefa["titulo"] == titulo_normalizado:
                self._tarefas.pop(i)
                return
                
        raise ValueError(f"Tarefa '{titulo_normalizado}' não encontrada")

    def concluir_tarefa(self, titulo: str) -> None:
        """Marca tarefa como concluída."""
        titulo_normalizado = self._validar_titulo(titulo)
        
        for tarefa in self._tarefas:
            if tarefa["titulo"] == titulo_normalizado:
                tarefa["status"] = "concluída"
                return
                
        raise ValueError(f"Tarefa '{titulo_normalizado}' não encontrada")

    def listar_tarefas(self) -> list[dict[str, str]]:
        """Retorna cópia da lista de tarefas."""
        return [tarefa.copy() for tarefa in self._tarefas]

    def _validar_titulo(self, titulo: str) -> str:
        """Valida e normaliza título."""
        titulo_normalizado = titulo.strip()
        if not titulo_normalizado:
            raise ValueError("Título não pode ser vazio")
        return titulo_normalizado

    def _tarefa_existe(self, titulo: str) -> bool:
        """Verifica se já existe tarefa com título."""
        return any(t["titulo"] == titulo for t in self._tarefas)