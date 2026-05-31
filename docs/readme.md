# TechFlow Tasks

Sistema de gerenciamento de tarefas desenvolvido para a startup de logística LogiStart,
construído com metodologia ágil (Kanban + Scrum).

## Objetivo
Permitir o acompanhamento do fluxo de trabalho em tempo real, priorizando tarefas
críticas e monitorando o desempenho da equipe.

## Metodologia
Utilizamos uma abordagem híbrida **Kanban + Scrum**:
- Quadro Kanban no GitHub Projects para visualização do fluxo
- Commits semânticos para rastreabilidade das mudanças
- Pipeline de CI para garantia de qualidade contínua

## Como executar

**Requisitos:** Python 3.11+

```
# Instalar dependências
pip install pytest

# Rodar o sistema
python src/tasks.py

# Rodar os testes
pytest tests/ -v

## Mudança de Escopo
**Alteração:** Adição de filtro de tarefas por prioridade (alta, média, baixa).

**Justificativa:** Durante o desenvolvimento, identificou-se que a startup necessitava
visualizar rapidamente tarefas críticas sem percorrer toda a lista. A funcionalidade
de filtro por prioridade agrega valor imediato ao cliente sem impactar o prazo de entrega.

**Impacto:** Novo card adicionado ao Kanban ("Implementar filtro por prioridade"),
nova função incluída no módulo `tasks.py`.
