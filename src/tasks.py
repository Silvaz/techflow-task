
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


if __name__ == "__main__":
    while True:
        print("\n=== TechFlow Tasks ===")
        print("1. Criar tarefa")
        print("2. Listar tarefas")
        print("3. Atualizar status da tarefa")
        print("4. Deletar tarefa")
        print("0. Sair")

        opcao = input("\nEscolha uma opção: ")

        match opcao:
            case "1":
                titulo = input("Título: ")
                descricao = input("Descrição: ")
                prioridade = input("Prioridade (alta/media/baixa): ")
                t = criar_tarefa(titulo, descricao, prioridade)
                print(f"✓ Tarefa '{t['titulo']}' criada com ID {t['id']}!")

            case "2":
                tarefas = listar_tarefas()
                if not tarefas:
                    print("Nenhuma tarefa cadastrada.")
                else:
                    print("\n--- Suas tarefas ---")
                    for t in tarefas:
                        print(f"  [ID {t['id']}] [{t['prioridade'].upper()}] {t['titulo']} — {t['status']}")

            case "3":
                [print(f"  [ID {t['id']}] {t['titulo']}") for t in listar_tarefas()]
                id_t = int(input("ID da tarefa: "))
                print("Status disponíveis: a_fazer / em_progresso / concluido")
                novo_status = input("Novo status: ")
                resultado = atualizar_tarefa(id_t, {"status": novo_status})
                if resultado:
                    print("✓ Tarefa atualizada!")
                else:
                    print("Tarefa não encontrada.")

            case "4":
                [print(f"  [ID {t['id']}] {t['titulo']}") for t in listar_tarefas()]
                id_t = int(input("ID da tarefa a deletar: "))
                if deletar_tarefa(id_t):
                    print("✓ Tarefa deletada!")
                else:
                    print("Tarefa não encontrada.")

            case "0":
                print("Encerrando... Até logo!")
                break

            case _:
                print("Opção inválida. Tente novamente.")
    print("=== TechFlow Tasks ===\n")

    # Criando tarefas
    t1 = criar_tarefa("Configurar repositório", "Criar estrutura de pastas no GitHub", "alta")
    t2 = criar_tarefa("Implementar CRUD", "Desenvolver sistema de tarefas em Python", "alta")
    t3 = criar_tarefa("Escrever testes", "Criar testes unitários com Pytest", "media")

    print("Tarefas criadas:")
    for t in listar_tarefas():
        print(f"  [{t['prioridade'].upper()}] {t['titulo']} — status: {t['status']}")

    # Atualizando uma tarefa
    atualizar_tarefa(1, {"status": "concluido"})
    print("\nApós atualizar tarefa 1:")
    for t in listar_tarefas():
        print(f"  {t['titulo']} — status: {t['status']}")

    # Deletando uma tarefa
    deletar_tarefa(3)
    print("\nApós deletar tarefa 3:")
    for t in listar_tarefas():
        print(f"  {t['titulo']}")
