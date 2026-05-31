
# Módulo de gerenciamento de tarefas - TechFlow Solutions
# CRUD completo usando arquivo JSON como banco de dados

import json
import os

ARQUIVO = "tasks.json"

def carregar_tarefas():
    """Carrega tarefas do arquivo JSON."""
    if not os.path.exists(ARQUIVO):
        return []
    with open(ARQUIVO, "r") as f:
        return json.load(f)

def salvar_tarefas(tarefas):
    """Salva tarefas no arquivo JSON."""
    with open(ARQUIVO, "w") as f:
        json.dump(tarefas, f, indent=2)

def criar_tarefa(titulo, descricao, prioridade="media"):
    """Cria uma nova tarefa e retorna ela."""
    tarefas = carregar_tarefas()
    nova = {
        "id": len(tarefas) + 1,
        "titulo": titulo,
        "descricao": descricao,
        "prioridade": prioridade,
        "status": "a_fazer"
    }
    tarefas.append(nova)
    salvar_tarefas(tarefas)
    return nova

def listar_tarefas():
    """Retorna todas as tarefas."""
    return carregar_tarefas()

def atualizar_tarefa(id_tarefa, novos_dados):
    """Atualiza campos de uma tarefa pelo ID."""
    tarefas = carregar_tarefas()
    for tarefa in tarefas:
        if tarefa["id"] == id_tarefa:
            tarefa.update(novos_dados)
            salvar_tarefas(tarefas)
            return tarefa
    return None

def deletar_tarefa(id_tarefa):
    """Remove uma tarefa pelo ID."""
    tarefas = carregar_tarefas()
    filtradas = [t for t in tarefas if t["id"] != id_tarefa]
    if len(filtradas) == len(tarefas):
        return False
    salvar_tarefas(filtradas)
    return True
