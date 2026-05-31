# Testes unitários para o módulo de tarefas
# Executar com: pytest tests/

import pytest
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.tasks import criar_tarefa, listar_tarefas, atualizar_tarefa, deletar_tarefa

# Remove arquivo de teste antes e depois de cada teste
@pytest.fixture(autouse=True)
def limpar_arquivo():
    if os.path.exists("tasks.json"):
        os.remove("tasks.json")
    yield
    if os.path.exists("tasks.json"):
        os.remove("tasks.json")

def test_criar_tarefa():
    """Testa se uma tarefa é criada corretamente."""
    tarefa = criar_tarefa("Tarefa 1", "Descrição teste", "alta")
    assert tarefa["titulo"] == "Tarefa 1"
    assert tarefa["prioridade"] == "alta"
    assert tarefa["status"] == "a_fazer"

def test_listar_tarefas():
    """Testa se a listagem retorna todas as tarefas criadas."""
    criar_tarefa("Tarefa A", "Desc A")
    criar_tarefa("Tarefa B", "Desc B")
    tarefas = listar_tarefas()
    assert len(tarefas) == 2

def test_atualizar_tarefa():
    """Testa se uma tarefa é atualizada corretamente."""
    tarefa = criar_tarefa("Original", "Desc")
    atualizada = atualizar_tarefa(tarefa["id"], {"status": "concluido"})
    assert atualizada["status"] == "concluido"

def test_deletar_tarefa():
    """Testa se uma tarefa é removida corretamente."""
    tarefa = criar_tarefa("Para deletar", "Desc")
    resultado = deletar_tarefa(tarefa["id"])
    assert resultado == True
    assert len(listar_tarefas()) == 0
