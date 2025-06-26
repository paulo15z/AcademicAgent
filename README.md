# AI Academic Agent

Agente de IA e workflow inteligente para resolução, auxílio e formatação de atividades acadêmicas. Utiliza pydanticAI para validação de dados, OpenAI GPT-4.1-nano agent para geração de conteúdo, e é projetado para fácil extensão com novas ferramentas e integrações (ex: langgraphs, MCP server).

## Visão Geral

Este projeto implementa um agente de IA modular e extensível, focado em automatizar tarefas acadêmicas como redação, revisão, formatação (ex: ABNT), sumarização, explicação de conceitos e tradução. O objetivo é facilitar a vida de estudantes, professores e pesquisadores, fornecendo assistência inteligente e customizável.

## Principais Recursos
- **Workflows acadêmicos customizáveis** (redação, revisão, formatação, etc)
- **Validação inteligente de dados** com pydanticAI
- **Geração de conteúdo** com OpenAI GPT-4.1-nano agent
- **Extensibilidade** para novas ferramentas e integrações futuras (langgraphs, MCP, etc)
- **Testes automatizados** e documentação clara

## Arquitetura

```
src/
  academic_agent/
    core/         # Núcleo do agente e orquestração
    workflows/    # Workflows acadêmicos
    validation/   # Validação de dados (pydanticAI)
    llm/          # Integração com modelos OpenAI
    extensions/   # Extensões e integrações futuras
  tests/          # Testes unitários e de integração
  docs/           # Documentação adicional
  examples/       # Exemplos de uso
  scripts/        # Scripts utilitários
```

## Como Usar

### Pré-requisitos
- Python 3.10+
- pip

### Instalação

```bash
# Clone o repositório
git clone <repo-url>
cd ai-academic-agent

# Crie e ative um ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows

# Instale as dependências
pip install -r requirements.txt
```

### Rodando o Agente

```bash
python -m src.academic_agent.core.agent
```

- Exemplos de configuração e execução estão na pasta `examples/`.

### Testes

```bash
pytest --cov=src/academic_agent
```

- Testes unitários e de integração estão em `/tests`, seguindo a estrutura do projeto.

## Contribuindo
- Siga o padrão de código (PEP8, type hints, docstrings Google style)
- Sempre escreva testes para novas funcionalidades
- Atualize a documentação quando necessário
- Veja o arquivo `PLANNING.md` para arquitetura e padrões

## Roadmap
- [ ] Implementação do agente core e integração OpenAI
- [ ] Workflows acadêmicos (redação, revisão, formatação)
- [ ] Ferramentas de sumarização, explicação e tradução
- [ ] Pontos de extensão para langgraphs, MCP, etc
- [ ] Documentação e testes completos

## Referências
- [pydanticAI](https://github.com/pydantic/pydantic-ai)
- [OpenAI API](https://platform.openai.com/docs)
- [LangGraph](https://github.com/langchain-ai/langgraph)
- [MCP Specification](https://spec.modelcontextprotocol.io/)

---

> Projeto criado para facilitar a vida acadêmica com automação e inteligência artificial. Sinta-se à vontade para contribuir!
