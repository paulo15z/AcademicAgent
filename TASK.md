Purpose: Tracks current tasks, backlog, and sub-tasks.
Includes: Bullet list of active work, milestones, and anything discovered mid-process.
Prompt to AI: "Update TASK.md to mark XYZ as done and add ABC as a new task."
Can prompt the LLM to automatically update and create tasks as well (through global rules).


# TASK.md - AI Academic Agent

## Requisitos do Sistema

### Requisitos de Software
- **Python**: 3.10 ou superior
- **pip**: Gerenciador de pacotes Python
- **Git**: Controle de versão

### Requisitos de Hardware
- **RAM**: Mínimo 4GB, recomendado 8GB+
- **CPU**: Dual-core ou superior
- **Armazenamento**: 1GB de espaço livre
- **Rede**: Conexão estável para download de dependências

## Setup Inicial do Ambiente

```bash
# Clonar o repositório
git clone <repo-url>
cd ai-academic-agent

# Criar ambiente virtual
python -m venv venv

# Ativar ambiente virtual
# Linux/Mac: source venv/bin/activate
# Windows: venv\Scripts\activate

# Atualizar pip
pip install --upgrade pip setuptools wheel
```

## Tarefas Prioritárias (Semana 1)

### Task 1: Estrutura Inicial do Projeto ⏱️ 4h
**Prioridade**: Alta

**Subtarefas**:
- [ ] Criar estrutura de diretórios (core, workflows, validation, llm, extensions)
- [ ] Configurar pyproject.toml
- [ ] Criar requirements.txt e requirements-dev.txt
- [ ] Configurar .gitignore
- [ ] Setup inicial do README.md

**Entregável**: Estrutura básica do projeto configurada

### Task 2: Dependências Core ⏱️ 2h
**Prioridade**: Alta

**Dependências principais**:
```txt
pydanticAI>=0.1.0
openai>=1.0.0
```

**Dependências de desenvolvimento**:
```txt
pytest>=7.0.0
black>=23.0.0
mypy>=1.0.0
flake8>=6.0.0
pre-commit>=3.0.0
```

**Subtarefas**:
- [ ] Instalar dependências principais
- [ ] Configurar ferramentas de desenvolvimento
- [ ] Testar importações básicas

### Task 3: Agente Core e Integração OpenAI ⏱️ 8h
**Prioridade**: Alta

**Subtarefas**:
- [x] Implementar classe base do agente acadêmico
- [x] Integrar com OpenAI GPT-4.1-nano agent
- [x] Testes unitários básicos

**Status**: Concluído (2024-08-01)

### Task 4: Workflows Acadêmicos ⏱️ 10h
**Prioridade**: Alta

**Subtarefas**:
- [x] Implementar workflow de redação acadêmica
- [x] Implementar workflow de revisão e formatação (ex: ABNT)
- [x] Testes de integração

## Tarefas Secundárias (Semana 2+)

### Task 5: Ferramentas e Extensões ⏱️ 8h
**Prioridade**: Média

**Subtarefas**:
- [x] Sumarização automática
- [ ] Explicação de conceitos
- [ ] Tradução
- [ ] Pontos de extensão para integrações futuras (langgraphs, MCP)

### Task 6: Testes e Documentação ⏱️ 6h
**Prioridade**: Média

**Subtarefas**:
- [ ] Cobertura de testes > 90%
- [ ] Documentação de workflows e exemplos

### Task 7: Implementação da Base de Conhecimento (Database) ⏱️ 20h
**Prioridade**: Altíssima

**Subtarefas**:
- [ ] Configurar SQLAlchemy e SQLite
- [ ] Definir modelos de dados (ex: Documento, Pedaço de Texto)
- [ ] Criar camada de persistência para salvar e buscar dados
- [ ] Implementar workflow para "ingerir" documentos para a base de dados
- [ ] Refatorar workflow de sumarização para usar documentos da base de dados

## Discovered During Work
- [ ] (Adicionar aqui novas tarefas ou bugs encontrados durante o desenvolvimento)

## Backlog / Ideias Futuras
- [ ] Workflow de Explicação de Conceitos
- [ ] Workflow de Tradução
- [ ] Workflow de Guia de Estudos (depende do DB)

## Configurações Essenciais

### pyproject.toml (Base)
```