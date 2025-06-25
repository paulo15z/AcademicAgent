Purpose: Tracks current tasks, backlog, and sub-tasks.
Includes: Bullet list of active work, milestones, and anything discovered mid-process.
Prompt to AI: “Update TASK.md to mark XYZ as done and add ABC as a new task.”
Can prompt the LLM to automatically update and create tasks as well (through global rules).


# TASK.md - Primeiros Passos e Requisitos

## Requisitos do Sistema

### Requisitos de Software
- **Python**: 3.9 ou superior
- **pip**: Gerenciador de pacotes Python
- **Git**: Controle de versão
- **Docker**: (Opcional) Para containerização
- **Make**: (Opcional) Para automação de tarefas

### Requisitos de Hardware
- **RAM**: Mínimo 4GB, recomendado 8GB+
- **CPU**: Dual-core ou superior
- **Armazenamento**: 1GB de espaço livre
- **Rede**: Conexão estável para download de dependências

## Setup Inicial do Ambiente

### 1. Preparação do Ambiente de Desenvolvimento

```bash
# Clonar ou criar o repositório
git init mcp-server-python
cd mcp-server-python

# Criar ambiente virtual
python -m venv venv

# Ativar ambiente virtual
# No Linux/Mac:
source venv/bin/activate
# No Windows:
# venv\Scripts\activate

# Atualizar pip
pip install --upgrade pip setuptools wheel
```

### 2. Estrutura Inicial do Projeto

```
mcp-server-python/
├── .github/
│   └── workflows/
│       └── ci.yml
├── src/
│   └── mcp_server/
│       ├── __init__.py
│       ├── core/
│       │   ├── __init__.py
│       │   ├── server.py
│       │   └── protocol.py
│       ├── resources/
│       │   ├── __init__.py
│       │   └── base.py
│       ├── tools/
│       │   ├── __init__.py
│       │   └── base.py
│       └── transport/
│           ├── __init__.py
│           └── stdio.py
├── tests/
│   ├── __init__.py
│   ├── test_core/
│   ├── test_resources/
│   └── test_tools/
├── examples/
│   ├── simple_server.py
│   └── filesystem_server.py
├── docs/
│   ├── api.md
│   └── examples.md
├── scripts/
│   ├── setup.sh
│   └── test.sh
├── .gitignore
├── .pre-commit-config.yaml
├── pyproject.toml
├── requirements.txt
├── requirements-dev.txt
├── README.md
├── CHANGELOG.md
└── Makefile
```

## Tarefas Prioritárias (Semana 1)

### Task 1: Configuração do Projeto ⏱️ 4h
**Prioridade**: Alta

**Subtarefas**:
- [ ] Criar estrutura de diretórios
- [ ] Configurar pyproject.toml
- [ ] Criar requirements.txt e requirements-dev.txt
- [ ] Configurar .gitignore
- [ ] Setup inicial do README.md

**Entregável**: Estrutura básica do projeto configurada

### Task 2: Dependências Core ⏱️ 2h
**Prioridade**: Alta

**Dependências principais**:
```txt
asyncio-core>=3.9
pydantic>=2.0.0
websockets>=11.0
aiohttp>=3.8.0
```

**Dependências de desenvolvimento**:
```txt
pytest>=7.0.0
pytest-asyncio>=0.21.0
black>=23.0.0
flake8>=6.0.0
mypy>=1.0.0
pre-commit>=3.0.0
coverage>=7.0.0
```

**Subtarefas**:
- [ ] Instalar dependências principais
- [ ] Configurar ferramentas de desenvolvimento
- [ ] Testar importações básicas

### Task 3: Protocolo MCP Base ⏱️ 8h
**Prioridade**: Alta

**Arquivo**: `src/mcp_server/core/protocol.py`

**Subtarefas**:
- [ ] Definir estruturas de dados base (Request, Response, Error)
- [ ] Implementar tipos Pydantic para mensagens MCP
- [ ] Criar validação de protocolo
- [ ] Implementar serialização/deserialização JSON-RPC

**Entregável**: Classes base do protocolo MCP funcionais

### Task 4: Servidor Core ⏱️ 12h
**Prioridade**: Alta

**Arquivo**: `src/mcp_server/core/server.py`

**Subtarefas**:
- [ ] Implementar classe MCPServer base
- [ ] Gerenciamento de sessões
- [ ] Roteamento de mensagens
- [ ] Handler para inicialização/capability negotiation
- [ ] Sistema básico de logging

**Entregável**: Servidor MCP básico que aceita conexões

### Task 5: Transport Layer - STDIO ⏱️ 6h
**Prioridade**: Alta

**Arquivo**: `src/mcp_server/transport/stdio.py`

**Subtarefas**:
- [ ] Implementar transporte via STDIO
- [ ] Leitura assíncrona de stdin
- [ ] Escrita para stdout
- [ ] Tratamento de erros de comunicação

**Entregável**: Comunicação STDIO funcional

## Tarefas Secundárias (Semana 2)

### Task 6: Sistema de Resources ⏱️ 10h
**Prioridade**: Média

**Arquivos**: `src/mcp_server/resources/`

**Subtarefas**:
- [ ] Implementar classe base Resource
- [ ] Resource de sistema de arquivos básico
- [ ] Registry de resources
- [ ] Handlers para list_resources, read_resource

### Task 7: Sistema de Tools ⏱️ 8h
**Prioridade**: Média

**Arquivos**: `src/mcp_server/tools/`

**Subtarefas**:
- [ ] Implementar classe base Tool
- [ ] Tool de exemplo (echo, file operations)
- [ ] Registry de tools
- [ ] Handlers para list_tools, call_tool

### Task 8: Testes Unitários ⏱️ 12h
**Prioridade**: Média

**Subtarefas**:
- [ ] Testes para protocol.py
- [ ] Testes para server.py
- [ ] Testes para transport layer
- [ ] Setup de coverage

### Task 9: Exemplo Prático ⏱️ 6h
**Prioridade**: Baixa

**Arquivo**: `examples/simple_server.py`

**Subtarefas**:
- [ ] Servidor de exemplo funcional
- [ ] Documentação do exemplo
- [ ] Script de demonstração

## Configurações Essenciais

### pyproject.toml (Base)
```toml
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "mcp-server"
version = "0.1.0"
description = "Model Context Protocol Server Implementation in Python"
authors = [{name = "Your Name", email = "your.email@example.com"}]
requires-python = ">=3.9"
dependencies = [
    "pydantic>=2.0.0",
    "websockets>=11.0",
    "aiohttp>=3.8.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=7.0.0",
    "pytest-asyncio>=0.21.0",
    "black>=23.0.0",
    "flake8>=6.0.0",
    "mypy>=1.0.0",
    "pre-commit>=3.0.0",
    "coverage>=7.0.0",
]
```

### Comandos Úteis

```bash
# Instalar dependências
pip install -e .
pip install -e ".[dev]"

# Executar testes
pytest
pytest --cov=src/mcp_server

# Formatação de código
black src/ tests/
flake8 src/ tests/
mypy src/

# Pre-commit hooks
pre-commit install
pre-commit run --all-files
```

## Marcos e Entregáveis

### Marco 1 (Fim da Semana 1)
- [ ] Projeto configurado e funcional
- [ ] Protocolo MCP base implementado
- [ ] Servidor aceita conexões básicas
- [ ] Transporte STDIO funcional

### Marco 2 (Fim da Semana 2)
- [ ] Sistema de resources básico
- [ ] Sistema de tools básico
- [ ] Testes unitários passando
- [ ] Exemplo funcional

## Critérios de Aceitação

### Para cada task:
1. **Funcionalidade**: Código funcional conforme especificação
2. **Testes**: Cobertura mínima de 80%
3. **Qualidade**: Passar em linting e type checking
4. **Documentação**: Docstrings e comentários adequados

### Para o projeto:
1. **Conformidade MCP**: Aderir à especificação oficial
2. **Performance**: Responder em <100ms para operações básicas
3. **Robustez**: Tratamento adequado de erros
4. **Extensibilidade**: Fácil adição de novos resources/tools

## Recursos de Apoio

### Documentação Técnica
- [MCP Specification](https://spec.modelcontextprotocol.io/)
- [JSON-RPC 2.0](https://www.jsonrpc.org/specification)
- [Pydantic Documentation](https://docs.pydantic.dev/)
- [asyncio Documentation](https://docs.python.org/3/library/asyncio.html)

### Ferramentas de Debug
- **pytest-asyncio**: Para testes assíncronos
- **aiohttp-devtools**: Debug de aplicações async
- **python-json-logger**: Logging estruturado

### Próximos Passos Imediatos

1. **Hoje**: Configurar ambiente e estrutura do projeto
2. **Amanhã**: Começar implementação do protocolo base
3. **Esta semana**: Completar servidor básico funcional
4. **Próxima semana**: Implementar resources e tools