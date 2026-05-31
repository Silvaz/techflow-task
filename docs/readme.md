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
